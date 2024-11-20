def get_precedence(operator):
    """演算子の優先順位を返す"""
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3
    }
    return precedence.get(operator, 0)

def infix_to_polish(expression):
    """中間記法をポーランド記法に変換する"""
    # 結果とスタックを初期化
    result = []
    stack = []
    
    # 式を逆順に処理
    tokens = expression.split()
    tokens.reverse()
    
    for token in tokens:
        # トークンが数値の場合
        if token.isalnum():
            result.append(token)
        
        # 閉じカッコの場合
        elif token == ')':
            stack.append(token)
            
        # 開きカッコの場合
        elif token == '(':
            while stack and stack[-1] != ')':
                result.append(stack.pop())
            if stack:
                stack.pop()  # 対応する閉じカッコを削除
                
        # 演算子の場合
        else:
            while (stack and stack[-1] != ')' and 
                   get_precedence(token) <= get_precedence(stack[-1])):
                result.append(stack.pop())
            stack.append(token)
    
    # スタックに残っている演算子をすべて結果に追加
    while stack:
        result.append(stack.pop())
    
    # 結果を反転して返す
    result.reverse()
    return ' '.join(result)

# テスト用の実行コード
def test_conversion():
    test_cases = [
        "A + B",
        "A + B * C",
        "( A + B ) * C",
        "A + B * C + D",
        "( A + B ) * ( C + D )",
        "A * B + C * D",
        "A + B + C + D"
    ]
    
    print("中間記法 → ポーランド記法 の変換テスト:")
    print("-" * 50)
    for expr in test_cases:
        polish = infix_to_polish(expr)
        print(f"入力: {expr}")
        print(f"出力: {polish}")
        print("-" * 50)
        
def main():
    expression = input("中間記法の式を入力してください: (区切りはスペース)")
    polish = infix_to_polish(expression)
    print(f"ポーランド記法: {polish}")

if __name__ == "__main__":
    main()