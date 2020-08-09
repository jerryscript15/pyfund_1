#!/usr/bin/env python3
"""Launches calculator programmed for simple arithemetic

Usage:
    python3 calculator.py from your Terminal.
"""
def launch_calculator():   
    """Returns a calculated value taken from the user.

    Try:
        An opportunity just incase the user inputs a wrong figure.

    Returns:
        the calculated output in the WINDOWS TERMINAL.
    """ 
    try:    
        x = input('choose your first digit: ') 
        choice = input('your operation: ')
        y = input('choose your second digit: ')  

        if choice == '+':
            print(int(x) + int(y))

        elif choice == '-':
            print(int(x) - int(y))

        elif choice == "/":
            print(int(x) / int(y))

        elif choice == "*":
            print(int(x) * int(y))
        else:
            print('Wrong imput!')
            launch_calculator()
    except ValueError: 
        print("Invalid input! Input a digit ")
        launch_calculator()#To rewrite the program if there is a valueerror.
    

def remark_printer():
    """Review for the user
    
    Returns:
        Takes the user's view to make ammendment in out next app
    """
    print("Hope you enjoyeed our app, Do let us know your view and suppot us")
    view = input("What is your view in just three words mmax: ")
    review = input("Please rate our work between 1-5: ")
    output = "| Thanks for your support, next version would be released very soon would also put your 'review: {view}' into consideration |".format(view = view)                                    
    banner = '+' + '-' * (len(output) -2) + '+'
    border = '|' + ' ' * (len(output) -2) + '|'
    lines = [banner, border, output, border, banner]#Gives the output in a box.
    comment = '\n'.join(lines)
    print(comment)
    print()


def main():
    """Prints each functions defined in the calculator.
    
    Returns:
        It relays each function defined in the program.
    """
    launch_calculator()
    remark_printer()


if __name__ == '__main__':
    main()