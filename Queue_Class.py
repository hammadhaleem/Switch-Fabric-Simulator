import time 

class Queue:

	def __init__(self, lst=[]):
		self.queue = []
		self.out = 0

	def insert(self , obj):
		self.queue.append(obj)

	def process(self):
		try:
			data = self.queue[0]
			del self.queue[0]
			return data
		except:
			return None

	def debug(self):
		return self.queue

class SuperQueue:

	input_streams = {}
	number_of_queues = 0

	def __init__(self, default_number_queue = 4):
		for i in xrange(0,default_number_queue):
			self.input_streams[i] = {
				'outport' : i, 
				'queue'  : Queue()
				}
			self.number_of_queues = default_number_queue

	# get a list of input obejcts and allocate them to different subques.
	# if a object want to route to a 
	# packet = {
	# 	'timestamp' : xxxxx,
	# 	'outport' : xxxx,
	# 	'data' : xxxxxxxxxxx
	# }

	def insert_data_in_queues(self,data_list):
		for packet in data_list:
			Stream = self.input_streams[packet['outport']]
			Stream['queue'].insert(packet)
			self.input_streams[packet['outport']]

	def debug(self):
		for i in self.input_streams:
			print i , self.input_streams[i]['queue'].debug()

# Testing of inut data Queue

# Q= SuperQueue()

# data_list = []
# data_list.append({'timestamp' : time.time(),'outport' : 0,'data' : "this is my data", 'source' : 0})
# data_list.append({'timestamp' : time.time(),'outport' : 0,'data' : "this is my data", 'source' : 0})
# data_list.append({'timestamp' : time.time(),'outport' : 0,'data' : "this is my data", 'source' : 0})
# data_list.append({'timestamp' : time.time(),'outport' : 0,'data' : "this is my data", 'source' : 0})

# data_list.append({'timestamp' : time.time(),'outport' : 1,'data' : "this is my data", 'source' : 1})
# data_list.append({'timestamp' : time.time(),'outport' : 1,'data' : "this is my data", 'source' : 1})
# data_list.append({'timestamp' : time.time(),'outport' : 1,'data' : "this is my data", 'source' : 1})
# data_list.append({'timestamp' : time.time(),'outport' : 1,'data' : "this is my data", 'source' : 1})

# data_list.append({'timestamp' : time.time(),'outport' : 2,'data' : "this is my data", 'source' : 2})
# data_list.append({'timestamp' : time.time(),'outport' : 2,'data' : "this is my data", 'source' : 2})
# data_list.append({'timestamp' : time.time(),'outport' : 2,'data' : "this is my data", 'source' : 2})
# data_list.append({'timestamp' : time.time(),'outport' : 2,'data' : "this is my data", 'source' : 2})

# data_list.append({'timestamp' : time.time(),'outport' : 3,'data' : "this is my data", 'source' : 3})
# data_list.append({'timestamp' : time.time(),'outport' : 3,'data' : "this is my data", 'source' : 3})
# data_list.append({'timestamp' : time.time(),'outport' : 3,'data' : "this is my data", 'source' : 3})
# data_list.append({'timestamp' : time.time(),'outport' : 3,'data' : "this is my data", 'source' : 3})


# Q.insert_data_in_queues(data_list)
# Q.debug()
