import pytest
from src.discount_calculator_3 import discount_calc

class TestDiscountCalc(object):

    # Testing for good arguments

    def test_general_correct_examples(self):
        assert discount_calc("52", "20") == "RESULT: The discounted price is $41.60!"
        assert discount_calc("243.9685", "35") == "RESULT: The discounted price is $158.58!" # Dot for decimals
        assert discount_calc("243,9685", "35") == "RESULT: The discounted price is $158.58!" # Comma for decimals
        
    # Testing for bad arguments
      
    def test_discount_float(self):

        """Test if float discounts are correctly handled, by transforming them to integers."""

        assert discount_calc("20", "25.5") == "RESULT: The discounted price is $14.80!"
        assert discount_calc("100", "49.8") == "RESULT: The discounted price is $50.00!"
        assert discount_calc("100", "49,8") == "RESULT: The discounted price is $50.00!"

    def test_wrong_input_string(self):

        """After submitting string inputs, it tests whether a message requesting valid inputs is raised."""   

        assert discount_calc("Twenty", "0") == "ERROR: Please provide valid inputs."
        assert discount_calc("345", "Fourteen") == "ERROR: Please provide valid inputs."
        assert discount_calc("lost", "words") == "ERROR: Please provide valid inputs."
        assert discount_calc("23", "[0, 92, 23]") == "ERROR: Please provide valid inputs." # If you input a list, it will be submitted as a string
        assert discount_calc("[0, 92, 23]", "23") == "ERROR: Please provide valid inputs."

    def test_wrong_price_value(self):

        """After submitting a price below 0, tests whether a message requesting valid inputs is raised."""   

        assert discount_calc("-100", "10") == "ERROR: Price cannot be a negative number."
        assert discount_calc("-0.01", "10") == "ERROR: Price cannot be a negative number."
        assert discount_calc("-0,15", "10") == "ERROR: Price cannot be a negative number."
        assert discount_calc("-0.1", "20") == "ERROR: Price cannot be a negative number."
        assert discount_calc("-0,1", "20") == "ERROR: Price cannot be a negative number."

    def test_wrong_discount_value(self):

        """After submitting discount values above 100 or below 0, tests whether a message requesting valid inputs is raised."""   

        assert discount_calc("2500", "-1") == "ERROR: Choose a discount between 0 and 100."
        assert discount_calc("2500", "101") == "ERROR: Choose a discount between 0 and 100."

    def test_wrong_input_missing_arg(self):

        """Tests if an error is raised if the second argument is missing."""

        with pytest.raises(TypeError):
            discount_calc("345")

    # Testing for special arguments

    def test_discount_eq_0(self):
        assert discount_calc("3500", "0") == "RESULT: This item doesn't have a discount."
        assert discount_calc("25.50", "0") == "RESULT: This item doesn't have a discount."

    def test_discount_eq_100(self):
        assert discount_calc("17", "100") == "RESULT: This item is currently free!"
        assert discount_calc("0", "100") == "RESULT: This item is currently free!"

    def test_price_eq_0(self):
        assert discount_calc("0", "50") == "RESULT: This item is currently free!"
        assert discount_calc("0", "0") == "RESULT: This item is currently free!"
        assert discount_calc("0", "100") == "RESULT: This item is currently free!"


# Parametrized function

@pytest.mark.parametrize("price, discount, result", [("", "", "ERROR: Please provide valid inputs."), 
                                                     ("", " ", "ERROR: Please provide valid inputs."),
                                                     (" ", " ", "ERROR: Please provide valid inputs."),
                                                     (" ", "", "ERROR: Please provide valid inputs."),
                                                     ("4500", "", "ERROR: Please provide valid inputs."),
                                                     ("4500", " ", "ERROR: Please provide valid inputs."),
                                                     ("", "50", "ERROR: Please provide valid inputs."),
                                                     (" ", "50", "ERROR: Please provide valid inputs.")
                                                    ])
def test_empty_inputs(price, discount, result):

    """After submitting empty inputs, tests whether a message requesting valid inputs is raised."""

    assert discount_calc(price, discount) == result

