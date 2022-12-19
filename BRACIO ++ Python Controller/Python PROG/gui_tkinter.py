
""" ---- IMPORT LIBRARIES ---- """
from tkinter import *
import serial_config
import db
""" ---- VARIABLE DECLARATION ---- """
auto_proram_cycles=db.rdata('program')[0]
auto_steps=db.rdata('program')[1]
auto_point1_w8=db.rdata('program')[2]
auto_point2_w8=db.rdata('program')[3]
auto_point3_w8=db.rdata('program')[4]
auto_point4_w8=db.rdata('program')[5]
auto_point5_w8=db.rdata('program')[6]
auto_point6_w8=db.rdata('program')[7]
auto_point7_w8=db.rdata('program')[8]
auto_point8_w8=db.rdata('program')[9]
auto_point9_w8=db.rdata('program')[10]
auto_point10_w8=db.rdata('program')[11]
auto_count=0 

mode=0

base_read=0.0 
shoulder_read=0.0
elbow_read=0.0
elbow_read=0.0
vwrist_read=0.0
rwrist_read=0.0
gripper_read=0.0


speed_manu= db.rdata("speed") ;
increment_manu =db.rdata("step") ;

point1=db.rdata('point1')
point2=db.rdata('point2')
point3=db.rdata('point3')
point4=db.rdata('point4')
point5=db.rdata('point5')
point6=db.rdata('point6')
point7=db.rdata('point7')
point8=db.rdata('point8')
point9=db.rdata('point9')
point10=db.rdata('point10')	


point1_str=str(point1)
point2_str=str(point2)
point3_str=str(point3)
point4_str=str(point4)
point5_str=str(point5)
point6_str=str(point6)
point7_str=str(point7)
point8_str=str(point8)
point9_str=str(point9)
point10_str=str(point10)


print(point1_str)




# MAIN CLASS TO WRITE ON SERIAL 
class point():
	def __init__(self,arr):
		
		self.base=arr[0]
		self.shoulder=arr[1]
		self.elbow=arr[2]
		self.vwrist=arr[3]
		self.rwrist=arr[4]
		self.gripper=arr[5]

	def sttr(self,numar):
		a=numar//100
		if numar>100 :
			b=(numar-(a*100))//10
		else :
			b=numar//10
		c=numar%10
		return(str(a)+str(b)+str(c))

	def s_base(self):
		numar=self.base
		snumar=self.sttr(numar)
		return snumar

	def s_shoulder(self):
		numar=self.shoulder
		snumar=self.sttr(numar)
		return snumar

	def s_elbow(self):
		numar=self.elbow
		snumar=self.sttr(numar)
		return snumar

	def s_vwrist(self):
		numar=self.vwrist
		snumar=self.sttr(numar)
		return snumar


	def s_rwrist(self):
		numar=self.rwrist
		snumar=self.sttr(numar)
		return snumar

	def s_gripper(self):
		numar=self.gripper
		snumar=self.sttr(numar)
		return snumar


#DECLARING MAIN ROOT AND FRAMES
root=Tk() # declaring the main window , root window
frame0 = Frame(root,width=200, height=400,borderwidth=1,relief='sunken',bg='grey',padx=5,pady=5)
frame1 = Frame(root,width=200, height=400,borderwidth=1,relief='sunken',bg='grey',padx=5,pady=5)
frame2 = Frame(root,width=492, height=400,borderwidth=1,relief='sunken',bg='grey',padx=5,pady=5)
frame3 = Frame(root,width=492, height=400,borderwidth=1,relief='sunken',bg='grey',padx=5,pady=5)
frame4 = Frame(root,width=492, height=400,borderwidth=1,relief='sunken',bg='grey',padx=5,pady=5)
frame5 = Frame(root,width=492, height=400,borderwidth=1,relief='sunken',bg='grey',padx=5,pady=5)
root.geometry("492x965")

""" SERIAL READ """

""" DECODARE TELEGRAMA """
def decodare_char(input_char):
  if (chr(input_char)=='0') :
  	return 0 
  elif (chr(input_char)=='1'):
  	return 1
  elif (chr(input_char)=='2'):
  	return 2
  elif (chr(input_char)=='3'):
  	return 3
  elif (chr(input_char)=='4'):
  	return 4
  elif (chr(input_char)=='5'):
  	return 5
  elif (chr(input_char)=='6'):
  	return 6
  elif (chr(input_char)=='7'):
  	return 7
  elif (chr(input_char)=='8'):
  	return 8
  elif (chr(input_char)=='9'):
  	return 9

""" ---- CREATING EVENTS ----  """
#UPDATE DEGREES ON SCREEN

def get_speed_d():
	global speed_manu
	loc_speed_manu=get_speed.get()
	try:
		speed_manu_int=int(loc_speed_manu)
		a=speed_manu_int//100
		if speed_manu_int>100 :
			b=(speed_manu_int-(a*100))//10
		else :
			b=speed_manu_int//10
		c=speed_manu_int%10
		speed_manu=str(a)+str(b)+str(c)
		print(speed_manu)
	except:
		speed_manu='020'
		print(speed_manu)
   
def get_step_d():
	global increment_manu
	loc_step_manu=get_step.get()
	if int(loc_step_manu)>20 :
		increment_manu=20
	else:
		increment_manu=int(loc_step_manu)
	print(increment_manu)

def update_degrees():
	message=''
	sute=0
	zeci=0 
	unitati=0 
	global base_read
	global shoulder_read
	global elbow_read
	global elbow_read
	global vwrist_read
	global rwrist_read
	global gripper_read
	message=serial_config.serial_read()
	if message[0]==48:
		print("citit")
		sute=decodare_char(message[1]) 
		zeci=decodare_char(message[2]) 
		unitati=decodare_char(message[3]) 
		base_read = sute *100.0 + zeci * 10.0 + unitati   
		sute=decodare_char(message[4]) 
		zeci=decodare_char(message[5]) 
		unitati=decodare_char(message[6]) 
		shoulder_read = sute *100.0 + zeci * 10.0 + unitati  
		sute=decodare_char(message[7]) 
		zeci=decodare_char(message[8]) 
		unitati=decodare_char(message[9]) 
		elbow_read = sute *100.0 + zeci * 10.0 + unitati  
		sute=decodare_char(message[10]) 
		zeci=decodare_char(message[11]) 
		unitati=decodare_char(message[12]) 
		vwrist_read = sute *100.0 + zeci * 10.0 + unitati 
		sute=decodare_char(message[13]) 
		zeci=decodare_char(message[14]) 
		unitati=decodare_char(message[15]) 
		rwrist_read = sute *100.0 + zeci * 10.0 + unitati  
		sute= decodare_char(message[16]) 
		zeci=decodare_char(message[17]) 
		unitati=decodare_char(message[18]) 
		gripper_read = sute *100.0 + zeci * 10.0 + unitati 
		print(base_read)
		print(shoulder_read)
		print(elbow_read)
		print(vwrist_read)
		print(rwrist_read)
		print(gripper_read)	
		current_point_base.config(text=str(base_read))
		current_point_shoulder.config(text=str(shoulder_read))
		current_point_elbow.config(text=str(elbow_read))
		current_point_vwrist.config(text=str(vwrist_read))
		current_point_rwrist.config(text=str(rwrist_read))
		current_point_gripper.config(text=str(gripper_read))

def increment_joint(joint):
	update_degrees()
	global base_read
	global shoulder_read
	global elbow_read
	global vwrist_read
	global rwrist_read
	global gripper_read	
	base_read_i=int(base_read)
	shoulder_read_i=int(shoulder_read)
	elbow_read_i=int(elbow_read)
	vwrist_read_i=int(vwrist_read)
	rwrist_read_i=int(rwrist_read)
	gripper_read_i=int(gripper_read)	
	if joint==1 :
		to_comanda='3' 
		if (base_read_i)<300:
			base_read_i=int(base_read)+increment_manu
	if joint==2 :
		to_comanda='4' 
		if (shoulder_read_i)<120:
			shoulder_read_i=int(shoulder_read)+increment_manu
	if joint==3 :
		to_comanda='5' 	
		if (elbow_read_i)<210:
			elbow_read_i=int(elbow_read)+increment_manu	
	if joint==4 :
		to_comanda='6'
		if (vwrist_read_i)<220:
			vwrist_read_i=int(vwrist_read)+increment_manu
	if joint==5 :
		to_comanda='7' 
		if (rwrist_read_i)<270:
			rwrist_read_i=int(rwrist_read)+increment_manu
	if joint==6 :
		to_comanda='8' 
		if (gripper_read_i)<220:
			gripper_read_i=int(gripper_read)+increment_manu
	point_arr=[base_read_i,shoulder_read_i,elbow_read_i,vwrist_read_i,rwrist_read_i,gripper_read_i]
	point_to=point(point_arr)
	to_grade_base=point_to.s_base() 
	to_grade_shoulder=point_to.s_shoulder()
	to_grade_elbow=point_to.s_elbow()
	to_grade_vwrist=point_to.s_vwrist()
	to_grade_rwrist=point_to.s_rwrist()
	to_grade_gripper=point_to.s_gripper()
	to_speed=speed_manu 

	serial_config.serial_write(to_comanda,to_grade_base,to_grade_shoulder,to_grade_elbow,to_grade_vwrist,to_grade_rwrist,to_grade_gripper,to_speed)

def decrement_joint(joint):
	update_degrees()
	global base_read
	global shoulder_read
	global elbow_read
	global vwrist_read
	global rwrist_read
	global gripper_read	
	base_read_i=int(base_read)
	shoulder_read_i=int(shoulder_read)
	elbow_read_i=int(elbow_read)
	vwrist_read_i=int(vwrist_read)
	rwrist_read_i=int(rwrist_read)
	gripper_read_i=int(gripper_read)
	if joint==1 :
		to_comanda='3' 
		if (base_read_i)>=20:
			base_read_i=int(base_read)-increment_manu
		else:
			base_read_i=22
	if joint==2 :
		to_comanda='4' 
		if (shoulder_read_i)>=20:
			shoulder_read_i=int(shoulder_read)-increment_manu
		else:
			shoulder_read_i=22
	if joint==3 :
		to_comanda='5' 	
		if (elbow_read_i)>=90:
			elbow_read_i=int(elbow_read)-increment_manu		
		else:
			elbow_read_i=92
	if joint==4 :
		to_comanda='6'
		if (vwrist_read_i)>=60:
			vwrist_read_i=int(vwrist_read)-increment_manu
		else:
			vwrist_read_i=62
	if joint==5 :
		to_comanda='7' 
		if (rwrist_read_i)>=20:
			rwrist_read_i=int(rwrist_read)-increment_manu
		else:
			rwrist_read_i=22
	if joint==6 :
		to_comanda='8' 
		if (gripper_read_i)>=160:
			gripper_read_i=int(gripper_read)-increment_manu
		else:
			gripper_read_i=162
	point_arr=[base_read_i,shoulder_read_i,elbow_read_i,vwrist_read_i,rwrist_read_i,gripper_read_i]
	point_to=point(point_arr)
	to_grade_base=point_to.s_base() 
	to_grade_shoulder=point_to.s_shoulder()
	to_grade_elbow=point_to.s_elbow()
	to_grade_vwrist=point_to.s_vwrist()
	to_grade_rwrist=point_to.s_rwrist()
	to_grade_gripper=point_to.s_gripper()
	to_speed=speed_manu 

	serial_config.serial_write(to_comanda,to_grade_base,to_grade_shoulder,to_grade_elbow,to_grade_vwrist,to_grade_rwrist,to_grade_gripper,to_speed)

def sincronizare():
	to_comanda='1' ;
	to_grade_base='180' ;
	to_grade_shoulder='120' ;
	to_grade_elbow='150' ;
	to_grade_vwrist='110' ;
	to_grade_rwrist='050' ;
	to_grade_gripper='230' ;
	to_speed='030' ;
	serial_config.serial_write(to_comanda,to_grade_base,to_grade_shoulder,to_grade_elbow,to_grade_vwrist,to_grade_rwrist,to_grade_gripper,to_speed)

def teach_point(p_teach):
	update_degrees()
	global base_read
	global shoulder_read
	global elbow_read
	global vwrist_read
	global rwrist_read
	global gripper_read		
	base_int=int(base_read)
	shoulder_i=int(shoulder_read)
	elbow_i=int(elbow_read)
	vwrist_i=int(vwrist_read)
	rwrist_i=int(rwrist_read)
	gripper_i=int(gripper_read)


	if p_teach==1 :
		db.wdata("point1",[base_int,shoulder_i,elbow_i,vwrist_i,rwrist_i,gripper_i])
		Point1_value.config(text=str([base_int,shoulder_i,elbow_i,vwrist_i,rwrist_i,gripper_i]))		
	elif p_teach==2 :
		db.wdata("point2",[base_int,shoulder_i,elbow_i,vwrist_i,rwrist_i,gripper_i])
		Point2_value.config(text=str([base_int,shoulder_i,elbow_i,vwrist_i,rwrist_i,gripper_i]))	
	elif p_teach==3 :
		db.wdata("point3",[base_int,shoulder_i,elbow_i,vwrist_i,rwrist_i,gripper_i])
		Point3_value.config(text=str([base_int,shoulder_i,elbow_i,vwrist_i,rwrist_i,gripper_i]))	
	elif p_teach==4 :
		db.wdata("point4",[base_int,shoulder_i,elbow_i,vwrist_i,rwrist_i,gripper_i])
		Point4_value.config(text=str([base_int,shoulder_i,elbow_i,vwrist_i,rwrist_i,gripper_i]))	
	elif p_teach==5 :
		db.wdata("point5",[base_int,shoulder_i,elbow_i,vwrist_i,rwrist_i,gripper_i])
		Point5_value.config(text=str([base_int,shoulder_i,elbow_i,vwrist_i,rwrist_i,gripper_i]))	
	elif p_teach==6 :
		db.wdata("point6",[base_int,shoulder_i,elbow_i,vwrist_i,rwrist_i,gripper_i])
		Point6_value.config(text=str([base_int,shoulder_i,elbow_i,vwrist_i,rwrist_i,gripper_i]))	
	elif p_teach==7 :
		db.wdata("point7",[base_int,shoulder_i,elbow_i,vwrist_i,rwrist_i,gripper_i])
		Point7_value.config(text=str([base_int,shoulder_i,elbow_i,vwrist_i,rwrist_i,gripper_i]))	
	elif p_teach==8 :
		db.wdata("point8",[base_int,shoulder_i,elbow_i,vwrist_i,rwrist_i,gripper_i])
		Point8_value.config(text=str([base_int,shoulder_i,elbow_i,vwrist_i,rwrist_i,gripper_i]))	
	elif p_teach==9 :
		db.wdata("point9",[base_int,shoulder_i,elbow_i,vwrist_i,rwrist_i,gripper_i])
		Point9_value.config(text=str([base_int,shoulder_i,elbow_i,vwrist_i,rwrist_i,gripper_i]))	
	elif p_teach==10 :
		db.wdata("point10",[base_int,shoulder_i,elbow_i,vwrist_i,rwrist_i,gripper_i])
		Point10_value.config(text=str([base_int,shoulder_i,elbow_i,vwrist_i,rwrist_i,gripper_i]))	

def save_program():


	global auto_proram_cycles
	global auto_steps
	global auto_point1_w8
	global auto_point2_w8
	global auto_point3_w8
	global auto_point4_w8
	global auto_point5_w8
	global auto_point6_w8
	global auto_point7_w8
	global auto_point8_w8
	global auto_point9_w8
	global auto_point10_w8

	try:
		auto_proram_cycles=int(NR_OF_CYCLES_E.get())
	except:
		auto_proram_cycles=0

	try:
		auto_steps=int(NR_OF_STEPS_E.get())
	except:
		auto_steps=0

	try:
		auto_point1_w8=int(P1_W8_TIME_E.get())
	except:
		auto_point1_w8=0

	try:
		auto_point2_w8=int(P2_W8_TIME_E.get())
	except:
		auto_point2_w8=0

	try:		
		auto_point3_w8=int(P3_W8_TIME_E.get())
	except:
		auto_point3_w8=0
	try:	
		auto_point4_w8=int(P4_W8_TIME_E.get())
	except:
		auto_point4_w8=0

	try:	
		auto_point5_w8=int(P5_W8_TIME_E.get())
	except:
		auto_point5_w8=0

	try:	
		auto_point6_w8=int(P6_W8_TIME_E.get())
	except:
		auto_point6_w8=0

	try:	
		auto_point7_w8=int(P7_W8_TIME_E.get())
	except:
		auto_point7_w8=0

	try:	
		auto_point8_w8=int(P8_W8_TIME_E.get())
	except:
		auto_point8_w8=0

	try:
		auto_point9_w8=int(P9_W8_TIME_E.get())
	except:
		auto_point9_w8=0
	try:
		auto_point10_w8=int(P10_W8_TIME_E.get())
	except:
				auto_point10_w8=0

	program_arr=[auto_proram_cycles,auto_steps,auto_point1_w8,auto_point2_w8,auto_point3_w8,auto_point4_w8,auto_point5_w8,auto_point6_w8,auto_point7_w8,auto_point8_w8,auto_point9_w8,auto_point10_w8]

	db.wdata("program",program_arr)
	NR_OF_CYCLES_D1.config(text=str(auto_proram_cycles)+" cycles")
	NR_OF_STEPS_D1.config(text=str(auto_steps)+" steps")
	P1_W8_TIME_D1.config(text=str(auto_point1_w8)+" sec")
	P2_W8_TIME_D1.config(text=str(auto_point2_w8)+" sec")
	P3_W8_TIME_D1.config(text=str(auto_point3_w8)+" sec")
	P4_W8_TIME_D1.config(text=str(auto_point4_w8)+" sec")
	P5_W8_TIME_D1.config(text=str(auto_point5_w8)+" sec")
	P6_W8_TIME_D1.config(text=str(auto_point6_w8)+" sec")
	P7_W8_TIME_D1.config(text=str(auto_point7_w8)+" sec")
	P8_W8_TIME_D1.config(text=str(auto_point8_w8)+" sec")
	P9_W8_TIME_D1.config(text=str(auto_point9_w8)+" sec")
	P10_W8_TIME_D1.config(text=str(auto_point10_w8)+" sec")

def start_auto():
	global auto_count
	global mode 
	program_r=db.rdata("program")
	auto_count=program_r[0]
	mode=1

	root.after(program_r[2]*1000,start_goto_p1)
		
def start_manual():
	
	global mode 
	mode=0

def start_goto_p1():
	global speed_manu
	global auto_point1_w8
	global auto_steps
	global auto_count


	if auto_count>0 and mode==1 :
		point1=point(db.rdata("point1"))
		serial_config.serial_write('2',point1.s_base(),point1.s_shoulder(),point1.s_elbow(),point1.s_vwrist(),point1.s_rwrist(),point1.s_gripper(),speed_manu)
		if auto_steps>=2 :
			root.after(auto_point1_w8*1000,start_goto_p2)
		else :
			auto_count-=1 
			root.after(auto_point1_w8*1000,start_goto_p1)
	else:
			root.after(auto_point1_w8*1000,sincronizare)

def start_goto_p2():
	global speed_manu
	global auto_point2_w8
	global auto_steps
	global auto_count
	global mode 
	if auto_count>0 and mode==1 :
		point1=point(db.rdata("point2"))
		serial_config.serial_write('2',point1.s_base(),point1.s_shoulder(),point1.s_elbow(),point1.s_vwrist(),point1.s_rwrist(),point1.s_gripper(),speed_manu)

		if auto_steps>=3 :
			root.after(auto_point2_w8*1000,start_goto_p3)
		else :
			auto_count-=1 
			root.after(auto_point2_w8*1000,start_goto_p1)

def start_goto_p3():
	global speed_manu
	global auto_point3_w8
	global auto_steps
	global auto_count
	global mode 
	if auto_count>0 and mode==1 :
		point1=point(db.rdata("point3"))
		serial_config.serial_write('2',point1.s_base(),point1.s_shoulder(),point1.s_elbow(),point1.s_vwrist(),point1.s_rwrist(),point1.s_gripper(),speed_manu)

		if auto_steps>=4 :
			root.after(auto_point3_w8*1000,start_goto_p4)
		else :
			auto_count-=1 
			root.after(auto_point3_w8*1000,start_goto_p1)

def start_goto_p4():
	global speed_manu
	global auto_point4_w8
	global auto_steps
	global auto_count
	global mode 
	if auto_count>0 and mode==1 :
		point1=point(db.rdata("point4"))
		serial_config.serial_write('2',point1.s_base(),point1.s_shoulder(),point1.s_elbow(),point1.s_vwrist(),point1.s_rwrist(),point1.s_gripper(),speed_manu)

		if auto_steps>=5 :
			root.after(auto_point4_w8*1000,start_goto_p5)
		else :
			auto_count-=1 
			root.after(auto_point4_w8*1000,start_goto_p1)

def start_goto_p5():
	global speed_manu
	global auto_point5_w8
	global auto_steps
	global auto_count
	global mode 
	if auto_count>0 and mode==1 :
		point1=point(db.rdata("point5"))
		serial_config.serial_write('2',point1.s_base(),point1.s_shoulder(),point1.s_elbow(),point1.s_vwrist(),point1.s_rwrist(),point1.s_gripper(),speed_manu)

		if auto_steps>=6 :
			root.after(auto_point5_w8*1000,start_goto_p6)
		else :
			auto_count-=1 
			root.after(auto_point5_w8*1000,start_goto_p1)

def start_goto_p6():
	global speed_manu
	global auto_point6_w8
	global auto_steps
	global auto_count
	global mode 
	if auto_count>0 and mode==1:
		point1=point(db.rdata("point6"))
		serial_config.serial_write('2',point1.s_base(),point1.s_shoulder(),point1.s_elbow(),point1.s_vwrist(),point1.s_rwrist(),point1.s_gripper(),speed_manu)

		if auto_steps>=7 :
			root.after(auto_point6_w8*1000,start_goto_p7)
		else :
			auto_count-=1 
			root.after(auto_point6_w8*1000,start_goto_p1)

def start_goto_p7():
	global speed_manu
	global auto_point7_w8
	global auto_steps
	global auto_count
	global mode 
	if auto_count>0 and mode==1:
		point1=point(db.rdata("point7"))
		serial_config.serial_write('2',point1.s_base(),point1.s_shoulder(),point1.s_elbow(),point1.s_vwrist(),point1.s_rwrist(),point1.s_gripper(),speed_manu)

		if auto_steps>=8 :
			root.after(auto_point7_w8*1000,start_goto_p8)
		else :
			auto_count-=1 
			root.after(auto_point7_w8*1000,start_goto_p1)

def start_goto_p8():
	global speed_manu
	global auto_point8_w8
	global auto_steps
	global auto_count
	global mode 
	if auto_count>0 and mode==1 :
		point1=point(db.rdata("point8"))
		serial_config.serial_write('2',point1.s_base(),point1.s_shoulder(),point1.s_elbow(),point1.s_vwrist(),point1.s_rwrist(),point1.s_gripper(),speed_manu)

		if auto_steps>=9 :
			root.after(auto_point8_w8*1000,start_goto_p9)
		else :
			auto_count-=1 
			root.after(auto_point8_w8*1000,start_goto_p1)

def start_goto_p9():
	global speed_manu
	global auto_point9_w8
	global auto_steps
	global auto_count
	global mode 
	if auto_count>0 and mode==1 :
		point1=point(db.rdata("point9"))
		serial_config.serial_write('2',point1.s_base(),point1.s_shoulder(),point1.s_elbow(),point1.s_vwrist(),point1.s_rwrist(),point1.s_gripper(),speed_manu)

		if auto_steps>=9 :
			root.after(auto_point9_w8*1000,start_goto_p10)
		else :
			auto_count-=1 
			root.after(auto_point9_w8*1000,start_goto_p1)

def start_goto_p10():
	global speed_manu
	global auto_point10_w8
	global auto_steps
	global auto_count
	global mode 
	if auto_count>0 and mode==1:
		point1=point(db.rdata("point10"))
		serial_config.serial_write('2',point1.s_base(),point1.s_shoulder(),point1.s_elbow(),point1.s_vwrist(),point1.s_rwrist(),point1.s_gripper(),speed_manu)

		auto_count-=1 
		root.after(auto_point9_w8*1000,start_goto_p1)
		
		
		

""" ---- LABELS ---- """

mySection1=Button(frame0 , text='Teach Mode',width=21, command=start_manual)
mySection2=Button(frame0 , text='Auto Mode',width=22 ,command=start_auto)
mySection3=Button(frame0 , text='Synchronize',command= sincronizare,width=21)


""" --- MANUAL --- """


current_point_base_text=Label(frame1,text='Base',width=15,bg='grey')
current_point_shoulder_text=Label(frame1,text='Shoulder',width=15,bg='grey')
current_point_elbow_text=Label(frame1,text='Elbow',width=15,bg='grey')
current_point_vwrist_text=Label(frame1,text='VWrist',width=15,bg='grey')
current_point_rwrist_text=Label(frame1,text='RWrist',width=15,bg='grey')
current_point_gripper_text=Label(frame1,text='Gripper',width=15,bg='grey')



inc_base=Button(frame1 , text='+',command= lambda:increment_joint(1))
dec_base=Button(frame1 , text='-',command= lambda:decrement_joint(1))


inc_shoulder=Button(frame1 , text='+',command= lambda:increment_joint(2))
dec_shoulder=Button(frame1 , text='-',command= lambda:decrement_joint(2))

inc_elbow=Button(frame1 , text='+',command= lambda:increment_joint(3))
dec_elbow=Button(frame1 , text='-',command= lambda:decrement_joint(3))

inc_vwrist=Button(frame1 , text='+',command= lambda:increment_joint(4))
dec_vwrist=Button(frame1 , text='-',command= lambda:decrement_joint(4))

inc_rwrist=Button(frame1 , text='+',command= lambda:increment_joint(5))
dec_rwrist=Button(frame1 , text='-',command= lambda:decrement_joint(5))

inc_gripper=Button(frame1 , text='+',command= lambda:increment_joint(6))
dec_gripper=Button(frame1 , text='-',command= lambda:decrement_joint(6))

current_points=Label(frame1,text='Current Position',width=15)
limita_inf=Label(frame1,text='Min Limit',width=15)
limita_sup=Label(frame1,text='Max Limit',width=15)
current_point_base=Label(frame1,text=str(base_read),width=15)
current_point_shoulder=Label(frame1,text=str(shoulder_read),width=15)
current_point_elbow=Label(frame1,text=str(elbow_read),width=15)
current_point_vwrist=Label(frame1,text=str(vwrist_read),width=15)
current_point_rwrist=Label(frame1,text=str(rwrist_read),width=15)
current_point_gripper=Label(frame1,text=str(gripper_read),width=15)



min_base=Label(frame1,text='20',width=5)
min_shoulder=Label(frame1,text='20',width=5)
min_elbow=Label(frame1,text='90',width=5)
min_vwrist=Label(frame1,text='60',width=5)
min_rwrist=Label(frame1,text='20',width=5)
min_gripper=Label(frame1,text='160',width=5)


max_base=Label(frame1,text='300',width=5)
max_shoulder=Label(frame1,text='120',width=5)
max_elbow=Label(frame1,text='210',width=5)
max_vwrist=Label(frame1,text='220',width=5)
max_rwrist=Label(frame1,text='270',width=5)
max_gripper=Label(frame1,text='220',width=5)


text_speed=Label(frame1,text='Speed',width=15,bg='grey')
text_step=Label(frame1,text='Step',width=15,bg='grey')

get_speed=Entry(frame1,width=10)
get_step=Entry(frame1,width=10)


set_speed=Button(frame1,text='SET',width=5,command=get_speed_d)
set_step=Button(frame1,text='SET',width=5,command=get_step_d)



Point_TEXT=Label(frame3,text='PROGRAM POINTS',width=68)

Descr1=Label(frame2,text='POINTS',width=22)
Descr2=Label(frame2,text='COORDINATES',width=22)
Descr3=Label(frame2,text='TEACH NEW POSITION',width=22)


Point1=Label(frame2,text='Point1',width=10)
Point2=Label(frame2,text='Point2',width=10)
Point3=Label(frame2,text='Point3',width=10)
Point4=Label(frame2,text='Point4',width=10)
Point5=Label(frame2,text='Point5',width=10)
Point6=Label(frame2,text='Point6',width=10)
Point7=Label(frame2,text='Point7',width=10)
Point8=Label(frame2,text='Point8',width=10)
Point9=Label(frame2,text='Point9',width=10)
Point10=Label(frame2,text='Point10',width=10)

Point1_value=Label(frame2,text=point1_str,width=20)
Point2_value=Label(frame2,text=point2_str,width=20)
Point3_value=Label(frame2,text=point3_str,width=20)
Point4_value=Label(frame2,text=point4_str,width=20)
Point5_value=Label(frame2,text=point5_str,width=20)
Point6_value=Label(frame2,text=point6_str,width=20)
Point7_value=Label(frame2,text=point7_str,width=20)
Point8_value=Label(frame2,text=point8_str,width=20)
Point9_value=Label(frame2,text=point9_str,width=20)
Point10_value=Label(frame2,text=point10_str,width=20)


Point1_teach=Button(frame2 , text='Teach P1',command= lambda:teach_point(1),width=7)
Point2_teach=Button(frame2 , text='Teach P2',command= lambda:teach_point(2),width=7)
Point3_teach=Button(frame2 , text='Teach P3',command= lambda:teach_point(3),width=7)
Point4_teach=Button(frame2 , text='Teach P4',command= lambda:teach_point(4),width=7)
Point5_teach=Button(frame2 , text='Teach P5',command= lambda:teach_point(5),width=7)
Point6_teach=Button(frame2 , text='Teach P6',command= lambda:teach_point(6),width=7)
Point7_teach=Button(frame2 , text='Teach P7',command= lambda:teach_point(7),width=7)
Point8_teach=Button(frame2 , text='Teach P8',command= lambda:teach_point(8),width=7)
Point9_teach=Button(frame2 , text='Teach P9',command= lambda:teach_point(9),width=7)
Point10_teach=Button(frame2 , text='Teach P10',command= lambda:teach_point(10),width=7)


PROG_TEXT=Label(frame4,text='PROGRAM SEQUENCE',width=68)
PROG_STATE=Label(frame5,text='SAVED PROGRAM STATE',width=18,bg='grey')


NR_OF_CYCLES=Label(frame5,text='NR OF PROGRAM CYCLES ',width=30)
NR_OF_STEPS=Label(frame5,text='NR OF STEPS FROM P1 TO PX',width=30)
P1_W8_TIME=Label(frame5,text='GO TO P1 AND WAIT -->>',width=30)
P2_W8_TIME=Label(frame5,text='GO TO P2 AND WAIT -->>',width=30)
P3_W8_TIME=Label(frame5,text='GO TO P3 AND WAIT -->>',width=30)
P4_W8_TIME=Label(frame5,text='GO TO P4 AND WAIT -->>',width=30)
P5_W8_TIME=Label(frame5,text='GO TO P5 AND WAIT -->>',width=30)
P6_W8_TIME=Label(frame5,text='GO TO P6 AND WAIT -->>',width=30)
P7_W8_TIME=Label(frame5,text='GO TO P7 AND WAIT -->>',width=30)
P8_W8_TIME=Label(frame5,text='GO TO P8 AND WAIT -->>',width=30)
P9_W8_TIME=Label(frame5,text='GO TO P9 AND WAIT -->>',width=30)
P10_W8_TIME=Label(frame5,text='GO TO P10 AND WAIT -->>',width=30)



NR_OF_CYCLES_D=Label(frame5,text='',width=6,bg='grey')
NR_OF_STEPS_D=Label(frame5,text='',width=6,bg='grey')
P1_W8_TIME_D=Label(frame5,text='',width=6,bg='grey')
P2_W8_TIME_D=Label(frame5,text='',width=6,bg='grey')
P3_W8_TIME_D=Label(frame5,text='',width=6,bg='grey')
P4_W8_TIME_D=Label(frame5,text='',width=6,bg='grey')
P5_W8_TIME_D=Label(frame5,text='',width=6,bg='grey')
P6_W8_TIME_D=Label(frame5,text='',width=6,bg='grey')
P7_W8_TIME_D=Label(frame5,text='',width=6,bg='grey')
P8_W8_TIME_D=Label(frame5,text='',width=6,bg='grey')
P9_W8_TIME_D=Label(frame5,text='',width=6,bg='grey')
P10_W8_TIME_D=Label(frame5,text='',width=6,bg='grey')



NR_OF_CYCLES_E=Entry(frame5,width=14)
NR_OF_STEPS_E=Entry(frame5,width=14)
P1_W8_TIME_E=Entry(frame5,width=14)
P2_W8_TIME_E=Entry(frame5,width=14)
P3_W8_TIME_E=Entry(frame5,width=14)
P4_W8_TIME_E=Entry(frame5,width=14)
P5_W8_TIME_E=Entry(frame5,width=14)
P6_W8_TIME_E=Entry(frame5,width=14)
P7_W8_TIME_E=Entry(frame5,width=14)
P8_W8_TIME_E=Entry(frame5,width=14)
P9_W8_TIME_E=Entry(frame5,width=14)
P10_W8_TIME_E=Entry(frame5,width=14)

NR_OF_CYCLES_D1=Label(frame5,text=str(auto_proram_cycles)+" cycles",width=18,bg='grey')
NR_OF_STEPS_D1=Label(frame5,text=str(auto_steps)+" steps",width=18,bg='grey')
P1_W8_TIME_D1=Label(frame5,text=str(auto_point1_w8)+" sec",width=18,bg='grey')
P2_W8_TIME_D1=Label(frame5,text=str(auto_point2_w8)+" sec",width=18,bg='grey')
P3_W8_TIME_D1=Label(frame5,text=str(auto_point3_w8)+" sec",width=18,bg='grey')
P4_W8_TIME_D1=Label(frame5,text=str(auto_point4_w8)+" sec",width=18,bg='grey')
P5_W8_TIME_D1=Label(frame5,text=str(auto_point5_w8)+" sec",width=18,bg='grey')
P6_W8_TIME_D1=Label(frame5,text=str(auto_point6_w8)+" sec",width=18,bg='grey')
P7_W8_TIME_D1=Label(frame5,text=str(auto_point7_w8)+" sec",width=18,bg='grey')
P8_W8_TIME_D1=Label(frame5,text=str(auto_point8_w8)+" sec",width=18,bg='grey')
P9_W8_TIME_D1=Label(frame5,text=str(auto_point9_w8)+" sec",width=18,bg='grey')
P10_W8_TIME_D1=Label(frame5,text=str(auto_point10_w8)+" sec",width=18,bg='grey')








P_TEACH_space=Label(frame5 , text='',bg='grey')
P_TEACH=Button(frame5 , text='SAVE CHANGES',command=save_program,width=22)








""" ---- RENDERING LABELS ---- """


frame0.grid(row=1)
frame1.grid(row=2)
frame2.grid(row=4)
frame3.grid(row=3)
frame4.grid(row=5)
frame5.grid(row=6)

mySection1.grid(row=1,column=0)
mySection2.grid(row=1,column=1)
mySection3.grid(row=1,column=2)



current_point_base_text.grid(row=2,column=0)
current_point_shoulder_text.grid(row=3,column=0)
current_point_elbow_text.grid(row=4,column=0)
current_point_vwrist_text.grid(row=5,column=0)
current_point_rwrist_text.grid(row=6,column=0)
current_point_gripper_text.grid(row=7,column=0)

inc_base.grid(row=2,column=1)
dec_base.grid(row=2,column=3)
inc_shoulder.grid(row=3,column=1)
dec_shoulder.grid(row=3,column=3)
inc_elbow.grid(row=4,column=1)
dec_elbow.grid(row=4,column=3)
inc_vwrist.grid(row=5,column=1)
dec_vwrist.grid(row=5,column=3)
inc_rwrist.grid(row=6,column=1)
dec_rwrist.grid(row=6,column=3)
inc_gripper.grid(row=7,column=1)
dec_gripper.grid(row=7,column=3)

current_points.grid(row=1,column=2)
current_point_base.grid(row=2,column=2)
current_point_shoulder.grid(row=3,column=2)
current_point_elbow.grid(row=4,column=2)
current_point_vwrist.grid(row=5,column=2)
current_point_rwrist.grid(row=6,column=2)
current_point_gripper.grid(row=7,column=2)


limita_inf.grid(row=1,column=4)
limita_sup.grid(row=1,column=5)

min_base.grid(row=2,column=4)
min_shoulder.grid(row=3,column=4)
min_elbow.grid(row=4,column=4)
min_vwrist.grid(row=5,column=4)
min_rwrist.grid(row=6,column=4)
min_gripper.grid(row=7,column=4)


max_base.grid(row=2,column=5)
max_shoulder.grid(row=3,column=5)
max_elbow.grid(row=4,column=5)
max_vwrist.grid(row=5,column=5)
max_rwrist.grid(row=6,column=5)
max_gripper.grid(row=7,column=5)


text_speed.grid(row=8,column=0)
text_step.grid(row=9,column=0)

get_speed.grid(row=8,column=2)
get_step.grid(row=9,column=2)


set_speed.grid(row=8,column=4)
set_step.grid(row=9,column=4)

Descr1.grid(row=1,column=0)
Descr2.grid(row=1,column=1)
Descr3.grid(row=1,column=2)

Point_TEXT.grid(row=0,column=0)
Point1.grid(row=2,column=0)
Point2.grid(row=3,column=0)
Point3.grid(row=4,column=0)
Point4.grid(row=5,column=0)
Point5.grid(row=6,column=0)
Point6.grid(row=7,column=0)
Point7.grid(row=8,column=0)
Point8.grid(row=9,column=0)
Point9.grid(row=10,column=0)
Point10.grid(row=11,column=0)


Point1_value.grid(row=2,column=1)
Point2_value.grid(row=3,column=1)
Point3_value.grid(row=4,column=1)
Point4_value.grid(row=5,column=1)
Point5_value.grid(row=6,column=1)
Point6_value.grid(row=7,column=1)
Point7_value.grid(row=8,column=1)
Point8_value.grid(row=9,column=1)
Point9_value.grid(row=10,column=1)
Point10_value.grid(row=11,column=1)

Point1_teach.grid(row=2,column=2)
Point2_teach.grid(row=3,column=2)
Point3_teach.grid(row=4,column=2)
Point4_teach.grid(row=5,column=2)
Point5_teach.grid(row=6,column=2)
Point6_teach.grid(row=7,column=2)
Point7_teach.grid(row=8,column=2)
Point8_teach.grid(row=9,column=2)
Point9_teach.grid(row=10,column=2)
Point10_teach.grid(row=11,column=2)



PROG_TEXT.grid(row=0,column=0)

PROG_STATE.grid(row=0,column=3)

NR_OF_CYCLES.grid(row=1,column=0)
NR_OF_STEPS.grid(row=2,column=0)
P1_W8_TIME.grid(row=3,column=0)
P2_W8_TIME.grid(row=4,column=0)
P3_W8_TIME.grid(row=5,column=0)
P4_W8_TIME.grid(row=6,column=0)
P5_W8_TIME.grid(row=7,column=0)
P6_W8_TIME.grid(row=8,column=0)
P7_W8_TIME.grid(row=9,column=0)
P8_W8_TIME.grid(row=10,column=0)
P9_W8_TIME.grid(row=11,column=0)
P10_W8_TIME.grid(row=12,column=0)




NR_OF_CYCLES_D.grid(row=1,column=1)
NR_OF_STEPS_D.grid(row=2,column=1)
P1_W8_TIME_D.grid(row=3,column=1)
P2_W8_TIME_D.grid(row=4,column=1)
P3_W8_TIME_D.grid(row=5,column=1)
P4_W8_TIME_D.grid(row=6,column=1)
P5_W8_TIME_D.grid(row=7,column=1)
P6_W8_TIME_D.grid(row=8,column=1)
P7_W8_TIME_D.grid(row=9,column=1)
P8_W8_TIME_D.grid(row=10,column=1)
P9_W8_TIME_D.grid(row=11,column=1)
P10_W8_TIME_D.grid(row=12,column=1)



NR_OF_CYCLES_E.grid(row=1,column=2)
NR_OF_STEPS_E.grid(row=2,column=2)
P1_W8_TIME_E.grid(row=3,column=2)
P2_W8_TIME_E.grid(row=4,column=2)
P3_W8_TIME_E.grid(row=5,column=2)
P4_W8_TIME_E.grid(row=6,column=2)
P5_W8_TIME_E.grid(row=7,column=2)
P6_W8_TIME_E.grid(row=8,column=2)
P7_W8_TIME_E.grid(row=9,column=2)
P8_W8_TIME_E.grid(row=10,column=2)
P9_W8_TIME_E.grid(row=11,column=2)
P10_W8_TIME_E.grid(row=12,column=2)


NR_OF_CYCLES_D1.grid(row=1,column=3)
NR_OF_STEPS_D1.grid(row=2,column=3)
P1_W8_TIME_D1.grid(row=3,column=3)
P2_W8_TIME_D1.grid(row=4,column=3)
P3_W8_TIME_D1.grid(row=5,column=3)
P4_W8_TIME_D1.grid(row=6,column=3)
P5_W8_TIME_D1.grid(row=7,column=3)
P6_W8_TIME_D1.grid(row=8,column=3)
P7_W8_TIME_D1.grid(row=9,column=3)
P8_W8_TIME_D1.grid(row=10,column=3)
P9_W8_TIME_D1.grid(row=11,column=3)
P10_W8_TIME_D1.grid(row=12,column=3)


P_TEACH_space.grid(row=13,column=0,columnspan=4)

P_TEACH.grid(row=14,column=0,columnspan=1)
print("started")
""" ---- SYSTEM CALL ---- """
root.after(1000,update_degrees())
root.after(1500,start_auto())
root.mainloop() # will continous looping (infinite while)
