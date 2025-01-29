def generate_insert_commands(table_name):
    # データ内容
    data = [
        ("田所浩二のアルバム", "田所浩二", 114514, 810),
    ]

    # SQLコマンド生成
    commands = []
    for album_title, artist, track_name, seconds in data:
        command = (
            f"INSERT INTO {table_name} (album_title, artist, track_name, seconds) " # テーブル名と列名を指定
            f"VALUES ('{album_title}', '{artist}', '{track_name}', {seconds});"
        )
        commands.append(command)

    return commands

# 実行
if __name__ == "__main__":
    # 任意のテーブル名を指定
    table_name = input("テーブル名を入力してください: ").strip()

    # コマンド生成
    commands = generate_insert_commands(table_name)

    print(f"-- {table_name} Table Commands --")
    for command in commands:
        print(command)
