class HuntCLINavigator:
    def __init__(self):
        self.commands = {
            'help': self.help_menu,
            'map': self.show_map,
            'hunt': self.hunt_options,
            'gather': self.gather_files,
            'skin': self.skin_files,
            'butcher': self.butcher_files,
            'tanner': self.tan_files,
            'tailor': self.tailor_files,
        }
        self.ascii_art = {
            'header': "###### # ## ### #### ### ## # ######\n#### ### hag CLI hunt.gather ## ####\n### ### NAVIGATION COMMANDS  ### ###\n## ##### # --- map --- # -- ##### ##",
            'footer': "####################################"
        }

    def navigate(self, command):
        action = self.commands.get(command, self.unknown_command)
        return action()

    def help_menu(self):
        return "Available Commands: help, map, hunt, gather, skin, butcher, tanner, tailor"

    def show_map(self):
        return self.ascii_art[
            'header'] + "\n1. help = /?, -h\n2. map = map\n3. hunt = \n6. gather = gather, ga\n7. skin = skin\n8. butcher = butch\n9. tanner = tanner, tan\n10. tailor = cloak, build\n" + \
            self.ascii_art['footer']

    def hunt_options(self):
        return "Hunting Options: prey, track, snare, trap, lure, bait, camouflage, decoy, blind, trophy"

    def gather_files(self):
        return "Gathering files... Use -file [filename] --dir [directory] to specify files and directories."

    def skin_files(self):
        return "Skinning file... Use -file [filename] to specify the file for skinning."

    def butcher_files(self):
        return "Butchering file... Use -file [filename] to remove unwanted elements like backticks and brackets."

    def tan_files(self):
        return "Tanning files... Use -file [filename] to insert correct variables."

    def tailor_files(self):
        return "Tailoring file... Use -file [filename] --editor [editor_name] to open the file in the specified editor."

    def unknown_command(self):
        return "Unknown command. Type 'help' for a list of commands."


if __name__ == "__main__":
    cli_nav = HuntCLINavigator()
    user_input = input("Enter your command: ")
    print(cli_nav.navigate(user_input))
