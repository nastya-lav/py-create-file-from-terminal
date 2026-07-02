import os
import sys
import datetime


def create_file_in_directory() -> None:
    if "-d" in sys.argv and "-f" in sys.argv:
        path = (sys.argv[sys.argv.index("-d") + 1:sys.argv.index("-f")])
        create_directory(path)
        os.chdir(*path)
        create_file()
    elif "-d" in sys.argv:
        path = sys.argv[sys.argv.index("-d") + 1:]
        create_directory(path)
    elif "-f" in sys.argv:
        create_file()


def create_directory(path: list) -> None:
    os.makedirs(os.path.join(*path))


def create_file() -> None:
    path = os.path.join(os.getcwd(), sys.argv[sys.argv.index("-f") + 1])
    with open(path, "a") as f:
        if os.path.exists(path):
            f.write("\n\n")
        f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        line_num = 0
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            line_num += 1
            f.write(f"\n{str(line_num)} {line}")


if __name__ == "__main__":
    create_file_in_directory()
