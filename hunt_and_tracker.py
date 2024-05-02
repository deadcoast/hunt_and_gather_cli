import itertools
import logging
import os
from typing import re

from black import List, Any

from main import get_file_path


class HunterXTracker:
    def __init__(self):
        pass

    @staticmethod
    def get_code_at_line(file_path, line):
        """
        Get the code at the specified line in the given file.

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
            with open(file_path, "r") as f:
                lines = f.readlines()
                if line > len(lines):
                    raise ValueError("Line number out of range")
                return lines[line - 1]
        except (FileNotFoundError, PermissionError) as e:
            logging.exception(f"Error occurred while getting code at line: {e}")
            raise e

    def track(self, dir: str) -> List[str]:
        """
        Track code patterns in a directory.

        Args:
            dir (str): The directory to track code patterns in.

        Returns:
            List[str]: A list of tracked code patterns.
        """
        logging.info(f"Tracking code patterns in {dir}")
        if not isinstance(dir, str) or not os.path.isdir(dir):
            raise ValueError("Directory path must be a string or a valid directory path")
        try:
            num_files_processed = 0
            for file_name in os.listdir(dir):
                file_path = os.path.join(dir, file_name)
                if os.path.isfile(file_path):
                    # Process the file
                    # ...
                    num_files_processed += 1
                    logging.info(f"Processed {num_files_processed} files")
            logging.info(f"Code tracking completed in {dir}")
            return []
        except ValueError as e:
            logging.exception(f"Error occurred while tracking code: {e}")
            raise

    def snare(self, pattern: str) -> str | list[Any]:
        """
        Snare code snippets using a regular expression pattern.

        Args:
            pattern (str): The regular expression pattern to snare.

        Returns:
            List[str]: A list of snared code snippets.

        Raises:
            ValueError: If the pattern is not a string or if it is an invalid regex pattern.
        """
        try:
            if not isinstance(pattern, str):
                raise ValueError("Pattern must be a string")
            try:
                compiled_pattern = re.compile(pattern)
            except re.error as e:
                raise ValueError("Invalid regex pattern") from e
            logging.info(f"Snaring code snippets with pattern: {pattern}")
            if result := compiled_pattern.search("some text"):
                # Perform snaring action or return meaningful value
                # ...
                return result.group()
            else:
                return []
        except (re.error, ValueError) as e:
            logging.error(f"Error occurred while snaring code snippets: {e}")

    def trap(self, lines):
        trapped_code = []
        try:
            return self.trap_error_handler(lines, trapped_code)
        except Exception as e:
            logging.error(f"Error occurred while trapping code: {e}")
            return False

    def trap_error_handler(self, lines, trapped_code, file_path=get_file_path("file_name.txt")):
        if not isinstance(lines, str):
            raise ValueError("Lines must be a string")
        line_range = lines.split("-")
        if len(line_range) != 2:
            raise ValueError("Invalid line range")
        start_line = int(line_range[0])
        end_line = int(line_range[1])
        if start_line > end_line:
            raise ValueError("Start line cannot be greater than end line")
        for line in range(start_line, end_line + 1):
            trapped_code.append(self.get_code_at_line(
                file_path, line))
        logging.info(f"Trapping code in lines {lines}")
        return trapped_code

    def lure(self, string: str) -> List[str]:
        """
        Lure code snippets containing a specific string.

        Args:
            string (str): The string to use for luring.

        Returns:
            List[str]: A list of code snippets containing the specified string.
        """
        if string is None or not string:
            raise ValueError("String cannot be empty or null")
        try:
            logging.info(f"Luring code with string: {string}")
            # Implement code luring functionality here
            return []
        except Exception as e:
            logging.error(f"Error occurred while luring code: {e}")


def get_code_at_line(file_path, line):
    """
    Get the code at the specified line in the given file.

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
