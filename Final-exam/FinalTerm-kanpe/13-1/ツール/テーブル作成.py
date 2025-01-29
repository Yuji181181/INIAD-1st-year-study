def generate_create_table_command(table_name, columns):
    
    columns_def = ", ".join([f"{col[0]} {col[1]}" for col in columns])
    
    
    create_table_sql = f"CREATE TABLE {table_name} ({columns_def});"
    return create_table_sql


table_name = "employees" # テーブル名を入力
columns = [
    ("id", "INTEGER PRIMARY KEY"),  # 列名とデータ型を入力
    ("name", "TEXT NOT NULL"),
    ("age", "INTEGER"),
    ("department", "TEXT")
]


sql_command = generate_create_table_command(table_name, columns)
print(sql_command)
