import glob
import itertools
import logging
import os
import re
from black import List, Any
import isdigit as isdigit
from main import get_file_path


class HunterXTracker:
    def __init__(self):

        self.file_path = None
        self.captured_code = None

    def trap(self, lines):
        trapped_code = []
        if not isinstance(lines, str):
            raise ValueError("Lines must be a string")
        line_range = lines.split("-")
        if len(line_range) != 2:
            raise ValueError("Invalid line range")
        start_line = line_range[0]
        end_line = line_range[1]
        is_start_digit = start_line.isdigit()
        is_end_digit = end_line.isdigit()
        if (not is_start_digit or not is_end_digit or end_line == "end") and (
                not is_start_digit or not is_end_digit
        ):
            raise ValueError("Invalid line range")
        if int(start_line) > int(end_line):
            raise ValueError("Start line must be less than or equal to end line")
        if start_line == '0':
            raise ValueError("Start line must be greater than 0")
        if end_line == '0':
            raise ValueError("End line must be greater than 0")
        if start_line == end_line:
            trapped_code.append(self.get_code_at_line(self.file_path, int(start_line)))
        else:
            with open(self.file_path, 'r') as file:
                lines = file.readlines()
                trapped_code.extend(lines[int(start_line) - 1:int(end_line)])
        return trapped_code

    @staticmethod
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
        return os.path.abspath(os.path.join(
            os.path.dirname(__file__),
            os.path.join("hunt_and_tracker",
                         "path",
                         "to",
                         "file"
                         )))

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
                for i, file_line in enumerate(f, start=1):
                    if i == line:
                        return file_line
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
            for root, dirs, files in os.walk(dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    # Process the file
                    # ...
                    num_files_processed += 1
                    logging.info(f"Processed {num_files_processed} files")
            logging.info(f"Code tracking completed in {dir}")
            return []
        except ValueError as e:
            logging.exception(f"Error occurred while tracking code: {e}")
            raise

    def snare(self, pattern: str, text: str) -> str | list[Any]:
        """
        Snare code snippets using a regular expression pattern.

        Args:
            pattern (str): The regular expression pattern to snare.
            text (str): The text to search for the pattern.

        Returns:
            str | None: The snared code snippet or None if no match is found.

        Raises:
            ValueError: If the pattern is not a string or if it is an invalid regex pattern.
        """
        try:
            if not isinstance(pattern, str):
                raise ValueError("Pattern must be a string")
            logging.info(f"Snaring code snippets with pattern: {pattern}")
            match = re.search(pattern, text)
            return match.group() if match else None
        except ValueError as e:
            logging.exception(f"Error occurred while snaring code snippets: {e}")

    def trap(self, lines, file_name="file.py"):
        trapped_code = []
        if not isinstance(lines, str):
            raise ValueError("Lines must be a string")
        line_range = lines.split("-")
        if len(line_range) != 2:
            raise ValueError("Invalid line range")
        start_line, end_line = map(int, line_range)
        if not (start_line.isdigit() and (end_line.isdigit() or end_line == "end")):
            raise ValueError("Invalid line range")
        if not start_line.isdigit() or not end_line.isdigit():
            raise ValueError("Start line and end line must be integers")
        if start_line >= end_line:
            raise ValueError("Start line cannot be greater than or equal to end line")
        try:
            file_path = get_file_path(file_name)
            trapped_code.extend(
                self.get_code_at_line(file_path, line)
                for line in range(start_line, end_line + 1)
            )
            logging.info(f"Trapping code in lines {lines}")
            return trapped_code
        except (FileNotFoundError, PermissionError):
            logging.exception("Error occurred while trapping code")
            raise

    def lure(self, string: str, dir: str) -> List[str]:
        """
        Lure code snippets containing a specific string.

        Args:
            string (str): The string to use for luring.
            dir (str): The directory to search for code snippets.

        Returns:
            List[str]: A list of code snippets containing the specified string.
        """
        if not isinstance(string, str):
            raise ValueError("String must be a string")
        try:
            logging.info(f"Luring code with string: {string}")
            # Implement code luring functionality here
            lured_code = []
            for file_path in glob.glob(dir + '/**/*.py', recursive=True):
                with open(file_path, 'r') as f:
                    for line in f:
                        if string in line:
                            lured_code.append(line)
            return lured_code
        except FileNotFoundError as e:
            logging.error(f"File not found: {e}")
        except PermissionError as e:
            logging.error(f"Permission error: {e}")
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
