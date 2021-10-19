def load_words():
    with open ("/usr/share/dict/words") as f:
        words = f.read().lower().split("\n")
    return words


def find_matches(words, letters):
    same_length = list(filter(lambda x: len(x) == len(letters), words))
    same_letters = list(filter(lambda x: set(x) == set(letters), same_length))
    return list(filter(lambda x: ''.join(sorted(x)) == ''.join(sorted(letters)), same_letters))


def solve(words, letters):
    print("Solution for", letters)
    print(find_matches(words, letters))


def main():
    words = load_words()
    solve(words, "vegdances")
    # solve(words, "lubecairn")
    # solve(words, "uteisrtac")
    # solve(words, "bttopoasr")
    # solve(words, "inlcertea")

main()