from Queue_Class import *
from Scheduler_Class import *
from Fabric_Class import *

NUMBER_OF_ACTIVE_QUEUES = 400

def Main(data):

	S = RoundRobinScheduler(NUMBER_OF_ACTIVE_QUEUES,data)

	S.generate_sequences_robin()
	print S.Status()
	S.generate_sequences_robin()
	print S.Status()

	# S.Packet_Exchange((1,1),1)
	# S.Packet_Exchange((1,0),0)
	# S.Packet_Exchange((0,1),1)
	# S.Packet_Exchange((0,0),0)
	
	# S.generate_sequences_robin()
	# S.generate_sequences_robin()
	# S.generate_sequences_robin()
	# S.generate_sequences_robin()
	# S.generate_sequences_robin()

	#print "\nOutput : ",S.Get_Output()

data_list = []

# data_list.append({'timestamp' : time.time(),'outport' : 0,'data' : "this is my data", 'source' : 0})
# data_list.append({'timestamp' : time.time(),'outport' : 0,'data' : "this is my data", 'source' : 1})
# data_list.append({'timestamp' : time.time(),'outport' : 0,'data' : "this is my data", 'source' : 2})
# data_list.append({'timestamp' : time.time(),'outport' : 0,'data' : "this is my data", 'source' : 3})

# data_list.append({'timestamp' : time.time(),'outport' : 1,'data' : "this is my data", 'source' : 0})
# data_list.append({'timestamp' : time.time(),'outport' : 1,'data' : "this is my data", 'source' : 1})
# data_list.append({'timestamp' : time.time(),'outport' : 1,'data' : "this is my data", 'source' : 2})
# data_list.append({'timestamp' : time.time(),'outport' : 4,'data' : "this is my data", 'source' : 4})

# data_list.append({'timestamp' : time.time(),'outport' : 2,'data' : "this is my data", 'source' : 0})
# data_list.append({'timestamp' : time.time(),'outport' : 2,'data' : "this is my data", 'source' : 1})
# data_list.append({'timestamp' : time.time(),'outport' : 2,'data' : "this is my data", 'source' : 2})
# data_list.append({'timestamp' : time.time(),'outport' : 2,'data' : "this is my data", 'source' : 3})

# data_list.append({'timestamp' : time.time(),'outport' : 3,'data' : "this is my data", 'source' : 0})
# data_list.append({'timestamp' : time.time(),'outport' : 3,'data' : "this is my data", 'source' : 1})
# data_list.append({'timestamp' : time.time(),'outport' : 3,'data' : "this is my data", 'source' : 2})
# data_list.append({'timestamp' : time.time(),'outport' : 3,'data' : "this is my data", 'source' : 3})

data_list.append({'timestamp' : time.time(),'outport' : 1 ,'data' : "this is my data", 'source' : 1})
data_list.append({'timestamp' : time.time(),'outport' : 1 ,'data' : "this is my data", 'source' : 0})
data_list.append({'timestamp' : time.time(),'outport' : 0 ,'data' : "this is my data", 'source' : 0})
data_list.append({'timestamp' : time.time(),'outport' : 0 ,'data' : "this is my data", 'source' : 1})
Main(data_list)
