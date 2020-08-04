import pytest
from discount_calculator_2 import discount_calc

class TestDiscountCalc(object):

    # Testing for good arguments

    def test_general_correct_examples(self):
        assert discount_calc(52, 20) == "RESULT: The discounted price is $41.60!"
        assert discount_calc(243.9685, 35) == "RESULT: The discounted price is $158.58!"
        
    # Testing for bad arguments
      
    def test_discount_gt_100(self):
        assert discount_calc(53485, 101) == "ERROR: Choose a discount between 0 and 100." 
        assert discount_calc(3400, 150) == "ERROR: Choose a discount between 0 and 100." 

    def test_discount_lt_0(self):
        assert discount_calc(21.5, -40) == "RESULT: The discounted price is $12.90!"
        assert discount_calc(21.5, -100) == "RESULT: This item appears to be currently free!"

    def test_discount_float(self):
        assert discount_calc(20, 25.5) == "RESULT: The discounted price is $15.00!"
        assert discount_calc(20, -0.2) == "RESULT: The item doesn't have a discount."

    def test_price_lt_0(self):
        assert discount_calc(-24000, 15) == "RESULT: The discounted price is $20400.00!"

    def test_wrong_input_string(self):

        """Tests if an error is raised if the arguments are strings."""   

        with pytest.raises(ValueError):
            discount_calc("Twenty", 0)

        with pytest.raises(ValueError):
            discount_calc(345, "Fourteen")

    def test_wrong_input_list(self):
        
        """Tests if an error is raised if the arguments are lists."""           
        
        with pytest.raises(TypeError):
            discount_calc(23, [0, 92, 23])
        
        with pytest.raises(TypeError):
            discount_calc([0, 92, 23], 23)

    def test_wrong_input_missing_arg(self):

        """Tests if an error is raised if the second argument is missing."""

        with pytest.raises(TypeError):
            discount_calc(345)
                
    # Testing for special arguments

    def test_discount_eq_0(self):
        assert discount_calc(3500, 0) == "RESULT: The item doesn't have a discount."
        assert discount_calc(25.50, 0) == "RESULT: The item doesn't have a discount."

    def test_discount_eq_100(self):
        assert discount_calc(17, 100) == "RESULT: This item appears to be currently free!"
        assert discount_calc(0, 100) == "RESULT: This item appears to be currently free!"

    def test_price_eq_0(self):
        assert discount_calc(0, 50) == "RESULT: This item appears to be currently free!"
        assert discount_calc(0, 0) == "RESULT: This item appears to be currently free!"
        assert discount_calc(0, 100) == "RESULT: This item appears to be currently free!"

