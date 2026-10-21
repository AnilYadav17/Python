"""
01_basic_usage.py
Demonstrates foundational function mechanics:
- Function definitions and return tuples
- Positional, keyword, positional-only (/), and keyword-only (*) arguments
- Variadic arguments: *args and **kwargs
"""

# 1. Positional-only (before /) and Keyword-only (after *) parameters
def configure_server(host, port, /, protocol="https", *, timeout=30, max_retries=3):
    """
    host, port: positional-only (cannot be called with host='...')
    protocol: standard positional or keyword
    timeout, max_retries: keyword-only (must be called with timeout=..., max_retries=...)
    """
    return {
        "url": f"{protocol}://{host}:{port}",
        "timeout": timeout,
        "retries": max_retries
    }


# 2. Variadic parameters: *args (tuple) and **kwargs (dict)
def calculate_metrics(title, *values, **tags):
    """
    title: mandatory positional argument
    *values: packs any number of numbers into a tuple
    **tags: packs any keyword metadata into a dictionary
    """
    if not values:
        return title, 0.0, tags  # Returns a tuple of 3 items

    total = sum(values)
    mean = total / len(values)
    return title, mean, tags


def main():
    print("--- 1. Positional-only and Keyword-only Parameters ---")
    # Valid invocation: host and port positional; timeout keyword-only
    config = configure_server("127.0.0.1", 8080, "http", timeout=15, max_retries=5)
    print(f"Server Config: {config}")

    print("\n--- 2. Variadic Arguments (*args, **kwargs) ---")
    # Unpack multiple values into *values, and keyword attributes into **tags
    name, avg_score, metadata = calculate_metrics(
        "Performance_Audit",
        88.5, 92.0, 79.5, 95.0,
        env="production",
        region="us-east-1"
    )
    print(f"Metric: {name}")
    print(f"Calculated Mean: {avg_score:.2f}")
    print(f"Metadata Tags: {metadata}")

    # Unpacking iterable into *args and dict into **kwargs at call site
    raw_scores = (100, 95, 98)
    extra_info = {"department": "Engineering", "auditor": "SecurityTeam"}
    _, unpacked_mean, _ = calculate_metrics("Unpacked_Audit", *raw_scores, **extra_info)
    print(f"Unpacked Call Mean: {unpacked_mean:.2f}")

if __name__ == "__main__":
    main()
