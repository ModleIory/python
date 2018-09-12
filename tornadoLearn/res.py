from tornado import web
from tornado import ioloop
from tornado import httpserver
from tornado import options
import os

class IndexHandler(web.RequestHandler):
	def get(self):
		# 直接渲染到模板就行了
		self.render('res.html') 

class RequestHandler(web.RequestHandler):
	def get(self):
		name = self.get_query_argument("name",strip=True)
		goal = self.get_query_argument("goal",strip=True)
		self.write("This is get methods,name is {} and goal is {}".format(name,goal))
	def post(self):
		name = self.get_body_argument("name",strip=True)
		goal = self.get_body_argument("goal",strip=True)
		self.write("This is post methods,name is {name} and goal is {goal}".format(name=name,goal=goal))

if __name__ == "__main__":
	app = web.Application([
		(r'/',IndexHandler),
		(r'/deal',RequestHandler)
	],
		template_path=os.path.join(os.path.dirname(__file__),'tpl'),
		debug=True
	)
	httpserver = httpserver.HTTPServer(app)
	httpserver.listen(8777)
	ioloop.IOLoop.current().start()

