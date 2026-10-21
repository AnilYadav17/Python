"""
03_real_world_use_case.py
Real-world scenario: Production-grade API client retry & latency decorator.
Demonstrates:
- Higher-order functions & parameterized decorators
- Preserving function metadata with functools.wraps
- Implementing exponential backoff on simulated intermittent failures
- Logging execution latency
"""

import time
import functools

def retry_with_backoff(max_retries=3, initial_delay=0.05, backoff_factor=2.0, exceptions=(Exception,)):
    """
    Parameterized decorator that retries a function with exponential backoff
    when any exception in `exceptions` is raised.
    """
    def decorator(func):
        # functools.wraps preserves original func's __name__, __doc__, and __module__
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            delay = initial_delay
            last_exception = None

            for attempt in range(1, max_retries + 1):
                start_time = time.perf_counter()
                try:
                    print(f"[{func.__name__}] Attempt {attempt}/{max_retries} executing...")
                    result = func(*args, **kwargs)
                    elapsed = time.perf_counter() - start_time
                    print(f"[{func.__name__}] Succeeded on attempt {attempt} in {elapsed * 1000:.2f}ms")
                    return result
                except exceptions as exc:
                    elapsed = time.perf_counter() - start_time
                    last_exception = exc
                    print(f"[{func.__name__}] Failed attempt {attempt} ({exc}) in {elapsed * 1000:.2f}ms")

                    if attempt < max_retries:
                        time.sleep(delay)
                        delay *= backoff_factor
                    else:
                        print(f"[{func.__name__}] All {max_retries} attempts exhausted!")

            # Re-raise the last caught exception after exhausting all retries
            raise last_exception

        return wrapper
    return decorator


# Simulated flaky network dependency
attempts_counter = 0

@retry_with_backoff(max_retries=3, initial_delay=0.02, backoff_factor=2.0, exceptions=(ConnectionError,))
def fetch_remote_user_profile(user_id):
    """Fetches user profile data from external microservice."""
    global attempts_counter
    attempts_counter += 1

    # Simulate intermittent network failures on first two attempts
    if attempts_counter < 3:
        raise ConnectionError(f"HTTP 503 Service Unavailable (attempt {attempts_counter})")

    return {"user_id": user_id, "name": "Sarah Connor", "status": "verified"}


def main():
    print(f"Decorator inspection: func name is '{fetch_remote_user_profile.__name__}'")
    print(f"Docstring: '{fetch_remote_user_profile.__doc__}'")

    print("\nExecuting resilient remote call:")
    profile = fetch_remote_user_profile(user_id=1042)
    print(f"\nFinal Result: {profile}")

if __name__ == "__main__":
    main()
