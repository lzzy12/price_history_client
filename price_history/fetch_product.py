import re
import requests
import json
from .models import ProductDetails
from .exceptions import ApiError


def fetch_product(product_url: str) -> ProductDetails:
    """
    :param product_url: URL of the product
    :return: Details of the product fetched
    """
    session = requests.session()
    HOMEPAGE = 'https://pricehistory.in/'
    session.headers.update(
        {'User-Agent': 'Mozilla/5.0 (Windows NT '
                       '10.0; Win64; x64) '
                       'AppleWebKit/537.36 (KHTML, '
                       'like Gecko) '
                       'Chrome/90.0.4430.93 '
                       'Safari/537.36',
         }
    )
    HomePageData = session.get(HOMEPAGE)

    CSRF = re.search('csrf-token" content="(.*)\"', HomePageData.text).group(1)
    dataId = re.search(':id="(.*?)"', HomePageData.text).group(1)
    htmlHash = re.search('htmlHash&quot;:&quot;(.*?)&', HomePageData.text).group(1)
    checksum = re.search('checksum&quot;:&quot;(.*?)&', HomePageData.text).group(1)

    session.headers.update({
        'x-csrf-token': CSRF,
        'content-type': 'application/json',
    })
    # product_url = "https://www.amazon.in/HP-K300-Gaming-Keyboard-4QM95AA/dp/B08497X176/"
    pageData = {
        "fingerprint": {
            "id": f"{dataId}",
            "name": "pricehistory",
            "locale": "en"
        },
        "serverMemo": {
            "children": [],
            "errors": [],
            "htmlHash": f"{htmlHash}",
            "data": {
                "url": None
            },
            "dataMeta": [],
            "checksum": f"{checksum}"
        },
        "updates": [
            {
                "type": "syncInput",
                "payload": {
                    "name": "url",
                    "value": product_url
                }
            },
            {
                "type": "callMethod",
                "payload": {
                    "method": "checkPriceHistory",
                    "params": []
                }
            }
        ]
    }
    r = session.post('https://pricehistory.in/livewire/message/pricehistory', data=json.dumps(pageData))
    if r.status_code != 200:
        raise ApiError(r.text)
    return ProductDetails.fromJson(r.text)
