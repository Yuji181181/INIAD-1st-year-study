# 偶数の時、後半の先頭を列の中心とみなす
# lst = [9, 10, 25, 27, 43, 55, 77, 78, 90, 95]
# target = 95
lst = list(map(int, input("空白区切りで二分探索対象の数列を入力してください\n例）10 25 37 9 16\n数字の列:").split()))
target = int(input("探索対象の数値を入力して下さい:"))

count = 0 # 探索回数
log = [] # 探索履歴
lstSorted = sorted(lst) # もしsortされていなかった場合不具合が生じる

left, right = 0, len(lst) # 範囲 (left < mid < right)
while left < right:
    # 列の中心の設定
    mid = (left + right) // 2

    # 探索回数・履歴を更新
    count += 1
    log.append(lst[mid])

    if lst[mid] < target:
        left = mid + 1

    elif lst[mid] == target:
        break

    else:
        right = mid

print("探索回数: {} 回, 探索履歴: {}".format(count, log))