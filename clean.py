from pathlib import Path
import shutil
import sys
from threading import Thread

folders = []
OUTPUT = Path("sorted")


def grabs_folder(path: Path) -> None:
    for el in path.iterdir():
        if el.is_dir():
            folders.append(el)
            grabs_folder(el)


def copy_file(path: Path) -> None:
    for el in path.iterdir():
        if el.is_file():
            ext = el.suffix[1:]
            ext_folder = OUTPUT / ext
            try:
                ext_folder.mkdir(exist_ok=True, parents=True)
                shutil.copyfile(el, ext_folder / el.name)
            except OSError as err:
                print(err)


if __name__ == "__main__":
    try:
        source = Path(sys.argv[1])
        folders.append(source)
        grabs_folder(source)

        threads = []
        for folder in folders:
            th = Thread(target=copy_file, args=(folder,))
            th.start()
            threads.append(th)

        [th.join() for th in threads]
        print(f"Папка {source} від сортована ")

    except FileNotFoundError:
        print("Дана апка не їснує!")
    except IndexError:
        print("Введіть назву папки")
