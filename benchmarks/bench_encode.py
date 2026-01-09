import base64

import base64_utils


ITERATIONS = 1_000
SMALL_DATA = b"t" * 1_000  # 1 KB
MEDIUM_DATA = b"t" * 100_000  # 100 KB
LARGE_DATA = b"t" * 1_000_000  # 1 MB


def stdlib_base64encode(data, altchars=None) -> None:
    for _ in range(ITERATIONS):
        base64.b64encode(data, altchars=altchars)


def base64_utils_base64encode(data, altchars=None) -> None:
    for _ in range(ITERATIONS):
        base64_utils.b64encode(data, altchars=altchars)


__benchmarks__ = [
    (
        lambda: stdlib_base64encode(SMALL_DATA),
        lambda: base64_utils_base64encode(SMALL_DATA),
        "b64encode (1 KB data)",
    ),
    (
        lambda: stdlib_base64encode(MEDIUM_DATA),
        lambda: base64_utils_base64encode(MEDIUM_DATA),
        "b64encode (100 KB data)",
    ),
    (
        lambda: stdlib_base64encode(LARGE_DATA),
        lambda: base64_utils_base64encode(LARGE_DATA),
        "b64encode (1 MB data)",
    ),
    (
        lambda: stdlib_base64encode(MEDIUM_DATA, altchars=b"-_"),
        lambda: base64_utils_base64encode(MEDIUM_DATA, altchars=b"-_"),
        "b64encode (altchars + 100 KB data)",
    ),
]
