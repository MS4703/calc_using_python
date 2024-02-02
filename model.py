ERROR_MSG = 'ERROR'

# Create a Model to handle the calculator's operation
    
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

def evaluateExpression(expression):
    try:
        result = str(eval(expression, {}, {}))
    except Exception:
        result = ERROR_MSG

    return result
    # Handle length conversions
    if expression in {'mm_to_cm', 'cm_to_mm', 'm_to_cm', 'cm_to_m', 'inch_to_cm', 'cm_to_inch'}:
        return expression

    try:
        result = str(eval(expression, {}, {}))
    except Exception:
        result = ERROR_MSG

    return result
