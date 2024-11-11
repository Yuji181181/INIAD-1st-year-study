# n枚のハノイの塔を a から c へ移動する
# 手順を表示する関数
def hanoi(n, a, b, c):
    if n == 1:
        print('move', a, 'to', c)
    else:
        hanoi(n-1, a, c, b)  # [A]: n-1枚をaからbへ (cを補助)
        print('move', a, 'to', c) # [B]: 一番大きい円盤をaからcへ
        hanoi(n-1, b, a, c)  # [C]: n-1枚をbからcへ (aを補助)



# 実行例
hanoi(4, 1, 2, 3) 