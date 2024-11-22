import math
list = ["O(n)", "O(logn)", "O(nlogn)", "O(n^2)"]
def change(num, n, c = None):
    if num == 1: return n
    if num == 2: return math.log2(n)
    if num == 3: return n * math.log2(n)
    if num == 4: return n ** 2
    if num == 5: return c ** n

def solve(a, b, leng, time, aleng, lst_cnt, c1 = 0, c2 = 0):
    ans = time * change(b, aleng, c2) / change(a, leng, c1)
    sa = list[a-1] if a != 5 else "O({}^n)".format(c1)
    sb = list[b-1] if b != 5 else "O({}^n)".format(c2)
    print("計算量 {} において 要素数 {}, {} ms のものの 計算量 {}, 要素数 {} への変換結果: {} ms".format(sa, leng, time, sb, aleng, (ans * lst_cnt)))

# 要素数の設定
# length = 100000
length = int(input("要素数を入力してください:"))

# 元の時間の設定
# before_ms = 30
before_ms = float(input("元の時間を入力して下さい(ms):"))

# 変更後の要素数の設定
# after_length = 1000000
after_length = int(input("変更後の要素数を入力して下さい:"))

# 対応する数字を選択
# O(n) = 1
# O(logn) = 2
# O(nlogn) = 3
# O(n^2) = 4
# O(C**n) = 5

print("\nO(n) = 1 ※線形探索など\nO(logn) = 2 ※二分探索など\nO(nlogn) = 3 ※マージソート・クイックソートなど\nO(n^2) = 4 ※選択ソートなど\nO(C**n) = 5")
before_number = int(input("変更前の対応する数字を入力して下さい:"))
after_number = int(input("変更後の対応する数字を入力して下さい:"))
lst_num = int(input("変更後のリストの数を入力して下さい（特に指定がない場合は1を入力して下さい):"))
print("\n")
solve(before_number, after_number, length, before_ms, after_length, lst_num)

# 変換元の計算量、変換先の計算量を設定して実行

# < 具体例 >
# O(nlogn) → O(nlogn) に変換するとき
# solve(3, 3, length, before_ms, after_length)

# O(n) → O(n^2) に変換するとき
# solve(3, 4, length, before_ms, after_length)

# O(2^n) → O(3^n) に変換するとき
# solve(5, 5, length, before_ms, after_length, 2, 3)

# 線形探索:O(n)
# 二分探索:O(logn)
# マージソート:O(nlogn)
# 選択ソート:O(n^2)
# クイックソート:O(nlogn)