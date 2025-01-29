import math

# 情報エントロピーを計算するプログラム
# 
# 使い方:
# 1. ps_kakuritu リストに確率の配列を設定する (合計が1になるように)
# 2. プログラムを実行すると、その確率分布の情報エントロピーを計算して表示
#
# 例: ps_kakuritu = [3/7,3/7,1/7] の場合、
#     それぞれの確率が 0.429, 0.429, 0.143 の分布のエントロピーを計算

def entropy(ps):
    """
    確率分布の情報エントロピーを計算する
    :param ps: 確率の配列 (合計が1になる必要あり)
    :return: 情報エントロピー (単位: ビット)
    """
    result = 0
    for p in ps:
        result -= p * math.log2(p)
    return result

ps_kakuritu = [3/7,3/7,1/7]

print(entropy(ps_kakuritu))