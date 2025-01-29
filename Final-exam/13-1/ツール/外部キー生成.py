def generate_foreign_key_constraint(fk_column, ref_table, ref_column):
    foreign_key_constraint = f"FOREIGN KEY ({fk_column}) REFERENCES {ref_table}({ref_column})"
    return foreign_key_constraint

# 使用例
if __name__ == "__main__":
    # 任意のパラメータを指定
    fk_column = 'x'  # 外部キーとして使用するカラム名
    ref_table = 'y'  # 参照先テーブル名
    ref_column = 'z'  # 参照先テーブルのカラム名

    constraint = generate_foreign_key_constraint(fk_column, ref_table, ref_column)

    # 結果の外部キー制約を表示
    print(constraint)


#公式
# FOREIGN KEY (x) REFERENCES y(z)