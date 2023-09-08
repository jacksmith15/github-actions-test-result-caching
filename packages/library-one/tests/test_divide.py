from library_one import divide


class TestDivide:
    @staticmethod
    def should_divide_a_number():
        assert divide(5, 2) == 2.5
