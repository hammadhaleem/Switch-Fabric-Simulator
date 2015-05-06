from Queue_Class import *
from Scheduler_Class import *
from Fabric_Class import *
import pprint
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

pp = pprint.PrettyPrinter(indent=4)
NUMBER_OF_ACTIVE_QUEUES = 6
NUMBER_OF_PACKETS = 5000
SCHEDULER_TYPE = 0 # 0 -> RR , 1-> Islip


#########Configration goes above this line ######################
NUMBER_OF_ACTIVE_QUEUES = NUMBER_OF_ACTIVE_QUEUES + 1


def Main(data):
	if SCHEDULER_TYPE == 0:	
		S_1 = RoundRobinScheduler(NUMBER_OF_ACTIVE_QUEUES,data)
		while S_1.generate_sequences():
		 	pass
		return S_1.Get_Output()
	elif SCHEDULER_TYPE == 1:
		S_2 = iSlipScheduler(NUMBER_OF_ACTIVE_QUEUES,data)
		while S_2.generate_sequences() :
		 	pass
		return S_2.Get_Output()

def generate_uniform_traffic(number_of_cards,packets=1):
	data_list = []
	for m in range(packets):
		for i in range(0,number_of_cards):
			for j in range(0,number_of_cards):
				obj = {'timestamp' : time.time(),'outport' : i ,'data' : "this is my data", 'source' : j}
				data_list.append(obj)
	return data_list

def generate_bursty_traffic(number_of_cards, number_of_active_outputs,packets=1):
	data_list = []
	for m in range(packets):
		for j in xrange(0,number_of_cards):
			for i in xrange(0,number_of_active_outputs):
				obj = {'timestamp' : time.time(),'outport' : i ,'data' : "this is my data", 'source' : j}
				data_list.append(obj)
	return data_list

def get_average_time(data_list):
	number = 0.0
	for obj in data_list:
		number = number + obj['time_out'] - obj['timestamp'] 
	return number, len(data_list)

def run_analysis(multiplier,type_in=0):
	if type_in == 0 :
		input_data =  generate_uniform_traffic(5,multiplier)
	else:
		input_data =  generate_bursty_traffic(5,2,multiplier) # sources are bursty 
	data_list = Main(input_data)
	sum_of_diff, number = get_average_time(data_list)
	return (sum_of_diff/number) , number


pairs = []
plt1 =plt
for multiplier in xrange(1,75):
	avg,number = run_analysis(multiplier,1)
	print multiplier,avg,number
	pairs.append((number,avg))

plt1.plot([p[0] for p in pairs], [p[1] for p in pairs], '.')

pairs = []
for multiplier in xrange(1,75):
	avg,number = run_analysis(multiplier,0)
	print multiplier,avg,number
	pairs.append((number,avg))

plt.plot([p[0] for p in pairs], [p[1] for p in pairs], '.')
plt1.show()
plt.show()

