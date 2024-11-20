class InfixToRPN:
    def __init__(self):
        # 演算子の優先順位を定義
        self.precedence = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '^': 3
        }

    def is_operator(self, char):
        """文字が演算子かどうかを判定"""
        return char in self.precedence

    def higher_precedence(self, op1, op2):
        """演算子の優先順位を比較"""
        if op1 not in self.precedence or op2 not in self.precedence:
            return False
        return self.precedence[op1] >= self.precedence[op2]

    def convert(self, expression):
        """中間記法を逆ポーランド記法に変換"""
        tokens = self.tokenize(expression)
        stack = []  # 演算子を一時的に格納するスタック
        output = []  # 出力用のリスト

        for token in tokens:
            if token.isdigit() or (token[0] == '-' and len(token) > 1 and token[1:].isdigit()):
                # 数値の場合は直接出力に追加
                output.append(token)
            elif token == '(':
                # 開き括弧はスタックに追加
                stack.append(token)
            elif token == ')':
                # 閉じ括弧が見つかった場合、開き括弧まで演算子を取り出す
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                if stack and stack[-1] == '(':
                    stack.pop()  # 開き括弧を除去
            elif self.is_operator(token):
                # 演算子の場合、優先順位に従って処理
                while (stack and stack[-1] != '(' and 
                       self.higher_precedence(stack[-1], token)):
                    output.append(stack.pop())
                stack.append(token)

        # スタックに残っている演算子をすべて出力に追加
        while stack:
            if stack[-1] == '(':
                return "Error: Mismatched parentheses"
            output.append(stack.pop())

        return ' '.join(output)

    def tokenize(self, expression):
        """式をトークンに分割"""
        tokens = []
        current_number = ''
        
        i = 0
        while i < len(expression):
            char = expression[i]
            
            if char.isspace():
                # スペースをスキップ
                i += 1
                continue
                
            if char.isdigit():
                # 数値の処理
                current_number = char
                i += 1
                while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                    current_number += expression[i]
                    i += 1
                tokens.append(current_number)
                continue
                
            if char in '+-*/^()':
                # 演算子と括弧の処理
                tokens.append(char)
            
            i += 1
            
        return tokens

# 使用例
def main():
    converter = InfixToRPN()
    
    input_str = input("Enter an infix expression: (divided by space)")
    
    result = converter.convert(input_str)
    print("Reverse Polish is :", result)


if __name__ == "__main__":
    main()