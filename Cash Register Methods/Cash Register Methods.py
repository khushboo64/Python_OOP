class CashRegister:

    Tax = 0.05

   

    def __init__(self, cashier):

        self.cashier = cashier

        self.products = {}

   

    def add_product(self,product,quantity=1):

        self.products[product["name"]] = {"price" : product["price"], "quantity" : quantity}

       

    def show_products(self):

        print("all products", self.products)

   

    def remove_product(self, product):

        del self.products[product]

   

    def update_price(self, product, new_price):

        self.products[product]["price"] = new_price

   

    def sub_total(self):

        sub_total = 0

        for product_info in self.products.values():

            sub_total += product_info["price"] * product_info["quantity"]

        return sub_total


    def print_sub_total(self):

        print(self.sub_total())

       

    def taxes(self):

        return round(self.sub_total() + CashRegister.Tax, 2)

       

       

    def print_taxes(self):

        print(f"taxes = {self.taxes()}")

       

    def total_amount(self):

        total = round(self.sub_total() + self.taxes() , 2)

        return total

   

    def print_total_amount(self):

        print(f"total amount = {self.total_amount()}")

   

   

    def clear(self):

        self.products.clear()

       


Purchase_1 = CashRegister("Alex")


product1 = {"name": "Pizza", "price": 6.15}

product2 = {"name": "coke", "price": 3.54}

product3 = {"name": "pasta", "price": 8.95}


Purchase_1.add_product(product1, 2)

Purchase_1.add_product(product2)

Purchase_1.add_product(product3, 10)

Purchase_1.show_products()

Purchase_1.remove_product("pasta")

Purchase_1.show_products()

Purchase_1.update_price("Pizza",10)

Purchase_1.show_products()

Purchase_1.print_taxes()

Purchase_1.print_total_amount()

Purchase_1.clear()

Purchase_1.show_products()