import json


"""DB HAS 10 PROGRAMS"""


class Database():

	def __init__(self):

		self.data = {

	"prog1":{
	"baudrate":9600,
	"port":'COM4',
	"speed":"020",
	"step":10,
	"stare": 0 ,
	"home":[70,100,110,90,10,157] ,
	"point1":[0,0,0,0,0,0],
	"point2":[0,0,0,0,0,0],
	"point3":[0,0,0,0,0,0],
	"point4":[0,0,0,0,0,0],
	"point5":[0,0,0,0,0,0],
	"point6":[0,0,0,0,0,0],
	"point7":[0,0,0,0,0,0],
	"point8":[0,0,0,0,0,0],
	"point9":[0,0,0,0,0,0],
	"point10":[0,0,0,0,0,0],	
	"lsup":[300,120,210,220,270,220],
	"linf":[20,20,90,60,20,160],
	"program":[2, 9, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
	},

	"prog2":{
	"baudrate":9600,
	"port":'COM4',
	"speed":"020",
	"step":10,
	"stare": 0 ,
	"home":[70,100,110,90,10,157] ,
	"point1":[0,0,0,0,0,0],
	"point2":[0,0,0,0,0,0],
	"point3":[0,0,0,0,0,0],
	"point4":[0,0,0,0,0,0],
	"point5":[0,0,0,0,0,0],
	"point6":[0,0,0,0,0,0],
	"point7":[0,0,0,0,0,0],
	"point8":[0,0,0,0,0,0],
	"point9":[0,0,0,0,0,0],
	"point10":[0,0,0,0,0,0],	
	"lsup":[300,120,210,220,270,220],
	"linf":[20,20,90,60,20,160],
	"program":[2, 9, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
	},


	"prog3":{
	"baudrate":9600,
	"port":'COM4',
	"speed":"020",
	"step":10,
	"stare": 0 ,
	"home":[70,100,110,90,10,157] ,
	"point1":[0,0,0,0,0,0],
	"point2":[0,0,0,0,0,0],
	"point3":[0,0,0,0,0,0],
	"point4":[0,0,0,0,0,0],
	"point5":[0,0,0,0,0,0],
	"point6":[0,0,0,0,0,0],
	"point7":[0,0,0,0,0,0],
	"point8":[0,0,0,0,0,0],
	"point9":[0,0,0,0,0,0],
	"point10":[0,0,0,0,0,0],	
	"lsup":[300,120,210,220,270,220],
	"linf":[20,20,90,60,20,160],
	"program":[2, 9, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
	},

	"prog4":{
	"baudrate":9600,
	"port":'COM4',
	"speed":"020",
	"step":10,
	"stare": 0 ,
	"home":[70,100,110,90,10,157] ,
	"point1":[0,0,0,0,0,0],
	"point2":[0,0,0,0,0,0],
	"point3":[0,0,0,0,0,0],
	"point4":[0,0,0,0,0,0],
	"point5":[0,0,0,0,0,0],
	"point6":[0,0,0,0,0,0],
	"point7":[0,0,0,0,0,0],
	"point8":[0,0,0,0,0,0],
	"point9":[0,0,0,0,0,0],
	"point10":[0,0,0,0,0,0],	
	"lsup":[300,120,210,220,270,220],
	"linf":[20,20,90,60,20,160],
	"program":[2, 9, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
	},

	"prog5":{
	"baudrate":9600,
	"port":'COM4',
	"speed":"020",
	"step":10,
	"stare": 0 ,
	"home":[70,100,110,90,10,157] ,
	"point1":[0,0,0,0,0,0],
	"point2":[0,0,0,0,0,0],
	"point3":[0,0,0,0,0,0],
	"point4":[0,0,0,0,0,0],
	"point5":[0,0,0,0,0,0],
	"point6":[0,0,0,0,0,0],
	"point7":[0,0,0,0,0,0],
	"point8":[0,0,0,0,0,0],
	"point9":[0,0,0,0,0,0],
	"point10":[0,0,0,0,0,0],	
	"lsup":[300,120,210,220,270,220],
	"linf":[20,20,90,60,20,160],
	"program":[2, 9, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
	},

	"prog6":{
	"baudrate":9600,
	"port":'COM4',
	"speed":"020",
	"step":10,
	"stare": 0 ,
	"home":[70,100,110,90,10,157] ,
	"point1":[0,0,0,0,0,0],
	"point2":[0,0,0,0,0,0],
	"point3":[0,0,0,0,0,0],
	"point4":[0,0,0,0,0,0],
	"point5":[0,0,0,0,0,0],
	"point6":[0,0,0,0,0,0],
	"point7":[0,0,0,0,0,0],
	"point8":[0,0,0,0,0,0],
	"point9":[0,0,0,0,0,0],
	"point10":[0,0,0,0,0,0],	
	"lsup":[300,120,210,220,270,220],
	"linf":[20,20,90,60,20,160],
	"program":[2, 9, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
	},

	"prog7":{
	"baudrate":9600,
	"port":'COM4',
	"speed":"020",
	"step":10,
	"stare": 0 ,
	"home":[70,100,110,90,10,157] ,
	"point1":[0,0,0,0,0,0],
	"point2":[0,0,0,0,0,0],
	"point3":[0,0,0,0,0,0],
	"point4":[0,0,0,0,0,0],
	"point5":[0,0,0,0,0,0],
	"point6":[0,0,0,0,0,0],
	"point7":[0,0,0,0,0,0],
	"point8":[0,0,0,0,0,0],
	"point9":[0,0,0,0,0,0],
	"point10":[0,0,0,0,0,0],	
	"lsup":[300,120,210,220,270,220],
	"linf":[20,20,90,60,20,160],
	"program":[2, 9, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
	},

	"prog8":{
	"baudrate":9600,
	"port":'COM4',
	"speed":"020",
	"step":10,
	"stare": 0 ,
	"home":[70,100,110,90,10,157] ,
	"point1":[0,0,0,0,0,0],
	"point2":[0,0,0,0,0,0],
	"point3":[0,0,0,0,0,0],
	"point4":[0,0,0,0,0,0],
	"point5":[0,0,0,0,0,0],
	"point6":[0,0,0,0,0,0],
	"point7":[0,0,0,0,0,0],
	"point8":[0,0,0,0,0,0],
	"point9":[0,0,0,0,0,0],
	"point10":[0,0,0,0,0,0],	
	"lsup":[300,120,210,220,270,220],
	"linf":[20,20,90,60,20,160],
	"program":[2, 9, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
	},

	"prog9":{
	"baudrate":9600,
	"port":'COM4',
	"speed":"020",
	"step":10,
	"stare": 0 ,
	"home":[70,100,110,90,10,157] ,
	"point1":[0,0,0,0,0,0],
	"point2":[0,0,0,0,0,0],
	"point3":[0,0,0,0,0,0],
	"point4":[0,0,0,0,0,0],
	"point5":[0,0,0,0,0,0],
	"point6":[0,0,0,0,0,0],
	"point7":[0,0,0,0,0,0],
	"point8":[0,0,0,0,0,0],
	"point9":[0,0,0,0,0,0],
	"point10":[0,0,0,0,0,0],	
	"lsup":[300,120,210,220,270,220],
	"linf":[20,20,90,60,20,160],
	"program":[2, 9, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
	},

	"prog10":{
	"baudrate":9600,
	"port":'COM4',
	"speed":"020",
	"step":10,
	"stare": 0 ,
	"home":[70,100,110,90,10,157] ,
	"point1":[0,0,0,0,0,0],
	"point2":[0,0,0,0,0,0],
	"point3":[0,0,0,0,0,0],
	"point4":[0,0,0,0,0,0],
	"point5":[0,0,0,0,0,0],
	"point6":[0,0,0,0,0,0],
	"point7":[0,0,0,0,0,0],
	"point8":[0,0,0,0,0,0],
	"point9":[0,0,0,0,0,0],
	"point10":[0,0,0,0,0,0],	
	"lsup":[300,120,210,220,270,220],
	"linf":[20,20,90,60,20,160],
	"program":[2, 9, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
	}
	}

	def initializare(self):
		with open("database.json", "w") as write_file:
			json.dump(self.data, write_file)



	def show_db(self):
		try:
			with open("database.json", "r") as read_file:
				response=json.load(read_file)
			return response 
		except:
			return 0

def rdata(skey):
	try:
		with open("database.json", "r") as read_file:
			response=json.load(read_file)
			response=response[skey]
			return response

	except:
		return 0 


def wdata(skey,svalue):
	with open("database.json", "r") as read_file:
		data=json.load(read_file)
	for i in data.keys():		
		if i==skey :
			data[i]=svalue 
			break
	with open("database.json", "w") as write_file:
		json.dump(data, write_file)

	






DB=Database()
DB.initializare()
