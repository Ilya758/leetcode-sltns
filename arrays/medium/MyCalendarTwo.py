class MyCalendarTwo:

    def __init__(self):
        self.A = []
        self.B = []        

    def check(self, a, b, c, d):
        return max(a, c) < min(b, d)

    def get(self, a, b, c, d):
        return (max(a, c), min(b, d))

    def book(self, start: int, end: int) -> bool:
        for booking in self.B:
            if self.check(*booking, start, end):
                return False

        for booking in self.A:
            if self.check(*booking, start, end):
                self.B.append(self.get(*booking, start, end))

        self.A.append((start, end))

        return True