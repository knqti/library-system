import csv


def export_dictionary_to_csv(csv_file, dictionary):
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)

        for item in dictionary.values():
            writer.writerow([
                item.author_last,
                item.author_first,
                item.book_title,
                item.book_edition,
                item.book_status,
                item.book_due_date
            ])