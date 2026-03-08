import redis
import json
from app.config import REDIS_HOST, REDIS_PORT

r = redis.Redis(
host=REDIS_HOST,
port=REDIS_PORT
)

def cache_product(product):

    r.set(product.id,json.dumps({
        "id":product.id,
        "name":product.name,
        "price":product.price
    }))

def get_cached_product(product_id):

    data = r.get(product_id)

    if data:

        return json.loads(data)

    return None