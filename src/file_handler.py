
from pathlib import Path


def read_vocabulary(file_path: str) -> list[str]:
    """读取词汇文件，返回清理后的词汇列表。"""
    path = Path(file_path)

    try:
        content = path.read_text(encoding="utf-8")
    except FileNotFoundError as e:
        raise FileNotFoundError(f"词汇文件不存在: {path}") from e

    lines = content.splitlines()

    return [line.strip() for line in lines if line.strip()]
