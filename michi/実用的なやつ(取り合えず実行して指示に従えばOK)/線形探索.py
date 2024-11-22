def linear_search(lst,x):
    compare, com_time = [], 0
    for a in lst:
        if a == x:
            compare.append(a)
            com_time += 1
            print("探索回数: {} 回, 探索履歴: {}".format(com_time, compare))
        else:
            compare.append(a)
            com_time += 1


lst = list(map(int, input("空白区切りで線形探索対象の数列を入力してください\n例）10 25 37 9 16\n数字の列:").split()))
target = int(input("探索対象の数値を入力して下さい:"))
linear_search(lst, target)