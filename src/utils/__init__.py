from pathlib import Path
from typing import Callable, IO, TextIO


def atomic_write(
        path: Path,
        write: Callable[[IO | TextIO], None],
        is_binary: bool = False
):
    path.parent.mkdir(parents=True, exist_ok=True)
    temp_path = path.with_suffix('.temp' + path.suffix)
    mode = 'wb' if is_binary else 'w'
    with temp_path.open(mode) as f:
        write(f)
    temp_path.rename(path)
