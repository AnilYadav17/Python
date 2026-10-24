# Project 09: Production-Style Enterprise Python Service

A production-grade Python service template implementing Twelve-Factor App principles, structured JSON logging, health probing, and error isolation.

---

## Key Features
- **12-Factor Configuration**: Environment-first configuration with type-coerced sensible defaults.
- **Structured JSON Logging**: Every log event includes timestamps, severity, module location, and contextual `request_id` for distributed tracing.
- **Kubernetes-Ready Probes**:
  - `/healthz`: Liveness probe ensuring the process is running.
  - `/readyz`: Readiness probe controlling ingress traffic acceptance.
- **Middleware Error Isolation**: Normalizes unhandled exceptions into RFC 7807 problem details without leaking internal stack traces.
- **Graceful Shutdown**: Drains in-flight requests and returns 503 during teardown.

---

## Testing
Run unit tests:
```bash
python -m unittest test_service.py
```
