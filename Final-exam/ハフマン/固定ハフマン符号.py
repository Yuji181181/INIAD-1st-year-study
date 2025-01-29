def get_input():
    """標準入力から文字の頻度と固定コードを取得"""
    print("文字の種類の数を入力してください(AとBが対象: 2):")
    n = int(input())
    
    frequencies = {}
    print("各文字とその頻度(%)を入力してください（例: A 30）:")
    for _ in range(n):
        char, freq = input().split()
        frequencies[char] = float(freq) / 100

    fixed_codes = {}
    print("固定コードの種類の数を入力してください:")
    m = int(input())
    print("固定コードを入力してください（例: A 001 改行区切り）:")
    for _ in range(m):
        char, code = input().split()
        fixed_codes[char] = code

    return frequencies, fixed_codes

def find_available_codes(used_codes):
    """使用可能なコードのリストを生成"""
    all_codes = []
    # 最大4ビットまでのコードを生成
    for length in range(1, 5):
        for i in range(2**length):
            code = format(i, f'0{length}b')
            if code not in used_codes:
                all_codes.append((len(code), code))
    return sorted(all_codes)  # 長さ順にソート

def find_huffman_with_fixed_codes(frequencies, fixed_codes):
    """固定コード付きハフマン符号を生成"""
    # 頻度の合計を確認
    total_freq = sum(frequencies.values())
    if abs(total_freq - 1.0) > 0.01:  # 1%の誤差を許容
        print(f"警告: 頻度の合計が100%になっていません（現在: {total_freq*100:.1f}%）")
    
    # 使用済みコードを集める
    used_codes = set(fixed_codes.values())
    
    # 残りの文字に使えるコードを見つける
    available_codes = find_available_codes(used_codes)
    
    # 頻度順にソートした未割り当ての文字のリスト
    remaining_chars = sorted(
        [(char, freq) for char, freq in frequencies.items() if char not in fixed_codes],
        key=lambda x: x[1],
        reverse=True
    )
    
    # コードの割り当て
    codes = fixed_codes.copy()
    code_index = 0
    for char, _ in remaining_chars:
        while code_index < len(available_codes):
            _, code = available_codes[code_index]
            # コードが他のコードの接頭辞になっていないか確認
            if not any(c.startswith(code) or code.startswith(c) 
                      for c in codes.values() if c != code):
                codes[char] = code
                code_index += 1
                break
            code_index += 1
    
    # 結果の表示
    print("\nハフマン符号:")
    for char, code in codes.items():
        print(f"{char}: {code}")

    # 平均符号長の計算
    avg_length = sum(frequencies[char] * len(codes[char]) for char in codes)
    print(f"\n平均符号長: {avg_length:.2f}")

    return codes

def main():
    try:
        frequencies, fixed_codes = get_input()
        find_huffman_with_fixed_codes(frequencies, fixed_codes)
    except ValueError as e:
        print(f"エラー: 入力形式が正しくありません - {e}")
    except Exception as e:
        print(f"エラー: {e}")

if __name__ == "__main__":
    main()
