from random import randrange

# List of names to choose from
name_list = ['John Doe', 'Jane Doe', 'Jimmy Dane', 'Carlos Guerra', 'Random Name',
            'Alex Caza', 'Dina Caon', 'Michel Caza', 'Aleksandra Zernova']

# List of numbers to choose from
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Function to randomly choose a name and number, then remove it from the
# originating list so that it doesn't get called again.
def choose_name(names, numbers):
    name = names[randrange(0, len(names))]
    names.remove(name)
    number = numbers[randrange(0, len(numbers))]
    numbers.remove(number)

    print "Winner name: " + name + " \n" + "Number: #" + str(number)

def main():
    # Start of the while loop.
    # Askes user to press enter then checks for empty string to continue.
    user_input = raw_input("Press <Enter> to start!")
    if user_input == "":
        while True:
            # Runs the function written above passing in the lists
            # to choose the names and numbers from
            choose_name(name_list, number_list)
            # if the lists don't have anything in them anymore; let the
            # user know the program is done and break the loop.
            if len(number_list) is 0 or len(name_list) is 0:
                print "All done"
                break;
            # A cheap way to stop the loop and wait for input. Could be
            # anything, really.
            continue_question = raw_input("Continute running?")

if __name__ == '__main__':
    main()
