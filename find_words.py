import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", default="words.txt",
                        help="Path to file containing list of valid words.")
    parser.add_argument("-l", "--letters",
                        help="Letters to use when making words")
    parser.add_argument("-m", "--minimum", default=1, type=int,
                        help="Minimum length of word to find.")

    args = parser.parse_args()
    return args


def load_words(file):
    with open (file) as f:
        words = f.read().lower().split("\n")
    return words


def can_make(word, letters):
    letter_list = list(letters)

    for l in word:
        if l not in letter_list:
            return False
        else:
            letter_list.remove(l)

    return True


def find_matches(letters, words, minimum):
    matches = [word for word in words if can_make(word, letters) and len(word) >= minimum]
    return sorted(matches, key=len, reverse=True)


def solve(letters, words, minimum):
    print("Solution for", letters)
    print(find_matches(letters, words, minimum))

def main():
    args = get_arguments()
    words = load_words(args.file)
    solve(args.letters, words, args.minimum)

main()
