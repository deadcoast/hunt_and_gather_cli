import logging


class HunterXTrophy:
    def __init__(self):
        self.captured_code = None

    def trophy(self, save):
        """
        This method saves the captured code as a file.

        Args:
            save (str): The file path to save the captured code.

        Returns:
            bool: True if the saving process was successful, False otherwise.
        """
        try:
            if not isinstance(save, str) or not save:
                raise ValueError("Save parameter must be a non-empty string")
            logging.info(f"Saving captured code as: {save}")
            with open(save, 'w') as file:
                file.write(self.captured_code)
            return True
        except Exception as e:
            logging.error(f"Error occurred while saving captured code: {e}")
            return False