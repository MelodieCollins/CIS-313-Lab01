import lab1
import unittest

class T0_TestingQueue(unittest.TestCase):    
	
	def test_basic_enqueue(self):        
		# testing the basic enqueue operation        
		print("\n")        
		q = lab1.Queue()        
		q.enqueue(1)        
		q.enqueue(2)        
		q.enqueue(3)        
		q.enqueue(4)        
		
		print(q.__str__())

		self.assertEqual(q.__str__(), "[1, 2, 3, 4]")        
		print("\n")

class T1_TestingStack(unittest.TestCase):    
	
	def test_is_empty_false(self):        
		# testing if queue is empty       
		print("\n")        
		s = lab1.Stack()        
		s.push("4")        
		print("return false if the stack is not empty")        
		self.assertEqual(s.isEmpty(), False)        
		print("\n")

class T2_TestingPalindrome(unittest.TestCase):    
	
	def test_basic_string(self):        
		# testing with basic string        
		print("\n")        
		string = "hello"        
		p = lab1.isPalindrome(string)        
		print("The string being tested is -> ", string)        
		self.assertEqual(p, False)        
		print("\n")

class T3_TestingStack(unittest.TestCase):    
	
	def test_pop_empty_stack(self):   
		# testing pop from empty stack raises exception   
		print("\n")        
		s = lab1.Stack()              
		self.assertEqual(s.pop(), None)       
		print("\n")

class T4_TestingQueue(unittest.TestCase):    
	
	def test_dequeue_empty_queue(self):   
		# testing dequeue from empty stack raises exception   
		print("\n")        
		s = lab1.Queue()              
		with self.assertRaises(Exception):           
			s.dequeue()       
		print("\n")

class T5_TestingPalindrome(unittest.TestCase):    
	
	def test_palindrome_string(self):        
		# testing with basic palindrome string        
		print("\n")        
		string = "TaCo CaT"        
		p = lab1.isPalindrome(string)        
		print("The string being tested is -> ", string)        
		self.assertEqual(p, True)        
		print("\n")

class T6_TestingStack(unittest.TestCase):    
	
	def test_basic_push(self):        
		# testing the basic push operation on empty stack       
		print("\n")        
		q = lab1.Stack()        
		q.push(1)               
		self.assertEqual(q.__str__(), "[1]")
		print("\n")

class T7_TestingStack(unittest.TestCase):    
	
	def test_basic_pop(self):        
		# testing the basic pop operation on stack with one item      
		print("\n")        
		q = lab1.Stack()
		q.push(1)                      
		self.assertEqual(q.pop(), 1)
		print("\n")

class T8_TestingQueue(unittest.TestCase):    
	
	def test_basic_enqueue_on_empty_queue(self):        
		# testing the basic enqueue operation on empty queue       
		print("\n")        
		q = lab1.Queue()        
		q.enqueue(1)                
		self.assertEqual(q.dequeue(), 1)
		print("\n")

if __name__ == '__main__':    
	unittest.main()