import unittest
from unittest.mock import patch

from retry import retry_with_backoff


class TestRetry(unittest.TestCase):

    @patch("retry.time.sleep")
    def test_retry_success(self, mock_sleep):

        attempts = []

        def operation():
            attempts.append(1)

            if len(attempts) < 3:
                raise ConnectionError("Temporary failure")

            return "Success"

        result = retry_with_backoff(
            operation,
            max_attempts=3,
            base_delay=1
        )

        self.assertEqual(result, "Success")
        self.assertEqual(len(attempts), 3)

        # Check exponential delays
        mock_sleep.assert_any_call(1)
        mock_sleep.assert_any_call(2)

    @patch("retry.time.sleep")
    def test_retry_failure(self, mock_sleep):

        def operation():
            raise ConnectionError("Server unavailable")

        with self.assertRaises(ConnectionError):
            retry_with_backoff(
                operation,
                max_attempts=3,
                base_delay=1
            )

        # Two waits occur before the third/final attempt
        self.assertEqual(mock_sleep.call_count, 2)


if __name__ == "__main__":
    unittest.main()import unittest
from unittest.mock import patch

from retry import retry_with_backoff


class TestRetry(unittest.TestCase):

    @patch("retry.time.sleep")
    def test_retry_success(self, mock_sleep):

        attempts = []

        def operation():
            attempts.append(1)

            if len(attempts) < 3:
                raise ConnectionError("Temporary failure")

            return "Success"

        result = retry_with_backoff(
            operation,
            max_attempts=3,
            base_delay=1
        )

        self.assertEqual(result, "Success")
        self.assertEqual(len(attempts), 3)

        # Check exponential delays
        mock_sleep.assert_any_call(1)
        mock_sleep.assert_any_call(2)

    @patch("retry.time.sleep")
    def test_retry_failure(self, mock_sleep):

        def operation():
            raise ConnectionError("Server unavailable")

        with self.assertRaises(ConnectionError):
            retry_with_backoff(
                operation,
                max_attempts=3,
                base_delay=1
            )

        # Two waits occur before the third/final attempt
        self.assertEqual(mock_sleep.call_count, 2)


if __name__ == "__main__":
    unittest.main()import unittest
from unittest.mock import patch

from retry import retry_with_backoff


class TestRetry(unittest.TestCase):

    @patch("retry.time.sleep")
    def test_retry_success(self, mock_sleep):

        attempts = []

        def operation():
            attempts.append(1)

            if len(attempts) < 3:
                raise ConnectionError("Temporary failure")

            return "Success"

        result = retry_with_backoff(
            operation,
            max_attempts=3,
            base_delay=1
        )

        self.assertEqual(result, "Success")
        self.assertEqual(len(attempts), 3)

        # Check exponential delays
        mock_sleep.assert_any_call(1)
        mock_sleep.assert_any_call(2)

    @patch("retry.time.sleep")
    def test_retry_failure(self, mock_sleep):

        def operation():
            raise ConnectionError("Server unavailable")

        with self.assertRaises(ConnectionError):
            retry_with_backoff(
                operation,
                max_attempts=3,
                base_delay=1
            )

        # Two waits occur before the third/final attempt
        self.assertEqual(mock_sleep.call_count, 2)


if __name__ == "__main__":
    unittest.main()
