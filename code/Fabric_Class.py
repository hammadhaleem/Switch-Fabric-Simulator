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

		# Request
		data = {}
		for keys in input_status :
			obj = input_status[keys]
			data[keys] = []
			for ob in obj:
				if obj[ob] > 0 :
					data[keys].append(ob)
		input_status = data
		self.pointer = pointer

		#Debug
		# pp.pprint (self.pointer)
		# pp.pprint (input_status)

		# print "\n"

		#Grant
		actions =[]
		allocated = []
		for keys in self.pointer:
			if self.pointer[keys]['pointer'] is None:
				for out in  input_status[keys]:
						try:
							if out not in allocated:
								self.pointer[keys]['pointer'] = out
								self.pointer[keys]['count'] = self.pointer[keys]['count'] - 1
								allocated.append(out)
								actions.append([(keys,out),out])
								del input_status[keys][input_status[keys].index(out)]
						except :
							pass 
			elif self.pointer[keys]['pointer'] is not None:

				if (len(input_status[keys]) > 0):
					pin = self.pointer[keys]['pointer'] +1
					# print input_status[keys], pin
					while  True:
						if pin in input_status[keys]:
							self.pointer[keys]['count'] = self.pointer[keys]['count'] - 1
							allocated.append(pin)
							actions.append([(keys,pin),pin])
							del input_status[keys][input_status[keys].index(pin)]
							break

						self.pointer[keys]['pointer'] = self.pointer[keys]['pointer'] + 1
						if self.pointer[keys]['pointer']  > number_of_queue:
							self.pointer[keys]['pointer']  = 0 
							pin = self.pointer[keys]['pointer']
						else:
							pin = self.pointer[keys]['pointer'] +1
						# print input_status[keys], pin

		#Debug
		pp.pprint(actions)
		# pp.pprint (self.pointer)
		# pp.pprint (input_status)
		# # Grant Sequence

		for i in actions:
			self.Packet_Exchange(i[0],i[1])

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