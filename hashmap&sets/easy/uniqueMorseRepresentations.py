# https://leetcode.com/problems/unique-morse-code-words/description/

def uniqueMorseRepresentations(words: list[str]):
    alp = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
           "....", "..", ".---", "-.-", ".-..", "--", "-.",
           "---", ".--.", "--.-", ".-.", "...", "-", "..-",
           "...-", ".--", "-..-", "-.--", "--.."]

    seen = {"".join(alp[ord(c) - 97] for c in word) for word in words}

    return len(seen)


print(uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))  # 2
