class Product:
    def __init__(self, name, u_p, g_p, quantity):
        self.name = name
        self.u_p = u_p
        self.g_p = g_p
        self.quantity = quantity

    def total_price(self):
        base_price = self.u_p + (self.u_p * self.g_p / 100)
        total_price = base_price * self.quantity

        if self.u_p > 500:
            total_price *= 0.95

        return total_price

def max_GST(basket):
    max_gst_product = max(basket, key=lambda x: x.u_p * x.g_p * x.quantity / 100)
    return max_gst_product

def total_AMT(basket):
    total_amount = sum(product.total_price() for product in basket)
    return total_amount

max_gst_product = max_GST(basket)
print(f"Max GST amt product is: {max_gst_product.name}")

total_amount = total_AMT(basket)
print(f"Total amount = Rs. {total_amount}")
