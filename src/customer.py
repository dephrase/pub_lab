class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = 0

    def buy_drink(self, drink, pub):
        if self.age >= 18 and self.drunkenness <= 10:
            pub.till += drink.price
            self.wallet -= drink.price
            self.drunkenness += drink.alcohol_level
            return "Enjoy!"
        else:
            return "Do one!"
        

        
