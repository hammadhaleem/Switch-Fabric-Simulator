from Queue_Class import *

class Scheduler(object):
	"""This is a template for a Scheduler which will manage input and output Queues."""

	input_queue_object = None
	output_queue_object = None
	def __init__(self, number_of_queue):
		super(Scheduler, self).__init__()
		self.number_of_queue = number_of_queue
		self.input_queue_object = SuperQueue(int(self.number_of_queue))
		self.output_queue_object = SuperQueue(int(self.number_of_queue))

	def Test_Queues(self):
		print "Input Queues"
		self.input_queue_object.debug()
		print "\nQutput Queues"
		self.output_queue_object.debug()



		