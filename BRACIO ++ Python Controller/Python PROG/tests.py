import unittest 
import db
from random import randint



"""DATABASE TESTS -UNIT TESTS"""

class TestDb(unittest.TestCase):

	""" SET UP TEST PARAMETER"""
	def setUp(self):
		
		self.fields = ['baudrate', 'port', 'speed', 'step', 'home', 'point1', 'point2', 'point3', 'point4', 'point5', 'point6', 'point7', 'point8', 'point9', 'point10', 'lsup', 'linf', 'program']
		self.DB=db.Database()
		self.dummy_prog="dummy"



	"""CHECK IF THE JSON FILE IS PRESENT AND HAS THE CORECT NAME - database.json""" 	

	def test_ShowDb_allProgInPlace(self):	
		
		self.assertNotEqual(0,self.DB.show_db())
	
	"""CHECK INTEGRITY OFF ALL JSONS PROGRAMS - CHECK EVERY FIELD OF JSON PRORAM TO BE ON PLACE"""
	def test_integrity_db(self):
		for i in range(1,10):
			prog="prog"+str(i)
			for j in range(0,len(self.fields)):				
				self.assertEqual(self.fields[j],list(self.DB.show_db()[prog])[j])


	""" MAKE A FULL READ OF ONE PROGRAM -randomly chosen """

	def test_read_db(self):
		rnd=randint(0,10)
		prog="prog"+str(rnd)
		for j in self.fields :
			if j!="stare" :
				self.assertNotEqual(0,self.DB.rdata(prog,j))


	""" MAKE A DUMMY WRITE  """

	def test_write_db(self):
		#WRITE A VALUE
		value=str(randint(1,1000))
		self.DB.wdata(self.dummy_prog,"baudrate",value)
		#READ IT BACK TO CHECK IT
		self.assertEqual(value,self.DB.rdata(self.dummy_prog,"baudrate"))


		

		
"""GUI WRITING AND READING FROM DB - FUNCTIONAL TESTS"""



