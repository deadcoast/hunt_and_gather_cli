import argparse


class DynamicObsidianCLI:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Dynamic Obsidian Parsing CLI')
        subparsers = self.parser.add_subparsers(dest='command', help='Commands')

        # Gather command setup
        gather_parser = subparsers.add_parser('gather', help='Search for Obsidian Markdown code')
        gather_parser.add_argument('-user_filename', required=True, help='Filename to gather')
        gather_parser.add_argument('--user_foldername', required=True, help='Folder to search in')

        # Skin command setup
        skin_parser = subparsers.add_parser('skin', help='Process and parse placeholders in files')
        skin_parser.add_argument('-file', required=True, help='File to process')

        # Butcher command setup
        butcher_parser = subparsers.add_parser('butcher', help='Remove unwanted text elements from files')
        butcher_parser.add_argument('-file', required=True, help='File to clean')

        # Tanner command setup
        tanner_parser = subparsers.add_parser('tanner', help='Insert correct variables into the file')
        tanner_parser.add_argument('-file', required=True, help='File to enhance')

        # Tailor command setup
        tailor_parser = subparsers.add_parser('tailor', help='Open the file in a specific editor')
        tailor_parser.add_argument('-file', required=True, help='File to open')
        tailor_parser.add_argument('--editor',
                                   choices=['pycharm', 'vscode', 'vim', 'spyder', 'emacs', 'notepad++', 'sublime',
                                            'atom', 'notepad'], help='Editor to use')

        args = self.parser.parse_args()
        if hasattr(self, args.command):
            getattr(self, args.command)(**vars(args))

    def gather(self, user_filename, user_foldername):
        print(f"Searching for {user_filename} in {user_foldername}...")

    def skin(self, file):
        print(f"Processing {file} for placeholder parsing...")

    def butcher(self, file):
        print(f"Cleaning up {file} by removing specified elements...")

    def tanner(self, file):
        print(f"Enhancing {file} by inserting correct variables...")

    def tailor(self, file, editor=None):
        editor = editor or 'default editor'
        print(f"Opening {file} in {editor}...")


if __name__ == '__main__':
    cli = DynamicObsidianCLI()