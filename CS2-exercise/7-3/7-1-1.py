def one(n):
    """1をn回足す関数 (実質的にはnを返す関数)"""
    if n == 0:
        return 0  # ベースケース：0回足すと0
    else:
        return one(n - 1) + 1


def power(x, n):
    """xをn回掛ける関数 (xのn乗を計算する関数)"""
    if n == 0:
        return 1  # ベースケース：0乗は1
    else:
        return power(x, n - 1) * x


def comb(n, k):
    """二項係数C(n, k)を計算する関数"""
    if k == 0 or k == n:
        return 1  # ベースケース：nCk は k=0 または k=n のとき 1
    elif k < 0 or k > n:
        return 0  # kが範囲外の場合は0
    else:
        return comb(n - 1, k) + comb(n - 1, k - 1)



# テスト (必要に応じてコメントを外して実行してください)
print(one(5))  # 出力: 5
print(power(2, 3))  # 出力: 8
print(comb(5, 2))  # 出力: 10