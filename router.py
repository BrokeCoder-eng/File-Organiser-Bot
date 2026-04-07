import logging
from pathlib import Path
from config import WORKSPACE_PATHS, CODING_LANGUAGE_FOLDERS

logger = logging.getLogger(f"organiser.{__name__}")

def get_folder_route(file_info: dict, route=WORKSPACE_PATHS["root"]) -> Path:
    temp_file_info = file_info.copy()
    if temp_file_info["module_code"] is not None:
        route = route / WORKSPACE_PATHS["uni_work"].name / temp_file_info["module_code"]
        temp_file_info["module_code"] = None
        logger.info(f"Building route '{route}'.")
        return get_folder_route(temp_file_info, route)
    else:
        match temp_file_info["category"]:
            case "image":
                route = route / WORKSPACE_PATHS["images"].name
                temp_file_info["category"] = None
                logger.info(f"Building route '{route}'.")
                return get_folder_route(temp_file_info, route)
            case "code":
                route = route / WORKSPACE_PATHS["coding"].name
                if Path(temp_file_info["filename"]).suffix in CODING_LANGUAGE_FOLDERS:
                    route = route / CODING_LANGUAGE_FOLDERS[Path(temp_file_info["filename"]).suffix]
                temp_file_info["category"] = None
                logger.info(f"Building route '{route}'.")
                return get_folder_route(temp_file_info, route)
            case "document":
                route = route / WORKSPACE_PATHS["documents"].name
                temp_file_info["category"] = None
                logger.info(f"Building route '{route}'.")
                return get_folder_route(temp_file_info, route)
            case "misc":
                route = route / WORKSPACE_PATHS["misc"].name
                temp_file_info["category"] = None
                logger.info(f"Building route '{route}'.")
                return get_folder_route(temp_file_info, route)
            case _:
                logger.info(f"Final route '{route}'.")
                return route