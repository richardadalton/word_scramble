
# 205ms

def load_words():
    with open ("/usr/share/dict/words") as f:
        words = f.read().lower().split("\n")
    return words


def can_make(word, letters):
    letter_list = [c for c in letters]

    for c in word:
        if c not in letter_list:
            return False
        else:
            letter_list.remove(c)

    return True


def find_matches(words, letters):
    matches = []
    for word in words:
        if can_make(word, letters):
            matches.append(word)
    return sorted(matches, key=len, reverse=True)


def solve(words, letters):
    print("Solution for", letters)
    print(find_matches(words, letters))


def main():
    words = load_words()
    solve(words, "aoeiomsth")

main()
