def discount_calc(price, discount):

    """
    Calculates the final price you'll pay if you use a discount. 

    Args:
        price: (int/float) The original price. No matter the input, it will always be transformed to a float with two decimals.
        discount: (int/float) The discount value. If it's a float, decimal values will be rounded into an integer.

    Returns:
        result: (str) A sentence that indicates the discounted price. 
    """
    
    try:

        price = float(price.replace(",", "."))
        price = round(price, 2)

        discount = float(discount.replace(",", "."))
        discount = round(discount, 0)

        # Addressing wrong inputs

        if price < 0:
            return "ERROR: Price cannot be a negative number."

        elif discount > 100 or discount < 0:
            return "ERROR: Choose a discount between 0 and 100."

        # Addressing special cases

        elif (price == 0) or (discount == 100):
            return "RESULT: This item is currently free!"

        elif discount == 0:
            return "RESULT: This item doesn't have a discount."

        # Correct output

        else:
            disc = (price * discount) / 100
            total = round(price - disc, 2)
            return "RESULT: The discounted price is ${:.2f}!".format(total)

    except ValueError:
        return "ERROR: Please provide valid inputs."

    except Exception as e:
        return e
