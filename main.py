import csv
import os
from datetime import datetime, timedelta


def display_books(library_file):
    with open(library_file, 'r') as file:
        reader = csv.reader(file)

        # Display header section
        print(f'\n{"Index":<5} | {"Author-Last":<20} | {"Author-First":<20} | {"Title":<19} | {"Edition":<8} | {"Status":<15} | {"Due Date":<10}')
        print('-' * 115)

        # Display library content
        for index, row in enumerate(reader):
            print(f'{index:<5} | {row[0][:20]:<20} | {row[1][:20]:<20} | {row[2][:20]:<20}| {row[3]:<8} | {row[4]:<15} | {row[5]:<10}')


def check_out_book(library_file):
    user_input = input('\n>>> Select the Index number to check out (x to main menu): ').strip().lower()

    # Unhappy route
    if user_input != 'x' and not 0<= int(user_input) <=3:
        print('Invalid choice. Please try again.\nTo check out a book, type its Index number and press enter.\nTo go back to the main menu, type "x" and press enter.')
        user_input = 'x'
        return user_input
    
    # Exit to main menu
    if user_input == 'x':
        return
    
    # Check out book
    with open(library_file, 'r') as file:
        reader = csv.reader(file)
        updated_rows = []

        for index, row in enumerate(reader):   
            if index == int(user_input):
                book_status = row[4]

                # Unhappy route
                if book_status != 'Available':
                    print('Sorry, that book is not available. Please try again.')
                    user_input = 'x'
                    return user_input

                print(f'\nChecking out:')
                print(f'{row[2]} by {row[0]}, {row[1]}')

                book_status = 'Checked out'
                book_due_date = (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d')

                row[4] = book_status
                row[5]= book_due_date
                print(f'\nYour book is due on {book_due_date}.')

            updated_rows.append(row)

    # Update the csv file
    with open(library_file, 'w',newline='') as file:
        writer = csv.writer(file)
        writer.writerows(updated_rows)

    user_input = 'success'


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
        
        user_navigation = input('\n>>> Select a number to navigate: ').strip()

        # Display books
        if user_navigation == '1':
            display_books(library_file)
            continue

        # Check out book
        elif user_navigation == '2':
            check_out_result = check_out_book(library_file)
            
            if check_out_result == 'x':
                continue

            elif check_out_result == 'success':
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