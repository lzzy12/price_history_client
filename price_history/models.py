import json


class ProductPrice:
    """Stores the price of a product at a given time"""

    def __init__(self, date, price: float):
        self.date = date
        self.price = price


class ProductDetails:
    """Stores name, current price, lowest price, highest price and history of the prices of the product"""

    def __init__(self, uid, name, current_price, lowest_price, highest_price, average_price, store, image):
        self.id = uid
        self.name = name
        self.current_price = current_price
        self.lowest_price = lowest_price
        self.highest_price = highest_price
        self.average_price = average_price
        self.store = store
        self.image = image

    @staticmethod
    def fromJson(jsonData):
        data = json.loads(jsonData)["effects"]["emits"][0]["params"][0]
        return ProductDetails(data["id"], data["title"], data["curr_price"], data["low_price"], data["high_price"],
                              data["avg_price"], data["store"], data['image'])
