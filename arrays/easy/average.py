# https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/description/

def average(salary: list[int]) -> float:
    mn = float('inf')
    mx = float('-inf')
    sum = 0

    for s in salary:
        sum += s
        mn = min(mn, s)
        mx = max(mx, s)

    return (sum - (mx + mn)) / (len(salary) - 2)


print(average(salary=[4000, 3000, 1000, 2000]))  # 2500.0
print(average(salary=[1000, 2000, 3000]))  # 2000.0
