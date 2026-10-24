"""
Enterprise Production Python Service (Project 09)

Demonstrates:
- 12-Factor app configuration loaded safely from environment variables
- Structured JSON logging with request tracing
- Liveness (/healthz) and Readiness (/readyz) health check monitors
- Robust error boundary middleware with latency instrumentation
- Graceful shutdown lifecycle management
"""

import json
import logging
import os
import time
import uuid
from dataclasses import asdict, dataclass
from typing import Any, Callable, Dict, Optional


@dataclass
class ServiceConfig:
    """12-factor configuration loaded from environment."""
    app_env: str = "development"
    port: int = 8080
    log_level: str = "INFO"
    service_name: str = "enterprise-api"
    readiness_flag: bool = True

    @classmethod
    def from_env(cls) -> "ServiceConfig":
        return cls(
            app_env=os.environ.get("APP_ENV", "development"),
            port=int(os.environ.get("PORT", "8080")),
            log_level=os.environ.get("LOG_LEVEL", "INFO").upper(),
            service_name=os.environ.get("SERVICE_NAME", "enterprise-api"),
            readiness_flag=os.environ.get("SERVICE_READY", "true").lower() in ("true", "1")
        )


class JsonLogFormatter(logging.Formatter):
    """Formats log records as single-line JSON objects for log aggregators (ELK, Datadog)."""

    def format(self, record: logging.LogRecord) -> str:
        payload = {
            "timestamp": self.formatTime(record, self.datefmt),
            "level": record.levelname,
            "message": record.getMessage(),
            "logger": record.name,
            "module": record.module,
            "lineno": record.lineno,
        }
        if hasattr(record, "request_id"):
            payload["request_id"] = getattr(record, "request_id")
        return json.dumps(payload)


@dataclass
class ServiceResponse:
    status_code: int
    body: Dict[str, Any]
    headers: Dict[str, str]
    duration_ms: float


class EnterpriseService:
    """Core enterprise microservice application."""

    def __init__(self, config: Optional[ServiceConfig] = None):
        self.config = config or ServiceConfig.from_env()
        self.is_healthy = True
        self.is_ready = self.config.readiness_flag
        self.request_count = 0
        self._running = True

        # Initialize logger
        self.logger = logging.getLogger(self.config.service_name)
        self.logger.setLevel(getattr(logging, self.config.log_level, logging.INFO))
        self.logger.handlers.clear()

        handler = logging.StreamHandler()
        handler.setFormatter(JsonLogFormatter())
        self.logger.addHandler(handler)

    def health_check(self) -> Dict[str, Any]:
        """Liveness check (indicates process is running)."""
        return {
            "status": "UP" if self.is_healthy else "DOWN",
            "service": self.config.service_name,
            "uptime_requests": self.request_count
        }

    def readiness_check(self) -> Dict[str, Any]:
        """Readiness check (indicates service can accept external customer traffic)."""
        return {
            "ready": self.is_ready and self.is_healthy,
            "environment": self.config.app_env,
        }

    def dispatch_request(self, endpoint: str, handler: Callable[[], Dict[str, Any]]) -> ServiceResponse:
        """
        Process a request with tracing ID, error boundary, and latency metrics.
        """
        if not self._running:
            return ServiceResponse(
                status_code=503,
                body={"error": "Service is shutting down"},
                headers={},
                duration_ms=0.0
            )

        start_time = time.perf_counter()
        request_id = str(uuid.uuid4())
        self.request_count += 1

        try:
            body = handler()
            status_code = 200
        except ValueError as e:
            status_code = 400
            body = {"error": "Bad Request", "detail": str(e)}
        except Exception as e:
            status_code = 500
            body = {"error": "Internal Server Error", "detail": "An unexpected error occurred"}

        duration = (time.perf_counter() - start_time) * 1000

        # Log completion
        self.logger.info(
            f"{endpoint} completed with {status_code}",
            extra={"request_id": request_id}
        )

        headers = {
            "X-Request-ID": request_id,
            "X-Response-Time-Ms": f"{duration:.2f}",
            "Content-Type": "application/json"
        }

        return ServiceResponse(
            status_code=status_code,
            body=body,
            headers=headers,
            duration_ms=round(duration, 2)
        )

    def shutdown(self) -> None:
        """Gracefully transition service to offline mode."""
        self.is_ready = False
        self._running = False
        self.logger.info("Service shutdown completed gracefully.")
