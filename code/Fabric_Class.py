from Queue_Class import *
from Scheduler_Class import *
import pprint

pp = pprint.PrettyPrinter(indent=4,depth=4)

class RoundRobinScheduler(StandardScheduler):

	def __init__(self, number_of_queue,data):
		super(StandardScheduler, self).__init__()
		self.number_of_queue = number_of_queue
		self.input_queue_object  = SuperMultiQueue(int(self.number_of_queue))
		self.output_queue_object = SuperMultiQueue(int(self.number_of_queue))
		self.input_queue_object.insert_data_in_queues(data)

		self.pointer = self.create_state_variable()

	def generate_sequences_robin(self):
		number_of_queue = self.number_of_queue
		input_status =  self.Status()
		pointer = self.pointer
		# pp.pprint( input_status)
		# pp.pprint( pointer )

		for key_1 in input_status:
			for key_2 in input_status[key_1]:
				data = input_status[key_1][key_2]
				if ( data != 0 ) and pointer[key_1]['pointer'] is None:
					 pointer[key_1]['pointer'] = key_1
					 input_status[key_1][key_2] = input_status[key_1][key_2] - 1
					 print (key_1,pointer[key_1]['pointer']),pointer[key_1]['pointer']					 
					 self.Packet_Exchange((key_1,pointer[key_1]['pointer']),pointer[key_1]['pointer'])
					 break

				if (data != 0) and pointer[key_1]['pointer'] is not None:
					pointer[key_1]['pointer'] = pointer[key_1]['pointer']  + 1
					if pointer[key_1]['pointer'] >= number_of_queue:
						print "\n",number_of_queue, pointer[key_1]['pointer']
						pointer[key_1]['pointer'] = 0
						print (key_1,pointer[key_1]['pointer']),pointer[key_1]['pointer']					 
					 	self.Packet_Exchange((key_1,pointer[key_1]['pointer']),pointer[key_1]['pointer'])
					 	break


		self.pointer = pointer
		print "\n",pointer, input_status
	def create_state_variable(self):
		states = {}
		data =self.Status()
		for cards in data : 
			obj = {}
			obj['pointer'] = None
			obj['count'] = 0
			obj['max'] = self.number_of_queue
			for keys in data[cards] :

				obj['count'] = obj['count'] +  data[cards][keys]
			states[cards] =obj
		return states