import hashlib
from django.utils.text import slugify
import datetime

POST_SLUG_HASH_DIGEST_LENGTH = 12

def slug_and_hash_post_title(post_title, user_id):
    
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    item_slug = slugify(post_title)
    hashing_item = f"{post_title}-{user_id}-{current_time}"
    hash_object = hashlib.shake_256(hashing_item.encode("utf-8"))
    item_hash = hash_object.hexdigest(POST_SLUG_HASH_DIGEST_LENGTH // 2)
    
    slug_and_hash = f"{item_slug}-{item_hash}"
    return slug_and_hash