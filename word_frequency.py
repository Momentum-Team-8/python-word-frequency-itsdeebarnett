
punctuations = "!$'()*+,-./:;<=>?@[\]^_`{|}~"


STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has',
    'he', 'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to',
    'were', 'will', 'with'
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    file = open('one-today.txt', 'rt')

    text = file.read().lower()
    for line_text in text:
        if line_text not in punctuations:
            empty_string = " "
        empty_string += line_text
        line_text = text.strip()
        line_text = text.split()
        wrdcount = []
    for wrd in line_text:
        wrdcount.append(line_text.count(wrd))
        print("Pairs\n" + str(list(zip(line_text, wrdcount))))

    def removeStopwords(line_text, STOP_WORDS):
        return[wrd for wrd in line_text if wrd not in STOP_WORDS]
        # print(line_text)

# Clean up text--get rid of punctuation and make sure text is lowercase


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
