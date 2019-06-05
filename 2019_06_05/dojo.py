def is_http(url):
	return url.startswith("http://")

def is_https(url):
	return url.startswith("https://")

class Url(object):
	def __init__(self, url):
		self.url = url

	@property
	def protocol(self):
		return self.url.split(":")[0]

	@property
	def domain(self):
		domain = self.url.split("/")[2]
		if "@" in self.url:
			domain = self.url.split("@")[1]
		return domain.split("/")[0]

	@property
	def user(self):
		return "user"