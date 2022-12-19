import unittest 
import db



"""DATABASE TESTS"""

class TestDb(unittest.TestCase):

	"""CHECK IF EVERY PROGRAM IS ON PLACE"""
	def setUp(self):
		self.fields = ['baudrate', 'port', 'speed', 'step', 'stare', 'home', 'point1', 'point2', 'point3', 'point4', 'point5', 'point6', 'point7', 'point8', 'point9', 'point10', 'lsup', 'linf', 'program']
	def test_ShowDb_allProgInPlace(self):
		for i in range(1,10):
			self.assertNotEqual(0,db.show_db(i))


	
	"""CHECK INTEGRITY OFF ALL JSONS """


	def test_integrity_db(self):
		

		for i in range(1,10):
			db_checked=list(db.show_db(i))

			for j in range(len(db_checked)) :
				self.assertEqual(db_checked[j],self.fields[j])


	def test_read(self):
		pass





