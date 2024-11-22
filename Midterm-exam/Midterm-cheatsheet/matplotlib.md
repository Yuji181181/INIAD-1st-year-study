
# Matplotlib グラフ描写と CSV データ可視化 チートシート

## Matplotlibによるグラフ描画

### 基本的な使い方

1. **ライブラリのインポート**
   ```python
   import matplotlib.pyplot as plt


    データの準備
    xs = []
    ys = []
    for i in range(10, 101):
        x = i * 0.1
        xs.append(x)
        ys.append(x)



    グラフの描画
    plt.plot(xs, ys, label='$y = x$')
    plt.xlim([1, 10])  # x軸の範囲設定
    plt.title('Graph of $y = x$')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()


    表示オプション

    x軸とy軸の範囲を設定する
    plt.xlim([xmin, xmax])
    plt.ylim([ymin, ymax])



    タイトルとラベルの設定
    plt.title('グラフのタイトル')
    plt.xlabel('X軸のラベル')
    plt.ylabel('Y軸のラベル')
    ```

CSVファイルのデータ可視化基本的な手順
```python

必要なライブラリのインポート
import matplotlib.pyplot as plt
import csv



CSVファイルのデータを読み込む
with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)  # ヘッダーの読み込み
    data = [row for row in reader]



データの処理
dates = []
avg_temps = []
for row in data:
    dates.append(row[0])  # 日付
    avg_temps.append(float(row[1]))  # 平均気温



データの可視化
plt.plot(dates, avg_temps, label='平均気温', color='blue')
plt.title('日別平均気温')
plt.xlabel('日付')
plt.ylabel('平均気温 (℃)')
plt.xticks(rotation=45)
plt.legend()
plt.show()
```


CSVファイルについて
CSVとは: Comma-Separated Values (CSV) は、複数の項目をカンマで区切ったテキストデータです。
CSVファイルの例:
```csv
日付,平均気温,最低気温,最高気温
2021/9/1,23.5,18.3,20.7
2021/9/2,19.4,18.4,20.6
2021/9/3,19.7,18.7,21.4
```

