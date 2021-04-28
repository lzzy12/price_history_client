import json


class ProductPrice:
    """Stores the price of a product at a given time"""

    def __init__(self, date, price: float):
        self.date = date
        self.price = price


class ProductDetails:
    """Stores name, current price, lowest price, highest price and history of the prices of the product"""

    def __init__(self, uid, name, current_price, lowest_price, highest_price, average_price, store, image, stock):
        self.id = uid
        self.name = name
        self.current_price = current_price
        self.lowest_price = lowest_price
        self.highest_price = highest_price
        self.average_price = average_price
        self.store = store
        self.image = image
        self.inStock = stock
    @staticmethod
    def __convert_price(price: str) -> float:
        return float(price.replace(',', ''))

    @staticmethod
    def fromJson(jsonData):
        data = json.loads(jsonData)["effects"]["emits"][0]["params"][0]

        return ProductDetails(data["id"], data["title"], ProductDetails.__convert_price(data["curr_price"]),
                              ProductDetails.__convert_price(data["low_price"]),
                              ProductDetails.__convert_price(data["high_price"]),
                              ProductDetails.__convert_price(data["avg_price"]), data["store"], data['image'], True if data['stock'] == 1 else False)
