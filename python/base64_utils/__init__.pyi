from _typeshed import ReadableBuffer

__version__: str

__all__ = [
    "b64encode",
    "b64decode",
    "standard_b64encode",
    "urlsafe_b64encode",
]

def b64encode(s: ReadableBuffer, altchars: ReadableBuffer | None = None) -> bytes: ...
def b64decode(
    s: str | ReadableBuffer,
    altchars: str | ReadableBuffer | None = None,
    validate: bool = False,
) -> bytes: ...
def standard_b64encode(s: ReadableBuffer) -> bytes: ...
def urlsafe_b64encode(s: ReadableBuffer) -> bytes: ...
