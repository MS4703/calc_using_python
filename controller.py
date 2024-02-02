# Create a Controller class to connect the GUI and the model
from functools import partial
from length_converter import LengthConverter
ERROR_MSG = 'ERROR'

class Controller:
    """PyCalc's Controller."""
    def __init__(self, model, view):
        """Controller initializer."""
        self._evaluate = model
        self._view = view
        # Connect signals and slots
        self._connectSignals()

    def _calculateResult(self):
        """Evaluate expressions."""
        result = self._evaluate(expression=self._view.getDisplayText())
        self._view.setDisplayText(result)

    def _buildExpression(self, sub_exp):
        """Build expression."""
        if self._view.getDisplayText() == ERROR_MSG:
            self._view.clearDisplay()

        expression = self._view.getDisplayText() + sub_exp
        self._view.setDisplayText(expression)

    def _connectSignals(self):
        """Connect signals and slots."""
        for btnText, btn in self._view.buttons.items():
            if btnText not in {'=', 'C'}:
                btn.clicked.connect(partial(self._buildExpression, btnText))

        self._view.buttons['='].clicked.connect(self._calculateResult)
        self._view.display.returnPressed.connect(self._calculateResult)
        self._view.buttons['C'].clicked.connect(self._view.clearDisplay)

    def _handleLengthConversion(self, conversion_type):
        value = float(self._view.getDisplayText())
        result = None

        if conversion_type == 'mm_to_cm':
            result = LengthConverter.mm_to_cm(value)
        elif conversion_type == 'cm_to_mm':
            result = LengthConverter.cm_to_mm(value)
        elif conversion_type == 'm_to_cm':
            result = LengthConverter.m_to_cm(value)
        elif conversion_type == 'cm_to_m':
            result = LengthConverter.cm_to_m(value)
        elif conversion_type == 'inch_to_cm':
            result = LengthConverter.inch_to_cm(value)
        elif conversion_type == 'cm_to_inch':
            result = LengthConverter.cm_to_inch(value)

        if result is not None:
            self._view.setDisplayText(str(result))

    def _connectLengthConversionButtons(self):
        length_conversion_buttons = {'mm_to_cm', 'cm_to_mm', 'm_to_cm', 'cm_to_m', 'inch_to_cm', 'cm_to_inch'}

        for conversion_type in length_conversion_buttons:
            self._view.buttons[conversion_type].clicked.connect(partial(self._handleLengthConversion, conversion_type))
