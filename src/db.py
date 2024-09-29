import os
import sqlite3
import pickle

DB_PATH=os.path.join(os.getcwd(), "data", "posts_infos.sqlite")
EXTRACTED_INFOS_FILE_PATH=os.path.join(os.getcwd(), "data", "posts_extracted_infos.pkl")

def main():
    with open(EXTRACTED_INFOS_FILE_PATH, "rb") as input_file:
        posts_info_list = pickle.load(input_file)

    with sqlite3.connect(DB_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='posts_infos'")
        if not cursor.fetchone():
            columns = list(posts_info_list[0].keys())
            cursor.execute(f"CREATE TABLE posts_infos({",".join(columns)})")
            columns_with_colon = [":" + column for column in columns]
            cursor.executemany(f"INSERT INTO posts_infos VALUES({",".join(columns_with_colon)})", posts_info_list)


if __name__ == "__main__":
    main()