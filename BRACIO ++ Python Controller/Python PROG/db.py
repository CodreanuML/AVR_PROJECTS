import json



data = {

	"baudrate":9600,
	"port":'COM4',

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
	"program":[1,10,6000,6000,6000,6000,6000,6000,6000,6000,6000,6000],
	
}


def initializare():
	with open("data_file.json", "w") as write_file:
		json.dump(data, write_file)



def show_db():
	with open("data_file.json", "r") as read_file:
		response=json.load(read_file)
	return response 


def rdata(skey):
	try:
		with open("data_file.json", "r") as read_file:
			response=json.load(read_file)
			response=response[skey]
			return response

	except:
		return 0 


def wdata(skey,svalue):
	with open("data_file.json", "r") as read_file:
		data=json.load(read_file)
	for i in data.keys():		
		if i==skey :
			data[i]=svalue 
			break
	with open("data_file.json", "w") as write_file:
		json.dump(data, write_file)

	








