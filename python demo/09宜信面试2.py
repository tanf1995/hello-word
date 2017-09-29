nums = list(map(int, input().split(" ")))
n = nums[0]
w = nums[1]

all = 1
for i in range(w):
    all *= n

res_bac = n * (n - 1) ** (w - 1)

res = all - res_bac
res = res % 100003
print(res)