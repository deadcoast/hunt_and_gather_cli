import argparse
import contextlib
import datetime
import html
import logging
import os
import subprocess

from poetry.mixology import result

from src.modules.hunt_and_tracker import HunterXTracker

from src.modules.hunt_and_gather_navigator import HunterXNavigator
from src.modules.obsidian_class import HunterXObsidianCLI

from src.modules.hunt_and_gather_skinner import HunterXSkinTool
from src.modules.hunt_and_gather_trap import HunterXTrap
from src.modules.hunt_and_gather_trophy import HunterXTrophy


from src.modules.hunter_unknown_handler import unknown_command

from src.modules.hunt_and_gather_skin import skin

from .test_HuntAndGatherCLI import TestHuntAndGatherCLI

# TODO: Add more options to gather command
    gather_parser.add_argument('-folder', required=False, help='Folder to gather files from')
    gather_parser.add_argument('-pattern', required=False, help='Pattern to search for in file names')
    gather_parser.add_argument('-extension', required=False, help='Extension to search for in file names')

# TODO: Add more options to knife command
    knife_parser.add_argument('-folder', required=False, help='Folder to search in')
    knife_parser.add_argument('-pattern', required=False, help='Pattern to search for in file names')
    knife_parser.add_argument('-extension', required=False, help='Extension to search for in file names')

# TODO: Add more options to tanner command
    tanner_parser.add_argument('-folder', required=False, help='Folder to search in')
    tanner_parser.add_argument('-pattern', required=False, help='Pattern to search for in file names')
    tanner_parser.add_argument('-extension', required=False, help='Extension to search for in file names')

# TODO: Add more options to tailor command
    tailor_parser.add_argument('-folder', required=False, help='Folder to search in')
    tailor_parser.add_argument('-pattern', required=False, help='Pattern to search for in file names')
    tailor_parser.add_argument('-extension', required=False, help='Extension to search for in file names')

    args = parser.parse_args()

    return args

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# TODO: Add more options to tailor command
# TODO: Add more options to tanner command
# TODO: Add more options to knife command
# TODO: Add more options to skin command
# TODO: Add more options to gather command
# TODO: Add more options to butcher command
# TODO: Add more options to tan command
# TODO: Add more options to map command


def hunter_map_navigation(cabin=False, hunt=False, knife=False, tanner=False, skin=False, tailor=False):
    try:
        command_messages = {
            'cabin': "Navigating to the cabin (main menu)...",
            'hunt': "Navigating to the hunt menu...",
            'knife': "Navigating to the knife menu...",
            'tanner': "Navigating to the tanner menu...",
            'skin': "Navigating to the skin menu...",
            'tailor': "Navigating to the tailor menu..."
        }
        if command := next(
                (command for command in locals() if locals()[command]), None
        ):
            logging.info(command_messages[command])
        else:
            logging.warning("No navigation option provided. Returning to main menu...")
    except KeyError as e:
        logging.error(f"An error occurred: {str(e)}")


def skin(file, clean, cabin):
    try:
        if not os.path.exists(file):
            logging.error(f"File {file} does not exist.")
            return
        if not os.access(file, os.R_OK):
            logging.error(f"File {file} is not readable.")
            return

        if clean:
            logging.info(f"Cleaning {file}...")
        else:
            logging.info(f"Processing {file} for skinning...")
        if cabin:
            logging.info("Returning to the main menu...")
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")


def insert_variables(file: str) -> bool:
    """
    This function attempts to insert correct variables into the specified file.

    Args:
        file (str): The file to insert variables into.

    Returns:
        bool: True if the insertion is successful, False otherwise.
    """
    try:
        logging.info(f"Attempting to insert correct variables into {file}...")
        return True
    except FileNotFoundError as e:
        logging.error(f"File not found: {str(e)}")
        return False
    except PermissionError as e:
        logging.error(f"Permission denied: {str(e)}")
        return False
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return False


def sanitize_input(command: str) -> str:
    """
    Sanitizes the input command by removing any unwanted characters or formatting.

    Args:
        command (str): The input command to be sanitized.

    Returns:
        str: The sanitized command.

    """
    if not command:
        raise ValueError("Invalid input: command cannot be None or empty.")

    return html.escape(command)


def unknown_command(command):
    """
    Logs an error message for an unknown command.

    Args:
        command (str): The unknown command.

    Raises:
        TypeError: If the command is not a string.
        ValueError: If an unknown command is encountered.

    """
    if not isinstance(command, str):
        raise TypeError("CommandParser must be a string.")

    sanitized_command = sanitize_input(command)  # Sanitize the command input

    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logging.error(
        f"Unknown command '{sanitized_command}' encountered at {current_time}. Please use 'help' to see available commands.")

    raise ValueError(f"Unknown command '{sanitized_command}'. Please use 'help' to see available commands.")


VALID_EDITORS = ['vim', 'nano', 'emacs']


def is_valid_editor(editor):
    """
    Checks if the provided editor is valid.

    Args:
        editor (str): The name of the editor to check.

    Returns:
        bool: True if the editor is valid, False otherwise.
    """
    if editor is None or editor == '':
        logging.warning("Invalid editor parameter.")
        return False

    try:
        return editor in VALID_EDITORS
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return False


def is_installed_editor(editor: str):
    """
    Check if the specified editor is installed on the system.

    Args:
        editor (str): The name of the editor to check for.

    Returns:
        bool: True if the editor is installed, False otherwise.
    """
    logging.info(f"Checking if {editor} is installed...")
    try:
        subprocess.check_output([editor, '--version'])
        logging.info(f"{editor} is installed: True")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        logging.error(f"An error occurred during the check for {editor} installation: {str(e)}")
        logging.info(f"{editor} is installed: False")
        return False


def tailor(file, editor):
    """
    Opens the specified file in the specified editor.

    Args:
        file (str): The path of the file to be opened.
        editor (str): The name of the editor to open the file with.

    Returns:
        bool: True if the file was opened successfully, False otherwise.
    """
    if file is None or file == '' or editor is None or editor == '':
        logging.warning("Invalid file or editor parameter. Returning...")
        return False

    if not os.path.exists(file):
        logging.warning(f"The file {file} does not exist.")
        return False

    if not is_valid_editor(editor) or not is_installed_editor(editor):
        logging.warning(f"{editor} is not a valid or installed editor.")
        return False

    try:
        logging.info(f"Opening {file} in {editor}...")
        return True
    except FileNotFoundError as e:
        logging.error(f"File not found: {str(e)}")
        return False
    except PermissionError as e:
        logging.error(f"Permission denied: {str(e)}")
        return False
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return False


def perform_functionality():
    pass


class Type2:
    """
    This class represents a Type2 object.
    """

    def __init__(self):
        pass

    def method1(self):
        """
        This method performs some functionality.
        """
        try:
            # code that may raise an exception
            pass
        except Exception as e:
            # handle the exception
            print(f"An error occurred: {str(e)}")

    def method2(self, param1, param2):
        """
        This method performs some functionality based on the input parameters.
        """
        # Add functionality here
        try:
            # code that may raise an exception
            pass
        except Exception as e:
            # handle the exception
            print(f"An error occurred: {str(e)}")
        return perform_functionality()


class Type1:
    """
    This class represents a Type1 object.
    """

    def __init__(self):
        pass

    def method1(self):
        """
        This method performs some functionality.
        """
        with contextlib.suppress(Exception):
            # code that may raise an exception
            pass

    def method2(self):
        """
        This method performs some functionality.
        """
        pass


def map_http_command(param1: Type1, param2: Type2) -> ReturnType:
    """
    This function maps an HTTP command to its corresponding action.
    """
    with contextlib.suppress(Exception):
        # code that may raise an exception
        pass
    return result


def skin_command(param1, param2):
    """This function executes a command related to skin."""
    with contextlib.suppress(Exception):
        # Add code to perform a task
        pass
    return result


def tanner_command(angle):
    """
    This function calculates the tannergent of a given angle.
    """
    with contextlib.suppress(Exception):
        return ...


def tailor_command(param1, param2):
    """
    This function executes a command tailored to specific requirements.
    """
    try:
        # code that may raise an error
        pass
    except Exception as e:
        # handle the error
        print(f"An error occurred: {e}")

    # Add functionality here
    print('Executing tailor command')

    return "Tailored command"


def help_command():
    """
    This function displays the help information for the command.
    
    Parameters:
    None
    
    Returns:
    None
    """
    with contextlib.suppress(Exception):
        # Add code to provide help and information
        print('This is the help command')


def gather_command():
    """
    This function gathers a command from the user and returns it.
    
    Parameters:
    None
    
    Returns:
    str: The command entered by the user.
    """
    with contextlib.suppress(Exception):
        # Add code to perform a task
        pass


def my_map(cabin, hunt, knife, tanner, skin, tailor):
    """
    This function maps the input arguments to specific values or strings.
    
    Args:
        cabin (bool): Indicates if cabin is true or false.
        hunt (bool): Indicates if hunt is true or false.
        knife (bool): Indicates if knife is true or false.
        tanner (bool): Indicates if tanner is true or false.
        skin (bool): Indicates if skin is true or false.
        tailor (bool): Indicates if tailor is true or false.
        
    Returns:
        int or str or list: The mapped value or string based on the input arguments.
    """
    if cabin:
        return 1
    elif hunt:
        return 2
    elif knife:
        return 3
    elif tanner:
        return 4
    elif skin:
        return 5
    elif tailor:
        return ['--cabin', '--hunt', '--knife', '--tanner', '--skin', '--tailor']
    else:
        return ['--cabin', '--hunt', '--knife', '--tanner', '--skin', '--tailor']


def butcher_command(arg1, arg2):
    """
    This function executes the 'butcher' command.
    """
    try:
        # code logic here
        pass
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
    return True  # or return False


def skinner(file, clean):
    """
    This method performs skinning on a given file.

    Args:
        file (str): The path of the file to be skinned.
        clean (bool): A flag indicating whether to perform a clean skinning.

    Returns:
        int: The number of lines processed if the skinning operation was successful, -1 otherwise.
    """
    try:
        logging.info(f"Starting skinning process for file: {file}")

        if not os.path.exists(file):
            raise FileNotFoundError(f"File {file} does not exist.")

        if not os.access(file, os.R_OK):
            raise PermissionError(f"File {file} is not readable.")

        if clean:
            logging.info(f"Cleaning {file}...")
        else:
            logging.info(f"Processing {file} for skinning...")

        # Perform skinning process and return the number of lines processed
        num_lines_processed = 0
        # ...

        logging.info(f"Finished skinning process for file: {file}")
        return num_lines_processed

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return -1


class HuntAndGatherCLI:
    def __init__(self):
        self.args = None
        self.command = None
        try:
            parser = argparse.ArgumentParser(
                description="Hunt and Gather CLI: Advanced CLI for handling Obsidian files")
            subparsers = parser.add_subparsers(dest='command', help='CommandParser to execute')

            # Map command
            map_parser = subparsers.add_parser('map', help='Navigate through CLI menus')
            map_parser.add_argument('-cabin', action='store_true', help='Navigate to the root menu')
            map_parser.add_argument('--hunt', action='store_true', help='Navigate to the hunt menu')
            map_parser.add_argument('--knife', action='store_true', help='Navigate to the knife menu')
            map_parser.add_argument('--tanner', action='store_true', help='Navigate to the tanner menu')
            map_parser.add_argument('--skin', action='store_true', help='Navigate to the skin menu')
            map_parser.add_argument('--tailor', action='store_true', help='Navigate to the tailor menu')

            # Skin command
            skin_parser = subparsers.add_parser('skin', help='Process placeholders in files')
            skin_parser.add_argument('--file', required=True, help='File to process')
            skin_parser.add_argument('--clean', action='store_true',
                                     help='Remove placeholders and leave the file blank')
            skin_parser.add_argument('--cabin', action='store_true', help='Return to the main menu after processing')

            # Tan command
            tanner_parser = subparsers.add_parser('tanner', help='Insert the correct variables into the file')
            tanner_parser.add_argument('--file', required=True, help='File to process')

            # Tailor command
            tailor_parser = subparsers.add_parser('tailor', help='Open the file in a specified editor')
            tailor_parser.add_argument('--file', required=True, help='File to edit')
            tailor_parser.add_argument('--editor', required=True,
                                       choices=['pycharm', 'vscode', 'vim', 'spyder', 'emacs', 'notepad++', 'sublime',
                                                'atom', 'notepad'], help='Editor to use')

            args = parser.parse_args()
            getattr(self, args.command, unknown_command)(args.cabin)
        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")

    def run(self, map_command=None, skin_command=None, tanner_command=None, tailor_command=None, help_command=None,):
        COMMAND_MAPPING = {
            'map': map_command,
            'skin': lambda: skin_command(skinner(file=self.args.file, clean=self.args.clean)),
            'tanner': lambda: tanner_command(file=self.args.file),
            'tailor': lambda: tailor_command(file=self.args.file, editor=self.args.editor),
            'cabin': lambda: unknown_command(self.args.cabin),
            'help': help_command,
            'gather': gather_command,
            'butcher': butcher_command,
        }

        command_function = COMMAND_MAPPING.get(self.command, unknown_command)
        command_function()

        try:
            self.hunter_arguments()
        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")

    def hunter_arguments(self):
        parser = argparse.ArgumentParser(
            description="Hunt and Gather CLI: Advanced CLI for handling Obsidian files")
        subparsers = parser.add_subparsers(dest='command', help='CommandParser to execute')

        # Map command
        map_parser = subparsers.add_parser('map', help='Navigate through CLI menus')
        map_parser.add_argument('-cabin', action='store_true', help='Navigate to the root menu')
        map_parser.add_argument('--hunt', action='store_true', help='Navigate to the hunt menu')
        map_parser.add_argument('--knife', action='store_true', help='Navigate to the knife menu')
        map_parser.add_argument('--tanner', action='store_true', help='Navigate to the tanner menu')
        map_parser.add_argument('--skin', action='store_true', help='Navigate to the skin menu')
        map_parser.add_argument('--tailor', action='store_true', help='Navigate to the tailor menu')

        # Skin command
        skin_parser = subparsers.add_parser('skin', help='Process placeholders in files')
        skin_parser.add_argument('--file', required=True, help='File to process')
        skin_parser.add_argument('--clean', action='store_true',
                                 help='Remove placeholders and leave the file blank')
        skin_parser.add_argument('--cabin', action='store_true', help='Return to the main menu after processing')

        # Tan command
        tanner_parser = subparsers.add_parser('tanner', help='Insert the correct variables into the file')
        tanner_parser.add_argument('--file', required=True, help='File to process')

        # Tailor command
        tailor_parser = subparsers.add_parser('tailor', help='Open the file in a specified editor')
        tailor_parser.add_argument('--file', required=True, help='File to edit')
        tailor_parser.add_argument('--editor', required=True,
                                   choices=['pycharm', 'vscode', 'vim', 'spyder', 'emacs', 'notepad++', 'sublime',
                                            'atom', 'notepad'], help='Editor to use')

        args = parser.parse_args()
        getattr(self, args.command, unknown_command)(args.cabin)

    def get_command(self):
        if self.command is None:
            self.hunter_arguments()
        return self.command

    def execute(self):
        try:
            self.parse_command_line_arguments()
        except FileNotFoundError as e:
            logging.error(f"File not found: {str(e)}")
        except PermissionError as e:
            logging.error(f"Permission denied: {str(e)}")
        except Exception as e:
            logging.exception("An error occurred")
            raise
        return True

    class CommandParser:
        def parse_command_line_arguments(self):
            """
            Parse the command line arguments.

            Returns:
                Parsed arguments for further processing.

            """
            try:
                parser = argparse.ArgumentParser(description="Hunt and Gather CLI: Advanced CLI for handling Obsidian files")
                parser.add_argument(...)
                args = parser.parse_args()
                # process the parsed arguments
                return args
            except Exception as e:
                logging.error(f"An error occurred during argument parsing: {str(e)}")

    def parse_command_line_arguments(self):
        try:
            parser = argparse.ArgumentParser(description="Hunt and Gather CLI: Advanced CLI for handling Obsidian files")
            parser.add_argument(...)
            args = parser.parse_args()
        
            # Validate file paths
            if not os.path.exists(args.file):
                logging.error(f"File {args.file} does not exist.")
                return
            if not os.access(args.file, os.R_OK):
                logging.error(f"File {args.file} is not readable.")
                return
        
            return args
        except argparse.ArgumentError as e:
            logging.error(f"An error occurred during argument parsing: {str(e)}")
        except Exception as e:
            logging.error(f"An error occurred during argument parsing: {str(e)}")


def main(log_level, logger, cli_instance):
    """
    Improved version of the main function.

    Args:
        log_level (int): The log level to set for the logger.
        cli_instance (HuntAndGatherCLI): An instance of the HuntAndGatherCLI class.
        logger (Logger): The logger to use for logging.

    Returns:
        bool: True if the CLI execution was successful, False otherwise.

    """
    try:
        cli_instance.run()
        return True
    except FileNotFoundError as e:
        logger.error(f"File not found: {str(e)}")
        return False
    except PermissionError as e:
        logger.error(f"Permission denied: {str(e)}")
        return False
    except Exception as e:
        logger.exception("An error occurred")
        return False


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    
    cli = HuntAndGatherCLI()
    main(log_level=logging.INFO, cli_instance=cli, logger=logger)
    
    # Example usage
    # logger.setLevel(logging.INFO)
    # cli = HuntAndGatherCLI()
    # main(log_level=logging.INFO, cli_instance=cli, logger=logger)

    # Example usage with user input for command
    # logger.setLevel(logging.INFO)
    # cli = HuntAndGatherCLI()
    # main(log_level=logging.INFO, cli_instance=cli, logger=logger)
    # user_input = input("Enter your command : ")

    # Example usage with user input for command and arguments (advanced usage)
    # logger.setLevel(logging.INFO)
    # cli = HuntAndGatherCLI()
    # main(log_level=logging.INFO, cli_instance=cli, logger=logger)
    # user_input = input("Enter your command : ")
    cli_app = HuntAndGatherCLI()
    user_input = input("Enter your command: ")
