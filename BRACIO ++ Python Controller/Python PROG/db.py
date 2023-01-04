import json


"""DB HAS 10 PROGRAMS"""


class Database():

	'''DATABASE MANIPULATION CLASS'''

	def __init__(self):

		self.data = {

	"program":"prog1",	
	"stare": 0 ,

	"prog1":{
	"baudrate":9600,
	"port":'COM4',
	"speed":"020",
	"step":10,
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


	"dummy":{
	"baudrate":9600,
	"port":'COM4',
	"speed":"020",
	"step":10,
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


	def rprogram(self):
		try:
			with open("database.json", "r") as read_file:
				response=json.load(read_file)
				response=response["program"]
				return response
		except:
			return 0


	def wprogram(self,svalue):
		programs=["prog1","prog2","prog3","prog4","prog5","prog6","prog7","prog8","prog9","prog9","prog10"]
		with open("database.json", "r") as read_file:
			data=json.load(read_file)	
			if (svalue in programs)  :
				data["program"]=svalue 
		with open("database.json", "w") as write_file:
			json.dump(data, write_file)
 

	def rmod(self):
		try:
			with open("database.json", "r") as read_file:
				response=json.load(read_file)
				response=response["stare"]
				return response
		except:
			return 0


	def wmod(self,svalue):
		stari=[0,1]
		with open("database.json", "r") as read_file:
			data=json.load(read_file)	
			if (svalue in stari)  :				
				data["stare"]=svalue 
		with open("database.json", "w") as write_file:
			json.dump(data, write_file)





	def rdata(self,prog,skey):
		try:
			with open("database.json", "r") as read_file:
				response=json.load(read_file)
				response_prog=response[prog]
				response=response_prog[skey]
				return response

		except:
			return 0 


	def wdata(self,prog,skey,svalue):
		with open("database.json", "r") as read_file:
			data=json.load(read_file)
		for program in data.keys(): 
			if program==prog:
				
				for i in data[program]:		
					
					if i==skey :
						data[program][i]=svalue 
						break
		with open("database.json", "w") as write_file:
			json.dump(data, write_file)

	
	def __str__(self):

		try:
			with open("database.json", "r") as read_file:
				response=json.load(read_file)
			return str(response )
		except:
			return "0"



