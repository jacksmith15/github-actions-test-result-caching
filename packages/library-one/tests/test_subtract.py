from library_one import subtract


class TestSubtract:
    @staticmethod
    def should_subtract_a_number_from_another():
        assert subtract(5, 3) == 2
