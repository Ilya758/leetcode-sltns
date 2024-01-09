class Cashier:

    def __init__(self, n: int, discount: int, products: list[int], prices: list[int]):
        self.n = n
        self.d = discount
        self.cache = {a: b for a, b in zip(products, prices)}
        self.c = 0

    def getBill(self, product: list[int], amount: list[int]) -> float:
        cur = sum(self.cache[a] * b for a, b in zip(product, amount)) 
        self.c += 1

        return (cur * (100 - self.d) / 100) if self.c % self.n == 0 else cur