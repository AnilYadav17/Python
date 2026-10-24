# Project 06: Asynchronous Resilient API Client

A high-concurrency, failure-resilient API client built on `asyncio` showcasing enterprise-grade stability patterns.

---

## Architectural Highlights
- **Rate-Limiting Throttle**: Uses `asyncio.Semaphore` to cap active outbound HTTP connections.
- **Exponential Backoff with Jitter**: Automatically retries 5xx server errors and network timeouts with increasing backoff delays ($delay = base \times 2^{attempt}$).
- **Timeout Guarantees**: Strict per-request cancellation timeouts preventing hung threads.
- **Asynchronous Context Manager**: Safely tears down client connections via `async with AsyncApiClient():`.

---

## Testing
Run unit tests:
```bash
python -m unittest test_client.py
```
