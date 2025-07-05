from collections import deque
from typing import List

def word_ladder(beginWord: str, endWord: str, wordList: List[str]) -> List[str]:
    wordSet = set(wordList)
    if endWord not in wordSet:
        return []

    queue = deque([[beginWord]])
    visited = set([beginWord])

    while queue:
        level_visited = set()
        for _ in range(len(queue)):
            path = queue.popleft()
            current_word = path[-1]

            if current_word == endWord:
                return path

            for i in range(len(current_word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = current_word[:i] + c + current_word[i+1:]
                    if next_word in wordSet and next_word not in visited:
                        queue.append(path + [next_word])
                        level_visited.add(next_word)

        visited.update(level_visited)

    return []


def test():
    print(word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
    # Expected: ["hit", "hot", "dot", "dog", "cog"] or any shortest path

    print(word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
    # Expected: [] because "cog" is not in the list

test()
