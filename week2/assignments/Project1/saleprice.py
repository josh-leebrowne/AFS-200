productPrompt = "Please enter product description: "
quantityPrompt = "Please enter quantity: "

product = input(productPrompt)
quantity = int(input(quantityPrompt))
print(f"Your order: {quantity} {product}")

pricePrompt = "Please enter product price: "
productPrice = float(input(pricePrompt))
totalPrice = productPrice * quantity
salesTax = .065

if totalPrice > 39.99:
    print("You are eligible for a 25 percent discount ")
    print("Your orginal order price was ${:,.2f}".format(totalPrice))

    discount = totalPrice*.25
    discountedPrice = totalPrice - discount
    tax = discountedPrice * salesTax
    finalPrice = discountedPrice + tax

    print("Your new order price is ${:,.2f}".format(finalPrice))
    print("Your total savings is ${:,.2f}".format(discount))
elif totalPrice > 19.99:
    print("You are eligible for a 15 percent discount ")
    print("Your orginal order price was ${:.2f}".format(totalPrice))

    discount = totalPrice*.15
    discountedPrice = totalPrice - discount
    tax = discountedPrice * salesTax
    finalPrice = discountedPrice + tax

    print("Your new order price is ${:.2f}".format(finalPrice))
    print("Your total savings is ${:,.2f}".format(discount))
else:
    print("You do not qualify for a discount.")

    tax = totalPrice * salesTax
    finalPrice = totalPrice + tax

    print("Your order total is ${:.2f}".format(finalPrice))



