import base64

import base64_utils


ITERATIONS = 1_000

SMALL_DATA = b"t" * 1_000  # 1 KB
MEDIUM_DATA = b"t" * 100_000  # 100 KB
LARGE_DATA = b"t" * 1_000_000  # 1 MB

SMALL_DATA_ENCODED = base64.b64encode(SMALL_DATA)
MEDIUM_DATA_ENCODED = base64.b64encode(MEDIUM_DATA)
LARGE_DATA_ENCODED = base64.b64encode(LARGE_DATA)


def stdlib_b64encode(data, altchars=None) -> None:
    for _ in range(ITERATIONS):
        base64.b64encode(data, altchars=altchars)


def base64_utils_b64encode(data, altchars=None) -> None:
    for _ in range(ITERATIONS):
        base64_utils.b64encode(data, altchars=altchars)

def stdlib_b64decode(data, altchars=None, validate=False) -> None:
    for _ in range(ITERATIONS):
        base64.b64decode(data, altchars=altchars, validate=validate)


def base64_utils_b64decode(data, altchars=None, validate=False) -> None:
    for _ in range(ITERATIONS):
        base64_utils.b64decode(data, altchars=altchars, validate=validate)


__benchmarks__ = [
    (
        lambda: stdlib_b64encode(SMALL_DATA),
        lambda: base64_utils_b64encode(SMALL_DATA),
        "b64encode (1 KB data)",
    ),
    (
        lambda: stdlib_b64encode(MEDIUM_DATA),
        lambda: base64_utils_b64encode(MEDIUM_DATA),
        "b64encode (100 KB data)",
    ),
    (
        lambda: stdlib_b64encode(LARGE_DATA),
        lambda: base64_utils_b64encode(LARGE_DATA),
        "b64encode (1 MB data)",
    ),
    (
        lambda: stdlib_b64encode(MEDIUM_DATA, altchars=b"-_"),
        lambda: base64_utils_b64encode(MEDIUM_DATA, altchars=b"-_"),
        "b64encode (altchars + 100 KB data)",
    ),
    (
        lambda: stdlib_b64decode(MEDIUM_DATA_ENCODED),
        lambda: base64_utils_b64decode(MEDIUM_DATA_ENCODED),
        "b64decode (100 KB data)",
    )
]
