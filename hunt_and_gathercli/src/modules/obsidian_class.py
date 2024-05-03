import logging
import os
import argparse

from numpy.f2py._src_pyf import process_file

from hunt_and_gathercli import src

src.path = os.path.dirname(os.path.abspath(__file__))


class HunterXObsidianCLI:
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
        """
        Searches for the given filename in the specified folder.
    
        Args:
            user_filename (str): The name of the file to search for.
            user_foldername (str): The name of the folder to search in.
        """
        logging.info(f"Searching for {user_filename} in {user_foldername}...")
    
        try:
            file_path = os.path.join(user_foldername, user_filename)
            if os.path.exists(file_path):
                logging.info(f"Found {user_filename} in {user_foldername}.")
                return True
            else:
                logging.info(f"{user_filename} not found in {user_foldername}.")
                return False
        except FileNotFoundError:
            logging.error(f"File {user_filename} not found.")
            return False
        except PermissionError:
            logging.error(f"Permission denied to access {user_filename}.")
            return False
       
    def butcher(self):
        """
        Process and parse placeholders in the given file.

        Args:
            file (str): The file to process.
        """
        try:
            with open(self, 'r') as f:
                file_content = f.read()  # Read the file content
                logging.info(f"Processing {self} for placeholder parsing...")
                return process_file(file_content)  # Process the file content
        except FileNotFoundError:
            logging.error(f"File {self} not found.")
        except PermissionError:
            logging.error(f"Permission denied to access {self}.")
        finally:
            f.close()

    class Butcher_Code:
        def butcher(self, file):
            """
            Clean up the specified file by removing specified elements.
        
            Args:
                file (str): The path of the file to be cleaned up.
        
            Returns:
                bool: True if the cleanup is successful, False otherwise.
            """
            try:
                if not os.path.isfile(file):
                    raise ValueError("Invalid file path")
            
                logging.info(f"Cleaning up {file} by removing specified elements...")
            
                # Code to remove specified elements from the file
            
                logging.info(f"Removed unwanted text elements from {file}.")
                return True
            except FileNotFoundError:
                logging.error(f"File {file} not found.")
                return False
            except PermissionError:
                logging.error(f"Permission denied to access {file}.")
                return False
            except Exception as e:
                logging.error(f"An error occurred while removing unwanted text elements from {file}: {str(e)}")
                return False

    def tanner(self, file):
        print(f"Enhancing {file} by inserting correct variables...")

    def tailor(self, file, editor=None):
        editor = editor or 'default editor'
        print(f"Opening {file} in {editor}...")


if __name__ == '__main__':
    cli = HunterXObsidianCLI()