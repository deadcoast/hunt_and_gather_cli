import itertools
import logging
import os


class HunterXSkinTool:
    """
    A class for handling the skinning tool.
    """

    def __init__(self, file_path, clean=False):
        self.file_path = file_path
        self.clean = clean
        self.code_lines = []

    @staticmethod
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
            raise e

    def check_file_path(self, file_path):
        """
        Check if the file path is valid.

        Args:
            file_path (str): The path of the file.

        Raises:
            ValueError: If the file path is not a string.
            FileNotFoundError: If the specified file does not exist.
        """
        if not isinstance(file_path, str):
            raise ValueError("File path must be a string")
        if not os.path.isfile(file_path):
            raise FileNotFoundError("File does not exist")

    def get_file_path(self, file_name):
        """
        Get the path of the specified file.

        Args:
            file_name (str): The name of the file.

        Returns:
            str: The path of the specified file.

        Raises:
            ValueError: If the file name is not a string.
            FileNotFoundError: If the specified file does not exist.
        """
        self.check_file_path(file_name)
        return os.path.abspath(file_name)

    def skin(self):
        """
        Skins the specified file.

        Args:
        Returns:
            None

        Raises:
            ValueError: If the file path is not a string.
            FileNotFoundError: If the specified file does not exist.
            PermissionError: If there is a permission error while accessing the file.
        """
        self.check_file_path(self.file_path)
        if self.clean:
            self.code_lines = []
        else:
            with open(self.file_path, 'r') as file:
                self.code_lines = file.readlines()

        logging.info(f"Skinned {self.file_path}")

        return self

    def __str__(self):
        if self.code_lines is None or len(self.code_lines) == 0:
            return "No code lines available"
        try:
            return '\n'.join(self.code_lines)
        except Exception as e:
            logging.exception(f"Error occurred while joining code lines: {e}")
            return ''

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        try:
            return iter(self.code_lines)
        except Exception as e:
            logging.error(f"Error occurred during iteration: {e}")
            raise

    def __len__(self):
        """
        Returns the length of the code lines.
        """
        if self.code_lines is None:
            return 0
        if not isinstance(self.code_lines, list):
            return 0
        try:
            logging.debug(f"Length of code lines: {len(self.code_lines)}")
            return len(self.code_lines)
        except Exception as e:
            logging.error(f"Error occurred while getting length: {e}")
            return 0