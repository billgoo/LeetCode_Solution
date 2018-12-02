class Codec:

    def __init__(self):
        # hash table
        self.map_verify = dict()
        self.map_decode = dict()
        
    
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if not (longUrl in self.map_verify):
            shortUrl = ''.join(random.sample(string.ascii_letters + string.digits, 6))
            while shortUrl in self.map_decode:
                shortUrl = ''.join(random.sample(string.ascii_letters + string.digits, 6))
            self.map_verify[longUrl] = shortUrl
            self.map_decode[shortUrl] = longUrl
        else:
            shortUrl = map_verify[longUrl]
        return "http://tinyurl.com/" + shortUrl
    

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.map_decode[shortUrl.split('/')[-1]]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))