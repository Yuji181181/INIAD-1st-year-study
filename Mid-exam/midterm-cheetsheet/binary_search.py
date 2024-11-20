#使い方:
#sorted_list に対象の数列をソートしたリストの形で入力
#target に検索したい数字を入力

def binary_search(lst, x):
    start = 0
    end = len(lst)
    comparisons = [] 
    count = 0         
    if x not in lst:
        print("対象の数字が見つかりません。")
        return
    while start < end:
        mid = start + (end - start) // 2
        comparisons.append(lst[mid])
        count += 1 

        if x > lst[mid]:
            start = mid + 1
        elif x < lst[mid]:
            end = mid
        else:
            print("対象の数字が見つかりました。")
            print("比較した数字の列:", comparisons)
            print("比較回数:", count)
            return

sorted_list = [2, 5, 12, 24, 31, 38, 43, 48, 57, 69, 88, 93, 99]
target = 31

binary_search(sorted_list, target)