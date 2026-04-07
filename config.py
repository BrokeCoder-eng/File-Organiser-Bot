import re
from pathlib import Path

MODULE_CODE_PATTERN_STR = r"[A-Z]{5}\d{3}"
MODULE_CODE_PATTERN = re.compile(MODULE_CODE_PATTERN_STR)

WORKSPACE_ROOT_FOLDER_NAME = "Work"

WORKSPACE_PATHS = {}
_root = Path.home() / "Documents" / "Python" / Path(WORKSPACE_ROOT_FOLDER_NAME)

WORKSPACE_PATHS = {
    "root": _root,
    "dump": _root / "Dump",
    "coding": _root / "Coding",
    "images": _root / "Images",
    "documents": _root / "Documents",
    "uni_work": _root / "University Work",
    "misc": _root / "Misc",
    "module_codes": _root / "data" / "module_codes.json",
    "logs": _root / "logs"
}

FOLDER_NAMES = {
    "coding",
    "documents",
    "images",
    "uni_work",
    "misc"   
}

FILE_CATEGORIES = {
    "image",
    "code",
    "document",
    "misc"
}

FILE_TYPE = {
    ".jpg": "image",
    ".jpeg": "image",
    ".png": "image",
    ".gif": "image",
    ".webp": "image",
    ".avif": "image",
    ".bmp": "image",
    ".tiff": "image",
    ".py": "code",
    ".cpp": "code",
    ".java": "code",
    ".js": "code",
    ".ts": "code",
    ".html": "code",
    ".css": "code",
    ".pdf": "document",
    ".doc": "document",
    ".docx": "document",
    ".xls": "document",
    ".xlsx": "document",
    ".ppt": "document",
    ".pptx": "document"
}

CODING_LANGUAGE_FOLDERS = {
    ".py": "Python",
    ".cpp": "C++",
    ".java": "Java",
    ".js": "JavaScript",
    ".ts": "TypeScript",
    ".html": "Web",
    ".css": "Web",
}
