import toml

import library_one as package


class TestVersion:
    @staticmethod
    def should_match_pyproject() -> None:
        with open("pyproject.toml", "r") as file:
            pyproject = toml.loads(file.read())
        assert pyproject["tool"]["poetry"]["version"] == package.__version__
