from flask import Flask,request
from flask_restful import Resource, Api
import sys,time,random,requests,threading

app = Flask(__name__)
api = Api(app)

count = 0
message = ""
infected = False

class GossipNode(Resource):

	def get(self):
		global count
		return {"count":count}

	def post(self):
		global message
		global infected
		
		print(request.json)
		message = request.json
		
		if(infected == False):
			infected = True
			pollThread = threading.Thread(target=gossip,name = "Polling Thread")
			pollThread.daemon = True
			pollThread.start()
		
		print(time.time())
		return "",201
		
def gossip():
	while True:#message['time']>time.time():
		global message
		print('while')
		port = random.randint(1,21)
		time.sleep(1)
		try:
			requests.post(url = "http://localhost:" + str(port) +"/api",json = message)
		except Exception as e:
			pass
			

api.add_resource(GossipNode, '/api')

if __name__ == '__main__':
	app.run(port=int(5000),debug=False)
	
