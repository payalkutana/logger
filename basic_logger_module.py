import logging
import logger_of_employee

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler('test.log')
#only error log's will be stored
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

def add(x,y):
     return x + y

def subtract(x,y):
     return x - y

def multiply(x,y):
    return x * y

def div(x,y):
    try:
        result = x/y
    except ZeroDivisionError:
        logger.exception('Tried to divided by zero')
    else:
        return result
    

num_1 = 10
num_2 = 0

add_result = add(num_1,num_2)
logger.debug('ADD: {} + {} = {}'.format(num_1,num_2,add_result))

sub_result = subtract(num_1,num_2)
logger.debug('SUB: {} - {} = {}'.format(num_1,num_2,sub_result))

mul_result = multiply(num_1,num_2)
logger.debug('MUL: {} * {} = {}'.format(num_1,num_2,mul_result))

div_result = div(num_1,num_2)
logger.debug('ADD: {} / {} = {}'.format(num_1,num_2,div_result))