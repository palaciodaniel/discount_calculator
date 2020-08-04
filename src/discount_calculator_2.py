def discount_calc(price, discount: int) -> str:

    """
    Calculates the final price you'll pay using a discount. 

    Args:
        price: (int/float) The original price. If int, it will be transformed into a float.
        discount: (int) The discount value. If float, decimal values will be ignored.

    Returns:
        result: (str) A sentence indicating either the discounted price or 
    """
    
    price = float(price)
    price = abs(round(price, 2))

    discount = int(discount)
    discount = abs(discount)

    # Addressing wrong input types    

    if (type(price) != float):
        result = "ERROR: Entered values must be numbers."
        return result

    elif type(discount) != int:
        result = "ERROR: For percentages only integer values are accepted."
        return result

    # Addressing wrong input values

    if discount > 100 or discount < 0:
        result = "ERROR: Choose a discount between 0 and 100."
        return result

    # Addressing special cases

    elif (price == 0) or (discount == 100):
        result = "RESULT: This item appears to be currently free!"
        return result

    elif discount == 0:
        result = "RESULT: The item doesn't have a discount."
        return result    

    # Normal output
            
    else:
        disc = (price * discount) / 100
        total = price - disc
        result = "RESULT: The discounted price is ${0:.2f}!".format(total)
        return result
