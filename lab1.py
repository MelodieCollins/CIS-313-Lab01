class Node(object):    
	"""    
	A class to represent a node.    
	
	...    
	
	Attributes    
	----------    
	data : int or float        
		An individual character or number to be stored in a node    
	next_node : object of class Node        
		A pointer to the next node in a stack or queue    

	Methods    
	-------    
	setData(data):        
		Updates the value of data attribute of Node    
	setNext(next_node):        
		Updates the value of next_node attribute of Node    
	getData():        
		Returns the value of data attribute    
	getNext():        
		Returns the value of next_node attribute    
	"""    
	def __init__(self, data = None, next_node = None):        
		"""        
		Constructs (or initializes) the attributes for an object of the class        

		...        

		Parameters        
		----------        
		data : int or float            
			An individual character or number to be stored in a node        
		next_node : object of class Node            
			A pointer to the next node in a stack or queue        
		"""        
		self.__data = data        
		self.__next_node = next_node    

	def setData(self, data):        
		'''Set the "data" data field to the corresponding input.'''        
		self.__data = data   

	def setNext(self, next_node):        
		'''Set the "next_node" data field to the corresponding input.'''        
		self.__next_node = next_node  

	def getData(self):        
		'''Return the "data" data field.'''       
		return self.__data 

	def getNext(self):        
		'''Return the "next_node" data field.'''        
		return self.__next_node

class Queue(object):    
	"""    
	A class to represent a queue. First in first out  
	
	...    
	
	Attributes    
	----------    
	head : int, float, or string        
		An individual character or number to be stored in the head    
	tail : int, float, or string        
		An individual character or number to be stored in the tail    

	Methods    
	-------    
	__str__():        
		Returns the queue as a string     
	enqueue(newData):        
		Creates a new node whose data is newData and whose next node is null.        
		Updates head and tail.   
	dequeue():
		Updates head.        
		Returns the head of the Queue.            
	isEmpty():        
		Checks if the Queue is empty.    
	"""   
	def __init__(self, head = None, tail = None):
		"""   
		Constructs (or initializes) the attributes for an object of the class    
		
		...    
		
		Attributes    
		----------    
		head : int, float, or string        
			An individual character or number to be stored in the head    
		tail : int, float, or string        
			An individual character or number to be stored in the tail    
		"""
		self.__head = head
		self.__tail = tail
		self.__queue = []

	def __str__(self):        
		'''Loop through your queue and print each Node's data.'''        
		list_len = len(self.__queue)
		string = "["
		count = 0
		for i in self.__queue:
			count += 1
			string = string + str(i.getData())
			if (list_len - count) != 0:
				string = string + ", "
		string = string + "]"
		return string

	def enqueue(self, newData):        
		'''Create a new node whose data is newData and whose next node is null        
		Update head and tail.'''               
		
		# Create node whose data is newData
		new_node = Node(newData)
		# Set new node's next node to None
		new_node.setNext(None)
		old_tail = self.__tail
		# Update tail
		self.__tail = new_node
		if len(self.__queue) == 0:
			self.__head = new_node
		else:
			# Set old tail's next node to new node
			old_tail.setNext(new_node)
		# Add new node to stack
		self.__queue.append(new_node) 

	def dequeue(self):        
		'''Return the head of the Queue        
		Update head.'''                
		
		try:
			# Raise attribute error on an empty Queue 
			if len(self.__queue) == 0:
				raise AttributeError
			# Remove head from list
			old_head = self.__queue.pop(0)
			# Update head
			self.__head = old_head.getNext()
			# Set next value of old head to none
			old_head.setNext(None)
			# Return old head
			return old_head.getData()

		except AttributeError:
			print("Cannot dequeue from empty queue.")
			raise AttributeError  

	def isEmpty(self):        
		'''Check if the Queue is empty.'''        
		if self.__head == None:
			return True
		else:
			return False

class Stack(object):    
	"""    
	A class to represent a stack. Last in first out  
	
	...    
	
	Attributes    
	----------    
	top : int, float, or string        
		An individual character or number to be stored in the top        

	Methods    
	-------    
	__str__():        
		Returns the stack as a string     
	push(newData):        
		Creates a node whose data is newData and next node is top.        
		Pushes the new node onto the stack and updates the top.          
	pop():
		Returns the Node that currently represents the top of the stack.        
		Updates the top.            
	isEmpty():        
		Checks if the Stack is empty.    
	"""   
	def __init__(self, top = None):        
		"""    
		Constructs (or initializes) the attributes for an object of the class    
		
		...    
		
		Attributes    
		----------    
		top : int, float, or string        
			An individual character or number to be stored in the top    
		"""        
		self.__top = top
		self.__stack = []   

	def __str__(self):        
		'''Loop through your stack and print each Node's data.'''
		list_len = len(self.__stack)
		string = "["
		count = 0
		for i in self.__stack:
			count += 1
			string = string + str(i.getData())
			if (list_len - count) != 0:
				string = string + ", "
		string = string + "]"
		return string           

	def push(self, newData):        
		'''We want to create a node whose data is newData and next node is top.        
		Push this new node onto the stack        
		Update top'''

		# Create node whose data is newData
		new_node = Node(newData)
		# Set new node's next node to current top
		new_node.setNext(self.__top)
		# Push node onto stack
		self.__stack.insert(0, new_node)
		# Update top to new node
		self.__top = new_node           

	def pop(self):        
		''' Return the Node that currently represents the top of the stack.        
		Update top'''

		# Return None on an empty stack
		if self.__top == None:
			return None
		top = self.__top
		#myNode = top.getData()
		# Update top
		self.__top = top.getNext()
		#remove top from list
		self.__stack.pop(0)
		# Return Node that currently represents top of stack
		return top.getData()  

	def isEmpty(self):        
		'''Check if the Stack is empty.'''
		if self.__top == None:
			return True
		else:
			return False

def isPalindrome(s):    
	'''Use your Queue and Stack class to test wheather an input is a palindrome.'''        
	x = s.strip()
	x = x.lower()

	myStack = Stack()
	myQueue = Queue()

	# Push string onto stack and queue
	for i in x:
		myStack.push(i)
		myQueue.enqueue(i)
	# If not same values, not a palindrome 
	if myStack.pop() != myQueue.dequeue():
		return False
	else:
		return True
		
def isPalindromeEC(s):    
	'''Implement if you wish to do the extra credit.'''    
	# Return appropriate value    
	pass





























