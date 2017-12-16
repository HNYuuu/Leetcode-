# 这道题就是自定义一种编解码方式，使得一个长URL可以被转换为短URL

# 我用了一个类变量 charset 来定义字符集，所有的数字和大小写字幕，
# 维护两个类变量：映射以及目前编解码了几个网址。每当有URL要求编码时
# 都会查找其是否在映射中，如果在直接返回；否则添加进映射中返回新的
# 短URL。

# 这道题没有什么难度，一道典型的应用题。但是我这个做法还有很大的优化
# 空间。


class Codec:

    jection ={}
    charset = '+0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    count = 1

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if longUrl in self.__class__.jection.values():
            for i in self.__class__.jection.keys():
                if self.__class__.jection[i] == longUrl:
                    shortUrl = i
        else:            
            result = []
            tempCount = self.__class__.count
            while tempCount != 0:
                remainder = tempCount % 62
                if remainder == 0:
                    result.insert(0, 'Z')
                else:
                    result.insert(0, self.__class__.charset[remainder])
                tempCount = tempCount // 62
            self.__class__.count += 1
            shortUrl = "".join(result)
            self.__class__.jection[shortUrl] = longUrl

        return 'http://tinyurl/' + shortUrl

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        shortUrl = shortUrl[15:]
        return self.__class__.jection[shortUrl]
        

# Your Codec object will be instantiated and called as such:
codec = Codec()
print(codec.encode('https://www.baidu.com'))
print(codec.encode('https://www.google.com'))
print(codec.decode(codec.encode('http://www.amazon.cn')))
# codec.decode(codec.encode(url))