class UnknownCommand(Exception):
    UNKNOWN_COMMAND_MESSAGE = "Unknown command. Please try again."

    def unknown_command(self, command=None):
        """
        This method handles unknown commands.
        """
        if command:
            logging.warning(f"Unknown command: {command}. Please try again.")
        else:
            logging.warning(self.UNKNOWN_COMMAND_MESSAGE)
        return False