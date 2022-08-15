applePrice = .50
userPrompt = "Please state your name: "
applePrompt = "How many apples would you like to buy?: "
thankYou = "Thank your for your purchase."
username = input(userPrompt)
print(username)

applePurchase = input(applePrompt)
print(f"Thank You {username} for your purchase of {applePurchase} Apples at {(applePrice):,.2f} each.")

