""" ---- IMPORT LIBRARIES ---- """
import serial #SERIAL PORT LIB
import db
import time



""" ---- VARIABLE DECLARATION ---- """
com=''  #COM PORT
baudrate=0 #baudrate


""" ---- SERIAL PROGRAM ---- """
DB=db.Database()
program=DB.rprogram()
""" SERIAL CONFIG """
ser=serial.Serial()
ser.baudrate=DB.rdata(program,"baudrate")
ser.port=DB.rdata(program,"port");


""" SERIAL WRITE """

#FORMA TELEGRAMA 
# 'YQQQEEERRRTTTYYYUUUIII'
# Y=COMANDA  1- sincronizare 2-miscare la punct 3- miscare baza 4-miscare shoulder 5-miscare elbow , 6-miscare vwrist ,7-miscare rwrist ,8-miscare gripper
# QQQ= grade_base  20-300
# EEE= grade_shoulder 20-120
# RRR= grade_elbow 90-120
# TTT= grade_vwrist 60-220
# YYY = grade_rwrist 20-270
# UUU = grade_gripper 160-220
# III = speed

# point home={157.5 ,10.0,90.0,110.0,100.0, 70.0};
# point home={grade_gripper ,grade_rwrist,grade_vwrist,grade_elbow,grade_shoulder, grade_base};

""" SERIAL WRITE """
def serial_write(comanda,grade_base,grade_shoulder,grade_elbow,grade_vwrist,grade_rwrist,grade_gripper,speed) :
	telegrama='{a}{b}{c}{d}{e}{f}{g}{i}'.format(a=comanda,b=grade_base,c=grade_shoulder,d=grade_elbow,e=grade_vwrist,f=grade_rwrist,g=grade_gripper,i=speed).encode('ASCII')
	telegrama_s=comanda+grade_base+grade_shoulder+grade_elbow+grade_vwrist+grade_rwrist+grade_gripper+speed
	try:
		
		print(telegrama_s)
		ser.close()
		ser.open()
		ser.write(telegrama)
		ser.close()
	except:
		print("unable to write")
		pass
	



""" SERIAL READ """

def serial_read():
	ser.close()
	try:
		ser.open()	
		s = ser.read(22)
		ser.close()
		print(s)
		
	except:
		s='1111111111'
		print("unable to read")
	return s 



to_comanda='1' ;
to_grade_base='180' ;
to_grade_shoulder='120' ;
to_grade_elbow='150' ;
to_grade_vwrist='110' ;
to_grade_rwrist='050' ;
to_grade_gripper='230' ;
to_speed='020' ;



