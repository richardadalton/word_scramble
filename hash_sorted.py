# Hash words by sorting their letters narrow search space for a specific word

def load_words():
    with open ("words.txt") as f:
        wordlist = f.read().lower().split("\n")

    words = dict()
    for word in wordlist:
        key = "".join(sorted(word))
        prev = words.get(key, [])
        prev.append(word)
        words[key] = prev

    print("Number of entries in original word list", len(wordlist))
    print("Number of entries in hash table", len(words))
    return words

def find_matches(words, letters):
    key = "".join(sorted(letters))
    return words.get(key, [])


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