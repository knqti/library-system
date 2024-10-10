import csv
import os
from datetime import datetime, timedelta

from my_classes import Book


def update_dictionary(library_file, book_dictionary):
    with open(library_file, 'r') as file:
        reader = csv.reader(file)

        for index, row in enumerate(reader):
            # Assign the column values to Book's attributes
            book = Book(
                book_index=index,
                author_last=row[0],
                author_first=row[1],
                book_title=row[2],
                book_edition=row[3],
                book_status=row[4],
                book_due_date=row[5]
            )

            # Store each book into the dictionary using the index as key
            book_dictionary[book.book_index] = book

    # for book_index, item in book_dictionary.items():
    #     print(f'\nBook index: {book_index}')
    #     print(item.__dict__)
    
    return book_dictionary


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
        print('\nInvalid choice. Please try again.\nTo check out a book, type its Index number and press enter.\nTo go back to the main menu, type "x" and press enter.')
        user_input = 'x'
        return user_input
    
    # Exit to main menu
    if user_input == 'x':
        return user_input
    
    # Check out book
    with open(library_file, 'r') as file:
        reader = csv.reader(file)
        
        updated_rows = []

        for index, row in enumerate(reader):   
            book_status = row[4]
            
            if index == int(user_input) and book_status == 'Available':
                author_last_name = row[0]
                author_first_name = row[1]
                book_title = row[2]                

                print(f'\nChecking out:')
                print(f'{book_title} by {author_last_name}, {author_first_name}')

                book_status = 'Checked out'
                book_due_date = (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d')

                row[4] = book_status
                row[5]= book_due_date
                print(f'\nYour book is due on {book_due_date}.')
            
            # Unhappy route
            else:
                print('\nSorry, that book is not available. Please try again.')
                user_input = 'x'
                return user_input

            updated_rows.append(row)

    # Update the csv file
    with open(library_file, 'w',newline='') as file:
        writer = csv.writer(file)
        writer.writerows(updated_rows)

    user_input = 'success'
    return user_input


def return_book(library_file):
    user_input = input('\n>>> Select the Index number to return (x to main menu): ').strip().lower()

    # Unhappy route
    if user_input != 'x' and not 0 <= int(user_input) <= 3:
        print('\nInvalid choice. Please try again.\nTo return a book, type its Index number and press enter.\nTo go back to the main menu, type "x" and press enter.')
        user_input = 'x'
        return user_input

    # Exit to main menu
    if user_input == 'x':
        return
    
    # Return book
    with open(library_file, 'r') as file:
        reader = csv.reader(file)

        updated_rows = []

        for index, row in enumerate(reader):
            if index == int(user_input):
                author_last_name = row[0]
                author_first_name = row[1]
                book_title = row[2]
                book_status = row[4]

                # Unhappy route
                if book_status != 'Checked out':
                    print('\nSorry, that book is not checked out. Please try again.')
                    user_input = 'x'
                    return user_input
            
                print('\nReturning:')
                print(f'{book_title} by {author_last_name}, {author_first_name}')

                row[4] = 'Available'
                row[5] = ''

            updated_rows.append(row)

    # Update the csv file
    with open(library_file, 'w',newline='') as file:
        writer = csv.writer(file)
        writer.writerows(updated_rows)

    user_input = 'success'
    return user_input


def main():

    # Get directory and file
    current_directory = os.path.dirname(os.path.abspath(__file__))
    library_file = os.path.join(current_directory, 'library.csv')

    # Initalize the book dictionary
    book_dictionary = {}
    book_dictionary = update_dictionary(library_file, book_dictionary)
    
    print('Welcome to the Library!')

    # Main menu

    while True:
        print('\n== Main Menu ==')
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
            return_result = return_book(library_file)

            if return_result == 'x':
                continue
            
            elif return_result =='success':
                print('\nReturn complete!')
                continue
        
        # Exit
        elif user_navigation == '4':
            print('Goodbye!')
            break
        
        else:
            print('Invalid choice. Please try again.')
            print('Type a number that matches a choice listed. Then press enter.')
            continue


if __name__ == '__main__':
    main()