import base64

import base64_utils

LARGE_DATA = b"t" * 1_000_000  # 1 MB
LARGE_DATA_ENCODED = base64.b64encode(LARGE_DATA)
LARGE_DATA_ENCODEBYTES = base64.encodebytes(LARGE_DATA)


def stdlib_b64encode_1mb() -> None:
    base64.b64encode(LARGE_DATA)


def base64_utils_b64encode_1mb() -> None:
    base64_utils.b64encode(LARGE_DATA)


def stdlib_b64decode_1mb() -> None:
    base64.b64decode(LARGE_DATA_ENCODED)


def base64_utils_b64decode_1mb() -> None:
    base64_utils.b64decode(LARGE_DATA_ENCODED)


def stdlib_encodebytes_1mb() -> None:
    base64.encodebytes(LARGE_DATA)


def base64_utils_encodebytes_1mb() -> None:
    base64_utils.encodebytes(LARGE_DATA)


def stdlib_decodebytes_1mb() -> None:
    base64.decodebytes(LARGE_DATA_ENCODEBYTES)


def base64_utils_decodebytes_1mb() -> None:
    base64_utils.decodebytes(LARGE_DATA_ENCODEBYTES)


__benchmarks__ = [
    ("b64encode (1 MB)", [stdlib_b64encode_1mb, base64_utils_b64encode_1mb]),
    ("b64decode (1 MB)", [stdlib_b64decode_1mb, base64_utils_b64decode_1mb]),
    ("encodebytes (1 MB)", [stdlib_encodebytes_1mb, base64_utils_encodebytes_1mb]),
    ("decodebytes (1 MB)", [stdlib_decodebytes_1mb, base64_utils_decodebytes_1mb]),
]
