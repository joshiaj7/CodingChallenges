import uuid 

"""
Space	: O(n)
Time	: O(1)
"""

class Codec:
    def __init__(self) -> None:
        self.hashmap = {}
    
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        new_id = uuid.uuid4().hex[:6]
        self.hashmap[new_id] = longUrl
        return "http://tinyurl.com/" + new_id
        
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        url_id = shortUrl[19:]
        return self.hashmap[url_id]
