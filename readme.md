# Word Scramble

![word_scramble_logo](logo.png)

## Overview
A simple tool for solving anagrams, or finding words in a set of letters, e.g. [Countdown Conundrum](https://en.wikipedia.org/wiki/Countdown_(game_show)), [Scrabble](https://en.wikipedia.org/wiki/Scrabble).

## Implementation
This program was written in Python. It iterates over a list of words and finds any that have the exact same letters and are the exact same length as the target letters.

The program also contains a number of variations that hash the list of words in different ways to make the searching faster. This would only be useful if the list of words was held in memory between searches.

### Hash Strategies
* Use the length of the word as a hash key (hash_length.py)
* Use the set of letters in the word as the hash key (hash_set.py)
* Use sort all the letters in a word and use that as a hash key (hash_sorted.py)

## Installation
Just clone this repository.

```bash
$ https://github.com/richardadalton/word_scramble.git
```

## Running Word Scramble

Run the find_words.py file

```bash
$ python find_words.py -h find_words.py [-h] [-f FILE] [-l LETTERS] [-m MINIMUM]

arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Path to file containing list of valid words.
  -l LETTERS, --letters LETTERS
                        Letters to use when making words
  -m MINIMUM, --minimum MINIMUM
                        Minimum length of word to find.
```