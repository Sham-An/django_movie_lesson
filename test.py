from pathlib import Path
import os


if __name__ == '__main__':

    BASE_DIR1 = Path(__file__).resolve().parent.parent
    BASE_DIR2 = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    NAME = (BASE_DIR2 / 'db.sqlite3')
    NAME2 = os.path.join(BASE_DIR2, 'db.sqlite3')

    print(BASE_DIR1)
    print(BASE_DIR2)
    print(NAME)
    print(NAME2)

