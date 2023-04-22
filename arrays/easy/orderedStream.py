# https://leetcode.com/problems/design-an-ordered-stream/description/

class OrderedStream:
    ptr = 0

    values: list

    def __init__(self, n: int):
        self.values = [''] * n

    def insert(self, idKey: int, value: str) -> list[str]:
        self.values[idKey - 1] = value

        if self.ptr == idKey - 1:
            chunk = []

            for i in range(self.ptr, len(self.values)):
                if self.values[i]:
                    chunk.append(self.values[i])
                    self.ptr += 1
                else:
                    break

            return chunk

        return []


os = OrderedStream(5)
os.insert(3, "ccccc")  # Inserts (3, "ccccc"), returns [].
os.insert(1, "aaaaa")  # Inserts (1, "aaaaa"), returns ["aaaaa"].
os.insert(2, "bbbbb")  # Inserts (2, "bbbbb"), returns ["bbbbb", "ccccc"].
os.insert(5, "eeeee")  # Inserts (5, "eeeee"), returns [].
os.insert(4, "ddddd")  # Inserts (4, "ddddd"), returns ["ddddd", "eeeee"].
