import os
import logging


class HunterXTrophy:
    def __init__(self):
        self.captured_code = None

    def set_captured_code(self, code: str):
        """
        This method sets the captured code.

        Args:
            code (str): The captured code to be set.

        Returns:
            None

        Raises:
            InvalidCodeError: If the provided `code` is not a non-empty string.
        """
        if not isinstance(code, str) or not code:
            raise InvalidCodeError("Code must be a non-empty string")
        self.captured_code = code

    def trophy(self, save):
        """
        This method saves the captured code as a file.

        Args:
            save (str): The file path to save the captured code.

        Returns:
            None

        Raises:
            InvalidSaveError: If the provided `save` is not a non-empty string or if the file path is invalid.
            FileNotFoundError: If the file path is not found.
            IsADirectoryError: If the file path is a directory.
        """
        try:
            if not isinstance(save, str) or not save:
                raise InvalidSaveError("Save parameter must be a non-empty string")
            if self.captured_code:
                if not os.path.isdir(os.path.dirname(save)):
                    os.makedirs(os.path.dirname(save))
                with open(save, 'w', encoding='utf-8') as file:
                    file.write(self.captured_code)
                logging.info(f"Saving captured code as: {save}")
        except InvalidSaveError as e:
            raise
        except FileNotFoundError as e:
            raise
        except IsADirectoryError as e:
            raise
        except Exception as e:
            raise

class InvalidCodeError(TypeError):
    """
    This exception is raised when an invalid code is encountered.
    """
    def __init__(self, message: str):
        super().__init__(message)
    
    def __str__(self):
        return "Invalid code provided. Code must be a non-empty string."

class InvalidSaveError(IOError):
    """
    This exception is raised when the provided save path is invalid.
    """
    def __init__(self, file_path: str):
        super().__init__("Invalid save path provided: {}. The save path must be a non-empty string and a valid file path.".format(file_path))
        self.file_path = file_path

    def __str__(self):
        return super().__str__()

    def __repr__(self):
        return f"InvalidSaveError(file_path={repr(self.file_path)})"