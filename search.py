import sys
from main import SuffixTree


def read_file(digits=''):
    """ Function reads all phone numbers and add them to Suffix Tree. """

    with open('numbers.txt') as file:
        data = ''.join(file.readlines())
        for number in data.split():
            suffix.add(number)
            suffix.search(digits)
        if suffix.numbers:
            for number in suffix.numbers:
                print(number)
        else:
            print('Sorry, nothing information.')


if __name__ == "__main__":
    suffix = SuffixTree()
    try:
        value = sys.argv[1]
        if value == '--help' and len(sys.argv) == 2:
            print("This script for searching phone numbers by first digits.\n"
                  "-If you want to show all phone numbers: '--show'\n"
                  "-If you want to search phone numbers: '--search <first digits>'\n"
                  "\tFor example: '--search 380'")

        elif value == '--show' and len(sys.argv) == 2:
            print('List of phone numbers:')
            read_file()

        elif value == '--search' and len(sys.argv) == 3 and int(sys.argv[2]):
            first_digits = sys.argv[2]
            print('Search phone number which start with ' + first_digits + ':')
            read_file(first_digits)
        else:
            print("Error. Write correct request! Try '--help' for more information.")
            sys.exit(1)
    except IndexError:
        print("Error. Write more arguments! Try '--help' for more information.")
        sys.exit(1)
    except ValueError:
        print("Error. Write correct request! Try '--help' for more information.")
        sys.exit(1)

