
class HunterXSkinner:

    def get_code_at_line(self, file_path, line):
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