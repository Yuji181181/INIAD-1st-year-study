def generate_delete_commands(table_name):
    # データ内容（削除対象のアルバムタイトルとアーティスト）
    data = [
        ("田所浩二のアルバム", "田所浩二"),  # 削除対象のアルバムタイトルとアーティストを指定
    ]

    # SQLコマンド生成
    commands = []
    for album_title, artist in data:
        command = (
            f"DELETE FROM {table_name} "
            f"WHERE album_title = '{album_title}' AND artist = '{artist}';"
        )
        commands.append(command)

    return commands

# 実行
if __name__ == "__main__":
    # 任意のテーブル名を指定
    table_name = input("テーブル名を入力してください: ").strip()

    # コマンド生成
    commands = generate_delete_commands(table_name)

    print(f"-- {table_name} Table Delete Commands --")
    for command in commands:
        print(command)
