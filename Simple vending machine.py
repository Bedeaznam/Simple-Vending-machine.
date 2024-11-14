class Machine:
    def __init__(self):

        self.languages = {
            "en": "Welcome",
            "bg": "Добре дошли!",
        }

        self.codes = {
            "coke": {"small": 14, "medium": 17, "large": 20},
            "cappy": {"small": 19, "medium": 18, "large": 22},
            "fantastic": {"small": 23, "medium": 24, "large": 25},
            "fanta lemon": {"small": 26, "medium": 27, "large": 28}
        }

        self.prices = {
            "coke": {"small": 1.00, "medium": 1.50, "large": 2.00},
            "cappy": {"small": 1.00, "medium": 1.50, "large": 2.00},
            "fantastic": {"small": 1.00, "medium": 1.50, "large": 2.00},
            "fanta lemon": {"small": 1.00, "medium": 1.50, "large": 2.00}

        }

    def select_product(self):
        coins = float(input("How many coins do you have? "))

        code = int(input("Enter the product code: "))

        # Намери продукт и размер по даден код
        selected_product = None
        selected_size = None
        for product, sizes in self.codes.items():
            for size, product_code in sizes.items():
                if product_code == code:
                    selected_product = product
                    selected_size = size
                    break
            if selected_product:
                break

        if selected_product:
            price = self.prices[selected_product][selected_size]
            if coins >= price:
                change = coins - price
                print(f"Take your {selected_product} ({selected_size})!")
                print(f"Your change: {change:.2f} coins")
            else:
                print("Not enough money.")
                print(f"Required: {price:.2f}, inserted: {coins:.2f}")
        else:
            print("Invalid product code.")

        def select_language(self, lang_code):
            message = self.languages.get(lang_code, self.languages["en"])
            print(message)