import json
import logging
from config import WORKSPACE_PATHS

logger = logging.getLogger(f"organiser.{__name__}")

def load_module_codes() -> list:
    try:
        with open(WORKSPACE_PATHS["module_codes"], "r") as f:
            module_codes = json.load(f)
            logger.info(f"Loaded {len(module_codes)} from '{WORKSPACE_PATHS['module_codes']}'")
            return module_codes
    except FileNotFoundError:
        logger.warning(f"No module codes file found at '{WORKSPACE_PATHS['module_codes']}'")
        return []
    except json.JSONDecodeError:
        logger.error(f"JSON file corrupted at '{WORKSPACE_PATHS['module_codes']}'")
        return []

def save_module_codes(module_codes: list) -> None:
    try:
        WORKSPACE_PATHS["module_codes"].parent.mkdir(parents=True, exist_ok=True)
        with open(WORKSPACE_PATHS["module_codes"], "w") as f:
            json.dump(module_codes, f, indent=4)
            logger.info(f"Saved {len(module_codes)} module codes to '{WORKSPACE_PATHS[module_codes]}'")
    except OSError as e:
        logger.error(f"Failed to save module codes: {e}")
