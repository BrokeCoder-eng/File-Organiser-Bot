import logging
import shutil
from pathlib import Path

logger = logging.getLogger(f"organiser.{__name__}")

def move_file(source: Path, destination: Path) -> bool:
    try:
        shutil.move(source, destination)
        logger.info(f"Successfully moved file to '{destination}'")
        return True
    except (shutil.Error(), OSError):
        logger.error(f"Failed to move file to '{destination}'")
        return False