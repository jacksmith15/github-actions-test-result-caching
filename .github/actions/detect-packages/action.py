import json
import os
from pathlib import Path
from typing import Optional


def main():
    changed_files = _get_changed_files()

    changed_packages = {_get_package(changed_file) for changed_file in changed_files} - {None}

    set_output("packages", json.dumps(sorted(changed_packages)))


def _get_package(filepath: str) -> Optional[str]:
    path = Path(filepath)
    if len(path.parts) >= 2:
        if path.parts[0] == "packages":
            return path.parts[1]
    return None


def _get_changed_files() -> list[str]:
    path = Path(f"{os.environ['HOME']}/files.json").resolve()
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8"))


def set_output(name: str, value: str) -> None:
    output_file = os.environ.get("GITHUB_OUTPUT")
    if output_file:
        with open(output_file, "a", encoding="utf-8") as file:
            print(f"{name}={value}", file=file)
    print(f"> Set: {name}={value}")


if __name__ == "__main__":
    main()
