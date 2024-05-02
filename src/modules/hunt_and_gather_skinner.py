import itertools
import logging
import os


def get_file_path(file_name):
    """
    Get the path of the specified file.

    Args:
        file_name (str): The name of the file.

    Returns:
        str: The path of the specified file.

    Raises:
        ValueError: If the file name is not a string.
    """
    if not isinstance(file_name, str):
        raise ValueError("File name must be a string")


def get_code_at_line(file_path, line):
    """
    Get the code at the specified line in the specified file.

    Args:
        file_path (str): The path of the file to get the code from.
        line (int): The line number to get the code from.

    Returns:
        str: The code at the specified line.

    Raises:
        ValueError: If the line is not a positive integer.
        FileNotFoundError: If the specified file does not exist.
        PermissionError: If there is a permission error while accessing the file.
    """
    if not isinstance(file_path, str):
        raise ValueError("File path must be a string")
    if not os.path.isfile(file_path):
        raise FileNotFoundError("File does not exist")

    if not isinstance(line, int) or line <= 0:
        raise ValueError("Line must be a positive integer")

    try:
        with open(file_path, 'r') as file:
            return next(itertools.islice(file, line - 1, line))
    except (FileNotFoundError, PermissionError) as e:
        logging.exception(f"Error occurred while getting code at line: {e}")
        raise


class HunterXSkinner:
    pass

