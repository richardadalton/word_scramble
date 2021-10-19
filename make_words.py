def load_words():
    with open ("/usr/share/dict/words") as f:
        words = f.read().lower().split("\n")
    return words


def can_make(word, letters):
    letter_list = [l for l in letters]

    for l in word:
        if l not in letter_list:
            return False
        else:
            letter_list.remove(l)

    return True


def find_matches(words, letters):
    matches = [word for word in words if can_make(word, letters)]
    return sorted(matches, key=len, reverse=True)


def solve(letters):
    words = load_words()
    print("Solution for", letters)
    print(find_matches(words, letters))

solve("aoeiomsth")