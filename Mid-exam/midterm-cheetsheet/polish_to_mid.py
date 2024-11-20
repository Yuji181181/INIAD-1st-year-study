def prefix_to_infix(expression):
    """
    前置記法（ポーランド記法）の式を中置記法に変換する関数
    
    Args:
        expression (str): スペース区切りの前置記法の式
        
    Returns:
        str: 中置記法に変換された式
        
    Examples:
        >>> prefix_to_infix("+ 2 3")
        '(2 + 3)'
        >>> prefix_to_infix("* + 2 3 4")
        '((2 + 3) * 4)'
    """
    tokens = expression.split()
    stack = []
    
    # 演算子の集合
    operators = {'+', '-', '*', '/', '^'}
    
    # 式を逆順に処理
    for token in reversed(tokens):
        if token in operators:
            # 演算子の場合、スタックから2つのオペランドを取り出して処理
            operand1 = stack.pop()
            operand2 = stack.pop()
            # 中置記法形式で括弧をつけて結合
            infix = f"({operand1} {token} {operand2})"
            stack.append(infix)
        else:
            # オペランドの場合はそのままスタックに追加
            stack.append(token)
    
    # 最終的な結果を返す
    return stack[0]

# テストケース
def test_prefix_to_infix():
    test_cases = [
        ("+ 2 3", "(2 + 3)"),
        ("* + 2 3 4", "((2 + 3) * 4)"),
        ("- * 3 4 5", "((3 * 4) - 5)"),
        ("* 2 + 3 4", "(2 * (3 + 4))"),
        ("/ + 7 * 4 2 3", "((7 + (4 * 2)) / 3)"),
    ]
    
    for test_input, expected in test_cases:
        result = prefix_to_infix(test_input)
        assert result == expected, f"Test failed for input '{test_input}'. Expected '{expected}', but got '{result}'"
        print(f"Test passed for input: {test_input}")
        print(f"Result: {result}")
        print("-" * 40)

if __name__ == "__main__":
    # テストケースを実行
    test_prefix_to_infix()
    
    # 対話的な入力テスト
    while True:
        try:
            expression = input("\n前置記法の式を入力してください（終了するにはCtrl+C）: ")
            result = prefix_to_infix(expression)
            print(f"中置記法: {result}")
        except KeyboardInterrupt:
            print("\nプログラムを終了します")
            break
        except Exception as e:
            print(f"エラーが発生しました: {e}")