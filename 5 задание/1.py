import random
import string
from pathlib import Path

def create_random_files(directory: str = "random_files", count: int = 10, length: int = 8):
    dir_path = Path(directory)
    dir_path.mkdir(exist_ok=True)
    chars = string.ascii_letters + string.digits

    for _ in range(count):
        name = ''.join(random.choice(chars) for _ in range(length))
        file_path = dir_path / f"{name}.txt"
        file_path.touch(exist_ok=True)

    for file_path in dir_path.glob("*.txt"):
        print(file_path.absolute())

if __name__ == "__main__":
    print("Задание 1:")
    create_random_files()
