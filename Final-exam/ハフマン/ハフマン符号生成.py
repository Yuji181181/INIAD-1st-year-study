"""
ハフマン符号生成プログラムの使い方:

1. プログラムを実行すると、文字列の入力を求められます
2. 任意の文字列を入力してEnterを押してください
3. プログラムは以下の情報を出力します:
   - 各文字に割り当てられたハフマン符号
   - 入力文字列の文字数と各文字の出現頻度
   - ハフマン符号化後のビット列
   - 平均符号長
   - 2バイト符号化と比較した場合の圧縮率

例:
入力: hello
出力:
l: 00
o: 01
h: 10
e: 11
"""

from collections import Counter


def MIN_PRIORITY_QUEUE(S):
    return sorted(S.items(), key=lambda x: x[1], reverse=True)


def EXTRACT_MIN(Q):
    return Q.pop()


def INSERT(Q, z):
    return Q.append(z)


def HUFFMAN(S, a):
    n = len(S)
    Q = MIN_PRIORITY_QUEUE(S)
    for i in range(n - 1):
        left = EXTRACT_MIN(Q)
        right = EXTRACT_MIN(Q)
        freq = left[1] + right[1]
        z = (left[0] + right[0], freq)
        INSERT(Q, z)
        a.append([left, "0", left[0] + right[0]])
        a.append([right, "1", left[0] + right[0]])
        Q = dict(zip([i[0] for i in Q], [i[1] for i in Q]))
        Q = MIN_PRIORITY_QUEUE(Q)
    a.append([EXTRACT_MIN(Q), "", "top"])
    return a


def PrintReslut(b):
    for i in range(len(a)):
        now = a[i][0][0]
        num = a[i][1]
        j = 0
        while a[j][2] != "top":
            if a[i][2] == a[j][0][0]:
                num = a[j][1] + num
                i = j
                flag = 0
                for k in range(len(a)):
                    if a[k][0][0] == "top" or a[j][2] == a[k][0][0]:
                        flag = 1
                        break
            else:
                j += 1
        if now in s:
            b.append([now, num])
    return b


def DivideS(S):
    S = list(S)
    S = Counter(S)
    S = dict(S)
    return S


input_str = input("hello")
s = DivideS(input_str)
a = HUFFMAN(s, [])

result = PrintReslut([])

total_counts = sum(s.values())
average_code_length = 0

convert = {}


for b in sorted(result):
    convert[b[0]] = b[1]
    symbol, code = b[0], b[1]
    print(symbol + ": " + code)
    probability = s[symbol] / total_counts
    average_code_length += probability * len(code)


char_num = {}
print("文字列の出現回数と割合")
print("入力された文字列の文字数:", len(input_str))
print("文字: 出現回数, 割合")
for c in input_str:
    char_num[c] = char_num.get(c, 0) + 1

for c, n in char_num.items():
    print(f"{c}: {n}回, {n / len(input_str) * 100:.2f}%")


ans = ""
for i in input_str:
    ans += convert[i]

print("符号化後のビット列:", ans)
print("平均符号長:", average_code_length)
print(
    f"2バイトでの符号化と比較した圧縮率: {100 - (len(ans) / (len(input_str) * 16)) * 100}%"
)
