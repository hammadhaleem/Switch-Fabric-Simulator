from Queue_Class import *
import time
class StandardScheduler(object):

	def __init__(self, number_of_queue,data):
		super(StandardScheduler, self).__init__()
		self.number_of_queue = number_of_queue
		self.input_queue_object = SuperMultiQueue(int(self.number_of_queue))
		self.output_queue_object = SuperMultiQueue(int(self.number_of_queue))
		self.input_queue_object.insert_data_in_queues(data)

	def Test_Queues(self):
		print "Input Queues"
		self.input_queue_object.debug()
		print "\nQutput Queues"
		self.output_queue_object.debug()

	def Get_Output(self):
		return self.output_queue_object.get_data_stream()

	# ((input port, output) , output_Card)
	def Packet_Exchange(self,set_inp,set_out):
		try:
			data = self.input_queue_object.pop_from_queue(set_inp)
			fake_list = [data]
			out = data['source']
			data['source']= set_out 
			data['outport'] = set_out
			data['time_out'] =time.time()
			self.output_queue_object.insert_data_in_queues(fake_list)
			return True
		except:
			pass
			return False

	def Status(self):
		return self.input_queue_object.generate_input_status()