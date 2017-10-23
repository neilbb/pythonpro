import random
import pdb
import logging
import datetime
import pytz

#logging.basicConfig(filename='game.log',level=logging.DEBUG)

class Question:
	answer = None
	text = None


class Add(Question):

	def __init__(self,num1,num2):
		self.answer = num1 + num2
		self.text = '{} + {}'.format(num1,num2)

class Multiply(Question):

	def __init__(self,num1,num2):
		self.answer = num1 * num2
		self.text = '{} * {}'.format(num1,num2)




if __name__ == '__main__':
	pacific = pytz.timezone('US/Pacific')
	eastern = pytz.timezone('US/Eastern')

	print(pacific)
	print(eastern)





