import base64

import base64_utils

SMALL_DATA = b"t" * 1_000  # 1 KB
MEDIUM_DATA = b"t" * 100_000  # 100 KB
LARGE_DATA = b"t" * 1_000_000  # 1 MB

SMALL_DATA_ENCODED = base64.b64encode(SMALL_DATA)
MEDIUM_DATA_ENCODED = base64.b64encode(MEDIUM_DATA)
LARGE_DATA_ENCODED = base64.b64encode(LARGE_DATA)

MEDIUM_DATA_ENCODEBYTES = base64.encodebytes(MEDIUM_DATA)
LARGE_DATA_ENCODEBYTES = base64.encodebytes(LARGE_DATA)


def stdlib_b64encode_1kb() -> None:
    base64.b64encode(SMALL_DATA)


def base64_utils_b64encode_1kb() -> None:
    base64_utils.b64encode(SMALL_DATA)


def stdlib_b64encode_100kb() -> None:
    base64.b64encode(MEDIUM_DATA)


def base64_utils_b64encode_100kb() -> None:
    base64_utils.b64encode(MEDIUM_DATA)


def stdlib_b64encode_1mb() -> None:
    base64.b64encode(LARGE_DATA)


def base64_utils_b64encode_1mb() -> None:
    base64_utils.b64encode(LARGE_DATA)


def stdlib_b64encode_altchars_100kb() -> None:
    base64.b64encode(MEDIUM_DATA, altchars=b"-_")


def base64_utils_b64encode_altchars_100kb() -> None:
    base64_utils.b64encode(MEDIUM_DATA, altchars=b"-_")


def stdlib_b64decode_1mb() -> None:
    base64.b64decode(LARGE_DATA_ENCODED)


def base64_utils_b64decode_1mb() -> None:
    base64_utils.b64decode(LARGE_DATA_ENCODED)


def stdlib_encodebytes_100kb() -> None:
    base64.encodebytes(MEDIUM_DATA)


def base64_utils_encodebytes_100kb() -> None:
    base64_utils.encodebytes(MEDIUM_DATA)


def stdlib_encodebytes_1mb() -> None:
    base64.encodebytes(LARGE_DATA)


def base64_utils_encodebytes_1mb() -> None:
    base64_utils.encodebytes(LARGE_DATA)


def stdlib_decodebytes_100kb() -> None:
    base64.decodebytes(MEDIUM_DATA_ENCODEBYTES)


def base64_utils_decodebytes_100kb() -> None:
    base64_utils.decodebytes(MEDIUM_DATA_ENCODEBYTES)


def stdlib_decodebytes_1mb() -> None:
    base64.decodebytes(LARGE_DATA_ENCODEBYTES)


def base64_utils_decodebytes_1mb() -> None:
    base64_utils.decodebytes(LARGE_DATA_ENCODEBYTES)


__benchmarks__ = [
    ("b64encode (1 KB)", [stdlib_b64encode_1kb, base64_utils_b64encode_1kb]),
    ("b64encode (100 KB)", [stdlib_b64encode_100kb, base64_utils_b64encode_100kb]),
    ("b64encode (1 MB)", [stdlib_b64encode_1mb, base64_utils_b64encode_1mb]),
    ("b64encode altchars (100 KB)", [stdlib_b64encode_altchars_100kb, base64_utils_b64encode_altchars_100kb]),
    ("b64decode (1 MB)", [stdlib_b64decode_1mb, base64_utils_b64decode_1mb]),
    ("encodebytes (100 KB)", [stdlib_encodebytes_100kb, base64_utils_encodebytes_100kb]),
    ("encodebytes (1 MB)", [stdlib_encodebytes_1mb, base64_utils_encodebytes_1mb]),
    ("decodebytes (100 KB)", [stdlib_decodebytes_100kb, base64_utils_decodebytes_100kb]),
    ("decodebytes (1 MB)", [stdlib_decodebytes_1mb, base64_utils_decodebytes_1mb]),
]
