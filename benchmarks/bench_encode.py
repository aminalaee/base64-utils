import io
import base64

import base64_utils


ITERATIONS = 1_000

SMALL_DATA = b"t" * 1  # 1 Byte
MEDIUM_DATA = b"t" * 1_000  # 1 KB
LARGE_DATA = b"t" * 1_000_000  # 1 MB


def stdlib_base64encode_small() -> None:
    for _ in range(ITERATIONS):
        base64.b64encode(SMALL_DATA)


def base64_utils_base64encode_small() -> None:
    for _ in range(ITERATIONS):
        base64_utils.b64encode(SMALL_DATA)


def stdlib_base64encode_medium() -> None:
    for _ in range(ITERATIONS):
        base64.b64encode(MEDIUM_DATA)


def base64_utils_base64encode_medium() -> None:
    for _ in range(ITERATIONS):
        base64_utils.b64encode(MEDIUM_DATA)


def stdlib_base64encode_large() -> None:
    for _ in range(ITERATIONS):
        base64.b64encode(LARGE_DATA)


def base64_utils_base64encode_large() -> None:
    for _ in range(ITERATIONS):
        base64_utils.b64encode(LARGE_DATA)


__benchmarks__ = [
    (
        stdlib_base64encode_small,
        base64_utils_base64encode_small,
        "b64encode with 1 Byte",
    ),
    (
        stdlib_base64encode_medium,
        base64_utils_base64encode_medium,
        "b64encode with 1 KB",
    ),
    (
        stdlib_base64encode_large,
        base64_utils_base64encode_large,
        "b64encode with 1 MB",
    ),
]
