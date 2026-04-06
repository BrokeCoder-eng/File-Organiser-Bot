import logging
from pathlib import Path
from datetime import datetime

from config import WORKSPACE_PATHS

def setup_logger() -> logging.Logger:
    log_dir = WORKSPACE_PATHS["logs"]
    log_dir.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y_%m_%d_%H%M%S")
    log_file = log_dir / f"run_{timestamp}.log"
    
    logger = logging.getLogger("organiser")
    logger.setLevel(logging.DEBUG)
    
    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(module)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    logger.info(f"Logger initialised, logging to {log_file}")
    
    return logger
