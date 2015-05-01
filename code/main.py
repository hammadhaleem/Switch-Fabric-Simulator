from Queue_Class import *
from Scheduler_Class import *

NUMBER_OF_ACTIVE_QUEUES = 4
def Main():
	S = Scheduler(NUMBER_OF_ACTIVE_QUEUES)
	S.Test_Queues()

Main()
