import logging
class HunterXUnknownHandler(ValueError):
    __UNKNOWN_COMMAND_MESSAGE = "Unknown command. Please try again."

    def handle_unknown_command(self, command=None):
        """
        This method handles unknown commands.
        """
        if command:
            raise ValueError(f"Unknown command: {command}. Please try again.")
        else:
            raise ValueError(self.__UNKNOWN_COMMAND_MESSAGE)