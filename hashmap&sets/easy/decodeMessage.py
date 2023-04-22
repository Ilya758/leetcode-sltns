# https://leetcode.com/problems/decode-the-message/
from collections import defaultdict


def decodeMessage(key: str, message: str) -> str:
    map = defaultdict(str)
    ptr = 0
    map[' '] = ' '

    for char in key:
        if not map[char]:
            map[char] = chr(97 + ptr)
            ptr += 1

    return "".join([map[char] for char in message])


print(decodeMessage(key="the quick brown fox jumps over the lazy dog",
      message="vkbs bs t suepuv"))  # "this is a secret"
