import requests
 
#url = 'http://www.google.com'
url = 'https://domain.com/dir/index.php?q=example'
 
r = requests.get(url, timeout=6)
respTime = r.elapsed.microseconds/1000/1000
print("response time = " + str(respTime))