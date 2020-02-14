def Convert_To_Word():

    # Create dictionary to compare
    numDict = {"0": "zero",
               "1": "one",
               "2": "two",
               "3": "three",
               "4": "four",
               "5": "five",
               "6": "six",
               "7": "seven",
               "8": "eight",
               "9": "nine"}

    # Loop to keep application running until 'quit' command
    while True:
        print("Please enter an number to convert or 'quit' to exit the application")
        num = input()
        if num == "quit":
            print("Application quit!")
            break
        
        # Validate empty input 
        while len(num) == 0:
            num = input("Empty input founded. Please enter a number: ")

        # Validate non-number input
        while not(CheckStringTryParse(num)):
            num = input("Please enter an integer: ")

        # Loop to print out result via checking key value
        for char in num:
            print(numDict[char], end=' ')

        print()


def CheckStringTryParse(str):
    try:
        return int(str)
    except ValueError:
        return False


Convert_To_Word()
