def generate_update_commands(table_name):
    # データ内容（例: album_titleを変更する）
    data = [
        ("田所浩二のアルバム", "田所浩二", "新しい曲名", 350),  # track_name と seconds を変更
    ]

    commands = []
    for album_title, artist, new_track_name, new_seconds in data:  # 変更後のデータを指定
        command = (
            f"UPDATE {table_name} "
            f"SET track_name = '{new_track_name}', seconds = {new_seconds} "
            f"WHERE album_title = '{album_title}' AND artist = '{artist}';"
        )
        commands.append(command)

    return commands

# 実行
if __name__ == "__main__":
    # 任意のテーブル名を指定
    table_name = input("テーブル名を入力してください: ").strip()

    commands = generate_update_commands(table_name)

    print(f"-- {table_name} Table Update Commands --")
    for command in commands:
        print(command)
