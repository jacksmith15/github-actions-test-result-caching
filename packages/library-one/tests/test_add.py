from library_one import add


class TestAdd:
    @staticmethod
    def should_add_two_numbers():
        assert add(5, 3) == 8
