# 計算時間見積もり
# 使い方:
# ℓ27 に使用する計算量をオーダー表記で記入
# ℓ28 に提示されているリストの長さとかかる時間(ms)を入力
# ℓ29 に求める時間に対するリストの長さを入力
import math

def estimate_calc_time(complexity, data, input_size):
    data_size, data_time = data
    if complexity == "O(1)":
        ratio = 1
    elif complexity == "O(n)":
        ratio = input_size / data_size
    elif complexity == "O(n^2)":
        ratio = (input_size / data_size) ** 2
    elif complexity == "O(logn)":
        ratio = math.log(input_size) / math.log(data_size)
    elif complexity == "O(nlogn)":
        ratio = (input_size * math.log(input_size)) / (data_size * math.log(data_size))
    elif complexity == "O(2^n)":
        ratio = (2 ** input_size) / (2 ** data_size)
    else:
        raise ValueError("この関数ではその計算量は想定されていません")
    
    return data_time * ratio

complexity = "O(nlogn)"
data = [10000, 6]  #[長さ, ms]
input_size = 100000 #長さ

estimated_time = estimate_calc_time(complexity, data, input_size)
print(f"長さ {input_size} のリストをソートするのにかかる時間は {estimated_time} ms です")