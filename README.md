Usage:

```python
from price_history import fetch_product
product = fetch_product.fetch_product("https://www.amazon.in/Ant-Esports-KM500W-Ergonomic-Programmable/dp/B081Q8PSKC/ref=sr_1_1?dchild=1&keywords=KM500w&qid=1619613615&smid=A14CZOWI0VEHLG&sr=8-1")
```

`fetch_product` function returns an instance of `ProductDetails`

###### ProductDetails
**id**: A unique ID of the product generated by the rest API

**name**: Name of the product

**current_price**: Current price of the product

**lowest_price**: Lowest price of the product

**highest_price**: Highest price of the product

**average_price**: Average price of the product

**store**: Store name

**image**: Image of the product

