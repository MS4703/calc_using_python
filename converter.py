class LengthConverter:
    @staticmethod
    def mm_to_cm(value):
        return value / 10.0

    @staticmethod
    def cm_to_mm(value):
        return value * 10.0

    @staticmethod
    def m_to_cm(value):
        return value * 100.0

    @staticmethod
    def cm_to_m(value):
        return value / 100.0

    @staticmethod
    def inch_to_cm(value):
        return value * 2.54

    @staticmethod
    def cm_to_inch(value):
        return value / 2.54
