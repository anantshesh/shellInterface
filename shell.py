from cmd import Cmd
 
class MyPrompt(Cmd):

	# This is used to change the label name
    prompt = 'Anantshesh >> '

    # Used to display a message every time it is run
    intro = "Welcome to my Customized Shell interface"
 
 	# Exits the shell
    def do_exit(self, inp):
        '''exit the application.'''
        print("Bye")
        return True
 
MyPrompt().cmdloop()