import unittest
from encotel import encotel

class EncotelTestCase(unittest.TestCase):
	
	def test_a_b_c_deve_ser_2(self):
		self.assertEquals(encotel('a'), '2')
		self.assertEquals(encotel('b'), '2')
		self.assertEquals(encotel('c'), '2')
	
	def test_d_e_f_deve_ser_3(self):
		self.assertEquals(encotel('d'), '3')
		self.assertEquals(encotel('e'), '3')
		self.assertEquals(encotel('f'), '3')
	
	def test_g_h_i_deve_ser_4(self):
		self.assertEquals(encotel('g'), '4')
		self.assertEquals(encotel('h'), '4')
		self.assertEquals(encotel('i'), '4')
	
	def test_j_k_l_deve_ser_5(self):
		self.assertEquals(encotel('j'), '5')
		self.assertEquals(encotel('k'), '5')
		self.assertEquals(encotel('l'), '5')
	
	def test_m_n_o_deve_ser_6(self):
		self.assertEquals(encotel('m'), '6')
		self.assertEquals(encotel('n'), '6')
		self.assertEquals(encotel('o'), '6')

	def test_p_q_r_s_deve_ser_7(self):
		self.assertEquals(encotel('p'), '7')
		self.assertEquals(encotel('q'), '7')
		self.assertEquals(encotel('r'), '7')
		self.assertEquals(encotel('s'), '7')
		
	def test_t_u_v_deve_ser_8(self):
		self.assertEquals(encotel('t'), '8')
		self.assertEquals(encotel('u'), '8')
		self.assertEquals(encotel('v'), '8')
	
	def test_w_x_y_z_deve_ser_9(self):
		self.assertEquals(encotel('w'), '9')
		self.assertEquals(encotel('x'), '9')
		self.assertEquals(encotel('y'), '9')
		self.assertEquals(encotel('z'), '9')
	
	def test_qualquer_coisa_retorna_ela_mesmo(self):
		self.assertEquals(encotel('1'), '1')
		self.assertEquals(encotel('0'), '0')
		self.assertEquals(encotel('-'), '-')
		
	def test_atw_deve_ser_289(self):
		self.assertEquals(encotel('atw'), '289')
unittest.main()