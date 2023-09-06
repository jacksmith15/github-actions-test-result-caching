from library_one import product


class TestProduct:
    @staticmethod
    def should_multiply_two_numbers():
        assert product(5, 3) == 15
