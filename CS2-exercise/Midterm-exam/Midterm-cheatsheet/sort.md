# Python Sort Cheat Sheet

## 1. Pythonのソート
### ソートとは
データの集まりを一定の規則で並べ替えることを「ソート」と言います。リストに含まれた要素を、要素間の全順序関係（大小関係）に従って並べ替えます。主に「昇順」と「降順」があります。

### ソート方法
- `sorted(list)`: 元のリストを変更せず、新しいソートされたリストを返します。
- `list.sort()`: 元のリストを直接変更し、ソートします。

### 例
```python
# 昇順ソート
numbers = [5, 2, 9, 1]
sorted_numbers = sorted(numbers)  # [1, 2, 5, 9]
numbers.sort()                    # [1, 2, 5, 9]

# 降順ソート
sorted_numbers_desc = sorted(numbers, reverse=True)  
# [9, 5, 2, 1]
```
2. オブジェクトのソート自分で定義したクラスのインスタンスのリストをソートする場合、クラスが比較可能である必要があります。  
例: Animalクラスの定義
```python
class Animal:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
      
    def __lt__(self, other):
        return self.speed < other.speed

# Animalインスタンスのリスト
animals = [Animal("Cheetah", 70), Animal("Tortoise", 0.5), Animal("Horse", 30)]
# speedに基づいてソート
sorted_animals = sorted(animals)  
```
この場合、`__lt__` メソッドを定義して、優先度を指定します。
3. 任意のキーでのソートsorted() 関数の key パラメータを使用すると、比較する基準を変更できます。  
例: 文字列のリストを大文字小文字無視でソート
```python
strings = ["banana", "Apple", "cherry"]
sorted_strings = sorted(strings, key=str.lower)  
# ['Apple', 'banana', 'cherry']
#整数のリストを1の桁の値でソート
numbers = [23, 45, 12, 9, 11]
sorted_by_last_digit = sorted(numbers, key=lambda x: x % 10)  
# [9, 11, 12, 23, 45]
```
1. まとめ
Pythonのソートには、`sorted()` と `list.sort()` の2つがある。
オブジェクトをソートするには、比較可能（< を実装）である必要がある。
任意のキーによるソートは、key パラメータを使用して定義できる。
このチートシートは、Pythonにおけるソート機能に関する基本的な事項をカバーしています。必要に応じて、他の詳細や例も追加してください。