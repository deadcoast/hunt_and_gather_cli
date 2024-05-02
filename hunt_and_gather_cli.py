class HuntAndGatherCLI:
    def __init__(self):
        try:
            parser = argparse.ArgumentParser(
                description="Hunt and Gather CLI: Advanced CLI for handling Obsidian files")
            subparsers = parser.add_subparsers(dest='command', help='Command to execute')

            # Map command
            map_parser = subparsers.add_parser('map', help='Navigate through CLI menus')
            map_parser.add_argument('-cabin', action='store_true', help='Navigate to the root menu')
            map_parser.add_argument('--hunt', action='store_true', help='Navigate to the hunt menu')
            map_parser.add_argument('--knife', action='store_true', help='Navigate to the knife menu')
            map_parser.add_argument('--tan', action='store_true', help='Navigate to the tan menu')
            map_parser.add_argument('--skin', action='store_true', help='Navigate to the skin menu')
            map_parser.add_argument('--tailor', action='store_true', help='Navigate to the tailor menu')

            # Skin command
            skin_parser = subparsers.add_parser('skin', help='Process placeholders in files')
            skin_parser.add_argument('--file', required=True, help='File to process')
            skin_parser.add_argument('--clean', action='store_true',
                                     help='Remove placeholders and leave the file blank')
            skin_parser.add_argument('--cabin', action='store_true', help='Return to the main menu after processing')

            # Tan command
            tan_parser = subparsers.add_parser('tan', help='Insert the correct variables into the file')
            tan_parser.add_argument('--file', required=True, help='File to process')

            # Tailor command
            tailor_parser = subparsers.add_parser('tailor', help='Open the file in a specified editor')
            tailor_parser.add_argument('--file', required=True, help='File to edit')
            tailor_parser.add_argument('--editor', required=True,
                                       choices=['pycharm', 'vscode', 'vim', 'spyder', 'emacs', 'notepad++', 'sublime',
                                                'atom', 'notepad'], help='Editor to use')

            args = parser.parse_args()
            getattr(self, args.command, self.unknown_command)()
        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")

    def map(self, **kwargs):
        try:
            if kwargs['cabin']:
                logging.info("Navigating to the cabin (main menu)...")
            elif kwargs['hunt']:
                logging.info("Navigating to the hunt menu...")
            elif kwargs['knife']:
                logging.info("Navigating to the knife menu...")
            elif kwargs['tan']:
                logging.info("Navigating to the tan menu...")
            elif kwargs['skin']:
                logging.info("Navigating to the skin menu...")
            elif kwargs['tailor']:
                logging.info("Navigating to the tailor menu...")
            else:
                logging.warning("No navigation option provided. Returning to main menu...")
        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")

    def skin(self, file, clean, cabin):
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

    def tan(self, file):
        try:
            logging.info(f"Attempting to insert correct variables into {file}...")
        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")

    def tailor(self, file, editor):
        try:
            logging.info(f"Opening {file} in {editor}...")
        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")

    def unknown_command(self):
        logging.warning("Unknown command. Please use 'help' to see available commands.")


def main():
    logging.basicConfig(level=logging.INFO)
    HuntAndGatherCLI()


if __name__ == '__main__':
    main()
    cli_app = HuntAndGatherCLI()
    user_input = input("Enter your command: ")