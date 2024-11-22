import math
# 単体
ans = - (1 / 2) * math.log2(1 / 2)
print(ans)

# 複数
ans = 0
datas = [3/7, 3/7, 1/7]
for s in datas:
    ans -= s * math.log2(s)

print(ans)
print("四捨五入忘れずに！")