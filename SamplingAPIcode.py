import requests
import re
import html 



headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

url = "http://welcomesignup.com/2065"

#url = "http://www.vabenefits.co/Xxxxxxx74"

#url = "http://firozhossainchaudhuri8451.purltest.com/"

response = requests.request('GET', url)

pattern = r'<iframe(.*)src="(.*)"></iframe>'

match = re.findall(pattern, response.text)

iframe_url = html.unescape(match[0][1])

rresponse = requests.request('GET', iframe_url, headers=headers)

response_string = rresponse.text

if 'INVALID OR MISTYPED URL' in response_string:
	print("Purl Does Not Exist!")
else:
	print("Purl Exists!")



