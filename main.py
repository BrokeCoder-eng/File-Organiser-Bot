import logging
from pathlib import Path
from config import WORKSPACE_PATHS, FOLDER_NAMES
from prompt import setup_dir, validate_module_code, get_file_info

logger = logging.getLogger(f"organiser.{__name__}")

def _validate_workspace() -> None:
    for name in FOLDER_NAMES:
        if WORKSPACE_PATHS[name].is_dir():
            logger.info(f"'{WORKSPACE_PATHS[name].name}' exists inside of workspace.")
        else:
            logger.warning(f"'{WORKSPACE_PATHS[name].name}' does not exist inside of workspace.")
            setup_dir(WORKSPACE_PATHS[name], WORKSPACE_PATHS[name].name)
            
_validate_workspace()    
