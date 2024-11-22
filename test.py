from collections import deque

target = [7, 3, 8, 1, 2, 6, 4, 5]  ## ここにソートしたいリストを入力

# pivotの選択方法を指定する関数
def get_pivot_index(arr, start, end, method='first', middle_bias='lower'):
    if method == 'first':
        return start
    elif method == 'last':
        return end - 1
    elif method == 'middle':
        mid = (start + end) // 2
        # 要素数が偶数の場合の処理
        if (end - start) % 2 == 0:
            # middle_biasの値に応じて、中央の2つの要素のどちらかを選択
            if middle_bias == 'lower':
                return mid - 1  # 前半の最後尾を選択
            elif middle_bias == 'upper':
                return mid      # 後半の先頭を選択
        return mid
    elif method == 'random':
        import random
        return random.randint(start, end - 1)
    return start  # デフォルト

count = 0
que = deque([[0, len(target)]])
# pivotの選択方法を指定（'first', 'last', 'middle', 'random'のいずれか）
pivot_method = 'middle'  
middle_bias = 'lower'  # 'lower'か'upper'を指定

print("簡易版クイックソート (quick sort) / O(nlogn) ~ O(n^2)")
while len(que):
    count += 1
    q = que.popleft()
    if q[0] == q[1]:
        continue

    # pivotのインデックスを選択方法に基づいて取得
    pivot_idx = get_pivot_index(target, q[0], q[1], pivot_method, middle_bias)
    pivot = target[pivot_idx]
    
    lst1 = [x for x in target[q[0]:q[1]] if x < pivot]
    lst2 = [x for x in target[q[0]:q[1]] if x == pivot]
    lst3 = [x for x in target[q[0]:q[1]] if x > pivot]
    target = target[:q[0]] + lst1 + lst2 + lst3 + target[q[1]:]

    if 1 < len(lst1): que.append([q[0], q[0] + len(lst1)])
    if 1 < len(lst2): que.append([q[0] + len(lst1), q[0] + len(lst1) + len(lst2)])
    if 1 < len(lst3): que.append([q[0] + len(lst1) + len(lst2), q[1]])

    print("比較回数 {}. [{}]".format(count, ", ".join(map(str, target))), "pivot:", pivot)