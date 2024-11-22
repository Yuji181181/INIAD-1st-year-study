def trace_quick_sort(lst):
    # 分割数をカウント
    division_count = 0
    
    # 分割プロセスをトレースするヘルパー関数
    def quick_sort_trace(lst):
        nonlocal division_count
        if len(lst) <= 1:
            return lst
        
        # ピボットの選択
        pivot = lst[0]
        
        # 分割
        lst1 = [x for x in lst if x < pivot]
        lst2 = [x for x in lst if x == pivot]
        lst3 = [x for x in lst if x > pivot]
        
        # 分割時の情報を出力
        division_count += 1
        print(f"分割回数 {division_count}: ピボット = {pivot}")
        print(f"  小:{lst1} 等:{lst2} 大:{lst3}")
        print(f"  現在の状態: {lst1 + lst2 + lst3}\n")
        
        # 再帰的にソート
        return quick_sort_trace(lst1) + lst2 + quick_sort_trace(lst3)
    
    # ソートの開始
    sorted_lst = quick_sort_trace(lst)
    
    # 結果の出力
    print(f"分割の合計回数: {division_count}")
    print(f"ソート結果: {sorted_lst}")
    return sorted_lst

# 使用例
numbers = list(map(int, input("空白区切りでクイックソートしたい数列を入力してください\n例）5 8 2 1 7 4 9 3\n数列:").split()))
trace_quick_sort(numbers)