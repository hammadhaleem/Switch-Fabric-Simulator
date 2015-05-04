from Queue_Class import *
from Scheduler_Class import *
from Fabric_Class import *
import pprint

pp = pprint.PrettyPrinter(indent=4)
NUMBER_OF_ACTIVE_QUEUES = 5
NUMBER_OF_PACKETS = 5000
SCHEDULER_TYPE = 1 # 0 -> RR , 1-> Islip

def Main(data):
	if SCHEDULER_TYPE is 0:
		S = RoundRobinScheduler(NUMBER_OF_ACTIVE_QUEUES,data)
	if SCHEDULER_TYPE is 1:
		S = iSlipScheduler(NUMBER_OF_ACTIVE_QUEUES,data)
	while True:
	 if S.generate_sequences() == False:
	 	break
	return S.Get_Output()

def generate_data():
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

	return data_list

input_Data =  generate_data()
print "\nInput  :\n",input_Data,"\n"
data_list = Main(input_Data)
print "\nOutput :\n",data_list,"\n"