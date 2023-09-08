from library_one import exponent


class TestExponent:
    @staticmethod
    def should_perform_exponentiation():
        assert exponent(3, 4) == 81
