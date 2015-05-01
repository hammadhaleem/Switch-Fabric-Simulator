from Queue_Class import *


class StandardScheduler(object):
	"""This is a template for a Scheduler which will manage input and output Queues."""

	input_queue_object = None
	output_queue_object = None
	def __init__(self, number_of_queue,data):
		super(StandardScheduler, self).__init__()
		self.number_of_queue = number_of_queue
		self.input_queue_object = SuperQueue(int(self.number_of_queue))
		self.output_queue_object = SuperQueue(int(self.number_of_queue))

		self.input_queue_object.insert_data_in_queues(data)

	def Test_Queues(self):
		print "Input Queues"
		self.input_queue_object.debug()
		print "\nQutput Queues"
		self.output_queue_object.debug()

	def Packet_Exchange(self,from_super_queue,to_super_queue,from_queue,to_queue):
		print from_super_queue, to_super_queue, from_queue, to_queue