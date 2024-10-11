import os
from my_functions import check_out_book, display_books, export_dictionary_to_csv, initialize_dictionary, return_book


def main():

    # Get directory and file
    current_directory = os.path.dirname(os.path.abspath(__file__))
    library_file = os.path.join(current_directory, 'library.csv')

    # Initalize the dictionary of books
    book_dictionary = {}
    book_dictionary = initialize_dictionary(library_file, book_dictionary)
    total_books = len(book_dictionary)
    
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
            display_books(book_dictionary)
            continue

        # Check out book
        elif user_navigation == '2':
            check_out_result = check_out_book(book_dictionary, total_books)
            
            if check_out_result == 'x':
                continue

            elif check_out_result == 'success':
                export_dictionary_to_csv(library_file, book_dictionary)            
                print('\nCheck out complete!')
                continue

        # Return book
        elif user_navigation == '3':
            return_result = return_book(book_dictionary, total_books)

            if return_result == 'x':
                continue
            
            elif return_result =='success':
                export_dictionary_to_csv(library_file, book_dictionary)
                print('\nReturn complete!')
                continue

        # Exit
        elif user_navigation == '4':
            print('Goodbye!')
            break
        
        else:
            print('Invalid choice. Please try again.')
            print('Type a number that matches a choice listed, then press enter.')
            continue


if __name__ == '__main__':
    main()