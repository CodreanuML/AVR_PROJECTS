import serial_config
import db
import sys
import time
""" ---- VARIABLE DECLARATION ---- """
try:
	argv_sys=int(sys.argv[1])

	p_argv=argv_sys % 10
	m_argv=argv_sys // 10

except:
	p_argv=0
	m_argv=0
print(p_argv)
print(m_argv)
#DABATASE INITIALIZATION
DB=db.Database()


#ALL VARIABLE INITIALIZATION
if p_argv in range(1,10):
	program="prog"+str(p_argv)
else:
	program=DB.rprogram()

if m_argv==1 :
	mode=1
else:
	mode=0


auto_program_cycles=DB.rdata(program,'program')[0]
auto_steps=DB.rdata(program,'program')[1]
auto_point1_w8=DB.rdata(program,'program')[2]
auto_point2_w8=DB.rdata(program,'program')[3]
auto_point3_w8=DB.rdata(program,'program')[4]
auto_point4_w8=DB.rdata(program,'program')[5]
auto_point5_w8=DB.rdata(program,'program')[6]
auto_point6_w8=DB.rdata(program,'program')[7]
auto_point7_w8=DB.rdata(program,'program')[8]
auto_point8_w8=DB.rdata(program,'program')[9]
auto_point9_w8=DB.rdata(program,'program')[10]
auto_point10_w8=DB.rdata(program,'program')[11]

speed_manu= DB.rdata(program,"speed") ;
increment_manu =DB.rdata(program,"step") ;
point1=DB.rdata(program,'point1')
point2=DB.rdata(program,'point2')
point3=DB.rdata(program,'point3')
point4=DB.rdata(program,'point4')
point5=DB.rdata(program,'point5')
point6=DB.rdata(program,'point6')
point7=DB.rdata(program,'point7')
point8=DB.rdata(program,'point8')
point9=DB.rdata(program,'point9')
point10=DB.rdata(program,'point10')	

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

def start_goto_p1():
	global program
	global speed_manu
	global auto_point1_w8



	
	point1=point(DB.rdata(program,"point1"))
	serial_config.serial_write('2',point1.s_base(),point1.s_shoulder(),point1.s_elbow(),point1.s_vwrist(),point1.s_rwrist(),point1.s_gripper(),speed_manu)
	time.sleep(auto_point1_w8)


def start_goto_p2():
	global program
	global speed_manu
	global auto_point2_w8


	point1=point(DB.rdata(program,"point2"))
	serial_config.serial_write('2',point1.s_base(),point1.s_shoulder(),point1.s_elbow(),point1.s_vwrist(),point1.s_rwrist(),point1.s_gripper(),speed_manu)
	time.sleep(auto_point2_w8)

def start_goto_p3():
	global program
	global speed_manu
	global auto_point3_w8

	point1=point(DB.rdata(program,"point3"))
	serial_config.serial_write('2',point1.s_base(),point1.s_shoulder(),point1.s_elbow(),point1.s_vwrist(),point1.s_rwrist(),point1.s_gripper(),speed_manu)
	time.sleep(auto_point3_w8)


def start_goto_p4():
	global program
	global speed_manu
	global auto_point4_w8


	point1=point(DB.rdata(program,"point4"))
	serial_config.serial_write('2',point1.s_base(),point1.s_shoulder(),point1.s_elbow(),point1.s_vwrist(),point1.s_rwrist(),point1.s_gripper(),speed_manu)
	time.sleep(auto_point4_w8)

def start_goto_p5():
	global program
	global speed_manu
	global auto_point5_w8


	point1=point(DB.rdata(program,"point5"))
	serial_config.serial_write('2',point1.s_base(),point1.s_shoulder(),point1.s_elbow(),point1.s_vwrist(),point1.s_rwrist(),point1.s_gripper(),speed_manu)
	time.sleep(auto_point5_w8)


def start_goto_p6():
	global program
	global speed_manu
	global auto_point6_w8

	point1=point(DB.rdata(program,"point6"))
	serial_config.serial_write('2',point1.s_base(),point1.s_shoulder(),point1.s_elbow(),point1.s_vwrist(),point1.s_rwrist(),point1.s_gripper(),speed_manu)
	time.sleep(auto_point6_w8)


def start_goto_p7():
	global program
	global speed_manu
	global auto_point7_w8


	point1=point(DB.rdata(program,"point7"))
	serial_config.serial_write('2',point1.s_base(),point1.s_shoulder(),point1.s_elbow(),point1.s_vwrist(),point1.s_rwrist(),point1.s_gripper(),speed_manu)
	time.sleep(auto_point7_w8)


def start_goto_p8():
	global program
	global speed_manu
	global auto_point8_w8


	point1=point(DB.rdata(program,"point8"))
	serial_config.serial_write('2',point1.s_base(),point1.s_shoulder(),point1.s_elbow(),point1.s_vwrist(),point1.s_rwrist(),point1.s_gripper(),speed_manu)
	time.sleep(auto_point8_w8)


def start_goto_p9():
	global program
	global speed_manu
	global auto_point9_w8


	point1=point(DB.rdata(program,"point9"))
	serial_config.serial_write('2',point1.s_base(),point1.s_shoulder(),point1.s_elbow(),point1.s_vwrist(),point1.s_rwrist(),point1.s_gripper(),speed_manu)
	time.sleep(auto_point9_w8)


def start_goto_p10():
	global program
	global speed_manu
	global auto_point10_w8

	point1=point(DB.rdata(program,"point10"))
	serial_config.serial_write('2',point1.s_base(),point1.s_shoulder(),point1.s_elbow(),point1.s_vwrist(),point1.s_rwrist(),point1.s_gripper(),speed_manu)
	time.sleep(auto_point10_w8)


while (auto_program_cycles>0) :
	
	if (auto_steps>=1) :
		start_goto_p1()
		print("Point1 Done !")

	if (auto_steps>=2):
		start_goto_p2()
		print("Point2 Done !")

	if (auto_steps>=3):
		start_goto_p3()
		print("Point3 Done !")

	if (auto_steps>=4):
		start_goto_p4()
		print("Point4 Done !")

	if (auto_steps>=5):
		start_goto_p5()
		print("Point5 Done !")

	if (auto_steps>=6):
		start_goto_p6()
		print("Point6 Done !")

	if (auto_steps>=7):
		start_goto_p7()
		print("Point7 Done !")

	if (auto_steps>=8):
		start_goto_p8()
		print("Point8 Done !")

	if (auto_steps>=9):
		start_goto_p9()	
		print("Point9 Done !")

	if (auto_steps==10):
		start_goto_p10()
		print("Point10 Done !")
	auto_program_cycles-=1 