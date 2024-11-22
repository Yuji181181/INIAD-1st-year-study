#選択ソート
#計算量: O(n) /n回ループし、一番小さいものと先頭を入れ替える。

# 選択ソートの実装 (Moocsより)
def selection_sort(lst):
    length = len(lst)
    for i in range(length):
        minpos = i
        for j in range(i + 1, length):
            if lst[j] < lst[minpos]:
                minpos = j
        if i != minpos:
            tmp = lst[i]
            lst[i] = lst[minpos]
            lst[minpos] = tmp

# 過程を表示する用
target = [10, 2, 5, 8, 1, 4, 3, 7, 9, 6]

def selection_sort_show(lst):
    print("選択ソート (selection sort) / O(n^2)")
    for i in range(len(lst)):
        tmin, tloc = 10 ** 18, -1 # データの初期化
        for j in range(i, len(lst)):

            # 現在の最小値より小さい値が見つかったとき
            # 最も小さい値とその場所を更新する
            if lst[j] < tmin:
                tmin = lst[j]
                tloc = j
        
        # ループが終了したら入れ替える
        lst[i], lst[tloc] = lst[tloc], lst[i]
        print("loop {}. {}".format(str(i + 1).zfill(2), lst))

selection_sort_show(target)