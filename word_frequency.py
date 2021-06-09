
from string import punctuation


STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has',
    'he', 'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to',
    'were', 'will', 'with'
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    file = open("one-today.txt")
    print(file)


# Clean up text--get rid of punctuation and make sure text is lowercase


empty_string = ""


for file in punctuation:
    file = file.replace('x', empty_string)
    file = file.lower()

    print(file)


# if __name__ == "__main__":
#     import argparse
#     from pathlib import Path

#     parser = argparse.ArgumentParser(
#         description='Get the word frequency in a text file.')
#     parser.add_argument('file', help='file to read')
#     args = parser.parse_args()

#     file = Path(args.file)
#     if file.is_file():
#         print_word_freq(file)
#     else:
#         print(f"{file} does not exist!")
#         exit(1)"""
