"""
Automated Asynchronous Tests for AsyncApiClient (Project 06)
"""

import asyncio
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))
from client import ApiException, ApiResponse, AsyncApiClient, MaxRetriesExceeded, RequestTimeout


class TestAsyncApiClient(unittest.IsolatedAsyncioTestCase):
    async def test_successful_request(self):
        client = AsyncApiClient(base_url="https://api.test")
        resp = await client.get("/users")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data["url"], "https://api.test/users")
        self.assertEqual(resp.attempt_count, 1)

    async def test_exponential_backoff_retry_recovery(self):
        # Transport fails twice with 500 error, succeeds on 3rd attempt
        call_count = 0

        async def flappy_transport(method: str, url: str) -> ApiResponse:
            nonlocal call_count
            call_count += 1
            if call_count < 3:
                return ApiResponse(status_code=503, data={"error": "service unavailable"}, attempt_count=call_count)
            return ApiResponse(status_code=200, data={"status": "recovered"}, attempt_count=call_count)

        client = AsyncApiClient(
            base_url="https://api.test",
            max_retries=3,
            backoff_factor=0.01,
            transport_func=flappy_transport
        )

        resp = await client.get("/checkout")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.attempt_count, 3)
        self.assertEqual(call_count, 3)

    async def test_max_retries_exceeded_raises_error(self):
        # Transport always returns 500
        async def always_failing(method: str, url: str) -> ApiResponse:
            return ApiResponse(status_code=500, data={"error": "fatal"}, attempt_count=1)

        client = AsyncApiClient(
            max_retries=2,
            backoff_factor=0.01,
            transport_func=always_failing
        )

        with self.assertRaises(MaxRetriesExceeded):
            await client.get("/broken")

    async def test_timeout_enforcement(self):
        # Transport hangs longer than timeout
        async def hanging_transport(method: str, url: str) -> ApiResponse:
            await asyncio.sleep(0.5)
            return ApiResponse(status_code=200, data={}, attempt_count=1)

        client = AsyncApiClient(
            max_retries=1,
            default_timeout_seconds=0.05,
            transport_func=hanging_transport
        )

        with self.assertRaises(MaxRetriesExceeded):
            await client.get("/slow")

    async def test_async_context_manager_close(self):
        async with AsyncApiClient() as client:
            resp = await client.get("/ping")
            self.assertEqual(resp.status_code, 200)

        self.assertTrue(client._closed)
        with self.assertRaises(RuntimeError):
            await client.get("/ping")


if __name__ == "__main__":
    unittest.main()
