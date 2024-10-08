import csv
import datetime
import os


# Get directory
current_directory = os.path.dirname(os.path.abspath(__file__))
library_file = os.path.join(current_directory, 'library.csv')

def display_books():
    with open(library_file, 'r') as file:
        reader = csv.reader(file)

        next(reader) # skip header row
        print(f'{"Author":<20} | {"Title":<20} | {"Edition":<8} | {"Status":<10} | {"Due Date":<10}')
        print('-' * 80)

        for row in reader:
            print(f'{row[0][:20]:<20} | {row[1][:20]:<20} | {row[2]:<8} | {row[3]:<10} | {row[4]:<10}')


def main():
    # User input
    print('\n== Library Checkout System ==')
    print('1. Display books')
    print('2. Check out book')
    print('3. Return book')
    print('4. Exit')
    
    user_choice = input('>>> Type a number and press enter to choose: ')

    if user_choice == '1':
        display_books()

    elif user_choice == '2':
        # function
        print('chose 2')
    elif user_choice == '3':
        # function
        print('chose 3')
    elif user_choice == '4':
        # exit function
        print('chose 4')
    else:
        print('Invalid choice. Please try again.')
        # loop back to start???

if __name__ == '__main__':
    main()