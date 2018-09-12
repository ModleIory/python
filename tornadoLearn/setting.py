from tornado import web
from tornado import httpserver
from tornado import ioloop
from tornado import options
import conf

class MainHandler(web.RequestHandler):
	def initialize(self,words):
		self.words = words
	def get(self):
		self.write("Ok I am setting test and words is {}".format(self.words))


def main():
	# the router give the value , debug true and 
	return web.Application([
		(r'/',MainHandler,{"words":"You are good"})
	],**conf.setting)

if __name__ == "__main__":
	app = main()
	httpserver = httpserver.HTTPServer(app)
	httpserver.listen(8777)
	print("running....")
	ioloop.IOLoop.current().start()