def load_words():
    with open ("/usr/share/dict/words") as f:
        wordlist = f.read().lower().split("\n")

    words = dict()
    for word in wordlist:
        key = len(word)
        prev = words.get(key, [])
        prev.append(word)
        words[key] = prev

    return words

def find_matches(words, letters):
    key = len(letters)
    same_length = words[key]
    return list(filter(lambda x: ''.join(sorted(x)) == ''.join(sorted(letters)), same_length))


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