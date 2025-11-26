from pathlib import Path
from .speakers import Saiful

def main():
    Saiful().print_name()
    with (Path(__file__).parent / "names.txt").open() as f:
        print(f.read())

if __name__ == "__main__":
    main()