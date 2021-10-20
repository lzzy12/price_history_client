import json


class ProductPrice:
    """Stores the price of a product at a given time"""
    def __init__(self, date, price: float):
        self.date = date
        self.price = price


class ProductDetails:
    """Stores name, current price, lowest price, highest price and history of the prices of the product"""
    def __init__(self, uid, name, current_price, lowest_price, highest_price, store,most_frequent_price,average_price):
        self.id = uid
        self.name = name
        self.current_price = current_price
        self.lowest_price = lowest_price
        self.highest_price = highest_price
        self.store = store
        self.most_frequent_price=most_frequent_price
        self.average_price=average_price

    @staticmethod
    def fromJson(jsonData):
        data = json.loads(jsonData)["effects"]["emits"][0]["params"][0]
        prices={}
        sum=0
        temp_data=json.loads(data["data"])
        max,maxPoint=1,temp_data[0][1]
        for i in temp_data:
            if i[1] in prices:
                prices[i[1]]+=1
            else:
                prices[i[1]]=1
            if prices[i[1]]>max:
                max,maxPoint=prices[i[1]],i[1]
            sum+=i[1]
        avg=round(sum/len(temp_data),2)
        return ProductDetails(data["id"], data["title"], data["curr_price"], data["low_price"], data["high_price"], data["store"],maxPoint,avg)
