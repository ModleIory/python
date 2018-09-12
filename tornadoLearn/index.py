import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("Hello world!")

class SecondHandler(tornado.web.RequestHandler):
	def get(self,type_id):
		print(self)
		self.write("Second try!!! And type id is {}".format(type_id))

def make_app():
	return tornado.web.Application([
		(r"/",MainHandler),
		(r"/second/([0-9]+)",SecondHandler)
	])

if __name__ == "__main__":
	app = make_app()
	app.listen(8888)
	tornado.ioloop.IOLoop.current().start()