class ProductOfNumbers:

    def __init__(self):
        self.nums = []
        self.prefix = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix = []
        else:
            self.prefix.append((self.prefix[-1] if self.prefix else 1) * num)

    def getProduct(self, k: int) -> int:
        n = len(self.prefix)

        if k > n:
            return 0

        return self.prefix[-1] // (self.prefix[n-k-1] if n-k-1 >= 0 else 1)
    
productOfNumbers = ProductOfNumbers();
productOfNumbers.add(3);        # // [3]
productOfNumbers.add(0);        # // [3,0]
productOfNumbers.add(2);        # // [3,0,2]
productOfNumbers.add(5);        # // [3,0,2,5]
productOfNumbers.add(4);        # // [3,0,2,5,4]
productOfNumbers.getProduct(2); # // return 20. The product of the last 2 numbers is 5 * 4 = 20
productOfNumbers.getProduct(3); # // return 40. The product of the last 3 numbers is 2 * 5 * 4 = 40
productOfNumbers.getProduct(4); # // return 0. The product of the last 4 numbers is 0 * 2 * 5 * 4 = 0
productOfNumbers.add(8);        # // [3,0,2,5,4,8]
productOfNumbers.getProduct(2); # // return 32. The product of the last 2 numbers is 4 * 8 = 32 
