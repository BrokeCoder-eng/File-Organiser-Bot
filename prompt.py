import logging
from pathlib import Path
from config import MODULE_CODE_PATTERN, FILE_TYPE, FILE_CATEGORIES

logger = logging.getLogger(f"organiser.{__name__}")
_session_cache = {}

def setup_dir(dir_path: Path, dir_name: str) -> None:
    print(f"Do you want to create directory for '{dir_name}' (Y/N):")
    user_input = input()
    while(user_input.lower() not in ["y", "n"]):
        logger.warning(f"Incorrect user input '{user_input}'")
        print("Invalid input. Please enter either Y/N:")
        user_input = input()
    if user_input.lower() == "y":
        try:
            dir_path.mkdir(exist_ok=True, parents=True)
            logger.info(f"'{dir_name}' was successfully created in '{dir_path}'.")
        except OSError:
            logger.error(f"Was not able to create folder in '{dir_path}'.")  
    else:
        logger.info(f"Directory for '{dir_name}' will not be created.")

def validate_module_code(module_codes_list: list, module_code: str) -> str | None:
    if module_code not in module_codes_list:
        logger.warning(f"Module code '{module_code}' does not exist.")
        print(f"Module code '{module_code}' does not exist. Would you like to add it (Y/N):")
        user_input = input()
        while(user_input.lower() not in ["y", "n"]):
            logger.warning(f"Incorrect user input '{user_input}'")
            print("Invalid input. Please enter either Y/N:")
            user_input = input()
        if user_input.lower() == "y":
            logger.info(f"Module code '{module_code}' confirmed and will be saved.")
            return module_code
        else:
            logger.info(f"Module is not valid, and will not be saved.")
            return None
    else:
        logger.info(f"Module code '{module_code}' already exists.")
        return module_code       

def _build_result(file_name: str, category: str) -> dict:
    module_code = MODULE_CODE_PATTERN.search(file_name)
    if module_code is not None:
        module_code = module_code.group()
    else:
        module_code = None
    return {"filename": file_name, "category": category, "module_code": module_code}

def get_file_info(file_name: str) -> dict:
    file_extension = Path(file_name).suffix
    
    if file_extension in _session_cache:
        logger.info(f"Dictionary fetched from session cache. {_session_cache}")
        return _build_result(file_name, _session_cache[file_extension])
    
    if file_extension in FILE_TYPE:
        logger.info(f"File validated. Dictionary generated for '{file_name}'")
        return _build_result(file_name, FILE_TYPE[file_extension])
    else:
        print(f"Unknown file type '{file_extension}' detected. Under what category does this file fall under:")
        user_input_category = input()
        while user_input_category.lower() not in FILE_CATEGORIES:
            logger.warning(f"'{user_input_category}' is not a valid category.")
            print("Invalid category. Please re-enter category:")
            user_input_category = input()
        logger.info(f"File category validated. Dictionary generated for '{file_name}'")
        _session_cache[file_extension] = user_input_category.lower()
        return _build_result(file_name, user_input_category.lower())
