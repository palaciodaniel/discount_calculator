# Do you want to know if that discount is a good one? Find out with this function!

def discount_calc(price, discount):
    """
    This function will help you determine the final price you'll pay using a discount. For the positional argument 'price' enter the original price, and for 'discount' just add an integer (without the '%' sign, of course!).
    """
    if discount == 100:
        print("RESULT: This item is free for a limited time! Go get it now!")
    elif discount > 100 or discount < 0:
        print("ERROR: Choose a discount between 0 and 100.")
    elif discount == 0:
        print("RESULT: The item doesn't have a discount.")
    elif price == 0:
        print("RESULT: This item is free! Go get it now!")
    else:
        disc = (abs(price) * discount) / 100
        total = abs(price) - abs(disc)
        print("RESULT: The discounted price is $", total, "!")

# --------------------------------------------------------------------------------------------------------------------------
    
print("Let's try the function with some examples:")
print("\n")

print("1) A toaster worth USD 52 with a 20% discount:")

discount_calc(52, 20)

# --------------------------------------------------------------------------------------------------------------------------

print("\n")

print("2) A fridge worth ARS 24000 with a 15% discount:")
print("(Yes! You can use any currency!)")

discount_calc(-24000, 15)

# --------------------------------------------------------------------------------------------------------------------------

print("\n")

print("3) A movie ticket worth AUD 21.50 with a 40% discount:")
print("""(Yes! Cents are also accepted! Just use 
a dot (.) to separate the decimals!)""")

discount_calc(21.5, 40)

# --------------------------------------------------------------------------------------------------------------------------

print("\n")

print("4) A Steam game worth USD 17, with a 100% discount for limited time:")
discount_calc(17, 100)
