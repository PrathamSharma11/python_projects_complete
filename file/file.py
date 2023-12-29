# a = open("file/sample.txt",'r')
# b = a.read()
# #b = a.read(3)

# print(b)
# a.close

lst = []
a = ['114.119.130.92 - - [24/Jun/2021:06:49:15 +0530] "GET /con/con/src/src/html/assets/_con/images/ecommerce-apple-ipad-air-30x30.jpg HTTP/1.1" 404 397 "-" "Mozilla/5.0 (Linux; Android 7.0;) AppleWebKit/537.36 (KHTML, like Gecko) Mobile Safari/537.36 (compatible; PetalBot;+https://webmaster.petalsearch.com/site/petalbot)"',
     '114.119.142.3 - - [24/Jun/2021:07:00:57 +0530] "GET /con/con/src/src/html/assets/_con/images/ecommerce-apple-mac-pro-30x30.jpg HTTP/1.1" 404 397 "-" "Mozilla/5.0 (Linux; Android 7.0;) AppleWebKit/537.36 (KHTML, like Gecko) Mobile Safari/537.36 (compatible; PetalBot;+https://webmaster.petalsearch.com/site/petalbot)"']

# chunks = [a[x:x+1] for x in range(0, len(a), 1)]
# print(chunks)


for i in range(0, len(a), 8):
    chunk = a[i:i + 8]
    print(chunk)






