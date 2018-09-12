from tornado import web
import tornado.ioloop as ioloop
from tornado import httpserver

class IndexHandler(web.RequestHandler):
	def get(self):
		self.write("Hello http server")

if __name__ == "__main__":
	app = web.Application([
		(r"/",IndexHandler)
	])
	#这个是创建一个服务，实际是index中的app.listen的一种详细版本吧
	http_server = httpserver.HTTPServer(app)
	http_server.listen(8777)
	#多个进程 
	'''
	#在linux上方可
	http_server.bind(8777)
	http_server.start(0)
	'''
	ioloop.IOLoop.current().start()