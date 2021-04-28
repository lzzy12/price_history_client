Installation:

# Method 1

Download the latest whl file from https://github.com/lzzy12/price_history_client/releases

Open command prompt/terminal and make sure you are in the same directory where you downloaded the release file

Then run:
 ```shell script
 pip install price_history*.whl
 ```


# Method 2: Install from git

Run:
```shell script
    pip install git+https://github.com/lzzy12/price_history_client.git
```

# Usage:

```python
from price_history import fetch_product
product = fetch_product.fetch_product("https://www.amazon.in/Ant-Esports-KM500W-Ergonomic-Programmable/dp/B081Q8PSKC/ref=sr_1_1?dchild=1&keywords=KM500w&qid=1619613615&smid=A14CZOWI0VEHLG&sr=8-1")
```

`fetch_product` function returns an instance of `ProductDetails`

####**ProductDetails**
 
**id**: A unique ID of the product generated by the rest API

**name**: Name of the product

**current_price**: Current price of the product

**lowest_price**: Lowest price of the product

**highest_price**: Highest price of the product

**average_price**: Average price of the product

**store**: Store name

**image**: URL of image of the product

**inStock**: Whether the product is in stock or not
