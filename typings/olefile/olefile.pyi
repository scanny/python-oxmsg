from __future__ import annotations

from typing import IO, Any

STGTY_STORAGE: int
STGTY_STREAM: int

def isOleFile(filename: str | IO[bytes] | None = None, data: bytes | None = None) -> bool: ...

class OleFileIO:
    root: OleDirectoryEntry
    def __init__(
        self,
        filename: str | IO[bytes] | bytes,
        raise_defects: int = 40,
        write_mode: bool = False,
        debug: bool = False,
        path_encoding: str | None = None,
    ) -> None: ...
    def __enter__(self) -> OleFileIO: ...
    def __exit__(self, *args: Any) -> None: ...
    def close(self) -> None: ...
    def listdir(self, streams: bool = True, storages: bool = False) -> list[list[str]]: ...
    def openstream(self, filename: str) -> IO[bytes]: ...

class OleDirectoryEntry:
    entry_type: int
    kids: list[OleDirectoryEntry]
    name: str
    root: OleDirectoryEntry
