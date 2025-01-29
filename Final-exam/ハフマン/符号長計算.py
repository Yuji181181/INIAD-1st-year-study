# 以下の問題を想定したプログラム
# "生成されたコードで上記の文字列をエンコードすると、各文字にnbitずつ割り当てた場合の何%の長さとなるか。"

def nbit_encoding_efficiency(bit, data, round_num):
    result = 0
    for i in data:
        result += (i[1] / 100) * len(i[0])
    per = (result / bit) * 100
    print("四捨五入前：", per)
    return round(per, round_num) 

# 自分で書き換える部分 =======================================
round_num = 0   #小数第何桁目まで表示するか (0で整数表示)
bit = 3         #与えられたビット数
data = [
    # 文字を書く必要はない
    #["コード", 出現頻度(%)]
    ["01",30],
    ["000",12],
    ["10",19],
    ["11",21],
    ["001",18]
]
# ==========================================================

result = nbit_encoding_efficiency(bit, data, round_num)
print(f"計算結果： {result} %")