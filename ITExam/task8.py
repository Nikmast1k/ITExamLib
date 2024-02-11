from itertools import product


def findWordByPosition(alphabet: str, repeat: int, position: int):
    all_words = []
    for x in product(sorted(alphabet), repeat=repeat):
        all_words.append(x)
        if len(all_words) == position:
            return ''.join(el for el in list(x))


def findPositionOfWord(alphabet: str, repeat: int, word: str):
    cnt = 0
    for x in product(sorted(alphabet), repeat=repeat):
        cnt += 1
        x = ''.join(el for el in list(x))
        if x == word:
            return cnt



