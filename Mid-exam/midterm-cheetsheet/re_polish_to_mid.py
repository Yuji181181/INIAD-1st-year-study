class RPNConverter:
    def __init__(self):
        # 演算子の優先順位を定義
        self.precedence = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '^': 3
        }

    def is_operator(self, token):
        """トークンが演算子かどうかを判定"""
        return token in self.precedence

    def add_parentheses(self, expr1, expr2, operator):
        """必要に応じて括弧を追加"""
        # 演算子の優先順位を取得
        op_prec = self.precedence[operator]
        
        # 式1の最後の演算子の優先順位をチェック
        if expr1.strip('()').find(' ') != -1:  # 式1が複合式の場合
            last_op = expr1.strip('()').split(' ')[-2]
            if self.is_operator(last_op) and self.precedence[last_op] < op_prec:
                expr1 = f"({expr1})"
        
        # 式2の最初の演算子の優先順位をチェック
        if expr2.strip('()').find(' ') != -1:  # 式2が複合式の場合
            first_op = expr2.strip('()').split(' ')[1]
            if self.is_operator(first_op) and self.precedence[first_op] <= op_prec:
                expr2 = f"({expr2})"
        
        return expr1, expr2

    def to_infix(self, rpn_expr):
        """逆ポーランド記法から中置記法に変換"""
        if not rpn_expr:
            return ""

        # スペースで区切られた式をトークンに分割
        tokens = rpn_expr.split()
        stack = []

        for token in tokens:
            if not self.is_operator(token):
                # オペランドの場合はそのままスタックに積む
                stack.append(token)
            else:
                # 演算子の場合、スタックから2つの式を取り出して結合
                if len(stack) < 2:
                    raise ValueError("Invalid RPN expression")
                
                expr2 = stack.pop()
                expr1 = stack.pop()
                
                # 必要に応じて括弧を追加
                expr1, expr2 = self.add_parentheses(expr1, expr2, token)
                
                # 新しい式を作成してスタックに積む
                new_expr = f"{expr1} {token} {expr2}"
                stack.append(new_expr)

        if len(stack) != 1:
            raise ValueError("Invalid RPN expression")

        return stack[0]

# 使用例
def main():
    converter = RPNConverter()
    
    test_cases = [
        "3 4 +",
        "3 4 2 * +",
        "3 4 + 5 *",
        "3 4 + 5 6 + *",
        "3 4 * 5 6 * +",
        "a b + c *",
        "p q * r s * +",
        "a b + c d + *"
    ]
    
    print("逆ポーランド記法 → 中置記法 の変換例:")
    print("-" * 40)
    for rpn in test_cases:
        try:
            infix = converter.to_infix(rpn)
            print(f"{rpn:20} → {infix}")
        except ValueError as e:
            print(f"Error: {e}")
            
    input_string = input("Enter an RPN expression: (space-separated)")
    infix = converter.to_infix(input_string)
    print(f"Infix expression: {infix}")
    
if __name__ == "__main__":
    main()