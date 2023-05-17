from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Empty(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class Time(_message.Message):
    __slots__ = ["time"]
    TIME_FIELD_NUMBER: _ClassVar[int]
    time: str
    def __init__(self, time: _Optional[str] = ...) -> None: ...

class TimeZone(_message.Message):
    __slots__ = ["name", "offset"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    name: str
    offset: float
    def __init__(self, name: _Optional[str] = ..., offset: _Optional[float] = ...) -> None: ...
