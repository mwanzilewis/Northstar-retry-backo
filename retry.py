import time


def retry_with_backoff(operation, max_attempts=3, base_delay=1):
    """
    Retry an operation using exponential backoff.

    Delays:
        Attempt 1 fails -> wait 1 second
        Attempt 2 fails -> wait 2 seconds
        Attempt 3 fails -> stop and raise the error
    """

    for attempt in range(max_attempts):
        try:
            return operation()

        except Exception as error:
            # If this was the final attempt, stop retrying
            if attempt == max_attempts - 1:
                raise error

            # Exponential backoff: 1, 2, 4, ...
            delay = base_delay * (2 ** attempt)

            print(
                f"Attempt {attempt + 1} failed. "
                f"Retrying in {delay} seconds..."
            )

            time.sleep(delay)


# Example failing operation
def warehouse_request():
    print("Contacting warehouse server...")
    raise ConnectionError("Warehouse server is temporarily unavailable")


if __name__ == "__main__":
    try:
        retry_with_backoff(
            warehouse_request,
            max_attempts=3,
            base_delay=1
        )
    except Exception as error:
        print(f"Request failed after all retries: {error}")
