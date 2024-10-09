import csv
import datetime
import os


def display_books(library_file):
    with open(library_file, 'r') as file:
        reader = csv.reader(file)

        # Display header section
        print(f'\n{"Index":<5} | {"Author-Last":<20} | {"Author-First":<20} | {"Title":<19} | {"Edition":<8} | {"Status":<10} | {"Due Date":<10}')
        print('-' * 110)

        # Display library content
        for index, row in enumerate(reader):
            print(f'{index:<5} | {row[0][:20]:<20} | {row[1][:20]:<20} | {row[2][:20]:<20}| {row[3]:<8} | {row[4]:<10} | {row[5]:<10}')


def check_out_book(library_file):
    # confirmation = check_out_confirmation(library_file)
    
    with open(library_file, 'r') as file:
        reader = csv.reader(file)

        user_check_out = input('\n>>> Select the Index number to check out (x to main menu): ').strip().lower()

        for index, row in enumerate(reader):

            if user_check_out == 'x':
                # Exit function
                return user_check_out
        
            elif index == int(user_check_out):
                print(f'\nChecking out:')
                print(f'{row[2]} by {row[0]}, {row[1]}')    
                return user_check_out



def main():

    # Get directory and file
    current_directory = os.path.dirname(os.path.abspath(__file__))
    library_file = os.path.join(current_directory, 'library.csv')

    # Main menu
    while True:
        print('\n== Library Main Menu ==')
        print('1. Display books')
        print('2. Check out book')
        print('3. Return book')
        print('4. Exit')
        
        user_navigation = input('>>> Select a number to navigate: ').strip()

        # Display books
        if user_navigation == '1':
            display_books(library_file)
            continue

        # Check out book
        elif user_navigation == '2':
            user_choice = check_out_book(library_file)
            
            if user_choice == 'x':
                continue

            elif 1 <= int(user_choice) <= 4:
                print('\nCheck-out complete!')
                continue

        # Return book
        elif user_navigation == '3':
            # function
            print('chose 3')
        
        # Exit
        elif user_navigation == '4':
            break
        
        else:
            print('Invalid choice. Please try again.')
            print('Type a number that matches a choice listed. Then press enter.')
            continue


if __name__ == '__main__':
    main()