import logging
 
logging.basicConfig(filename='test.log',level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s')
logging.config
def add(x,y):
     return x + y

def subtract(x,y):
     return x - y

def multiply(x,y):
    return x * y

def div(x,y):
    return x/y 

num_1 = 10
num_2 = 5

add_result = add(num_1,num_2)
logging.debug('ADD: {} + {} = {}'.format(num_1,num_2,add_result))

sub_result = subtract(num_1,num_2)
logging.debug('SUB: {} - {} = {}'.format(num_1,num_2,sub_result))

mul_result = multiply(num_1,num_2)
logging.debug('MUL: {} * {} = {}'.format(num_1,num_2,mul_result))

div_result = div(num_1,num_2)
logging.debug('ADD: {} / {} = {}'.format(num_1,num_2,div_result))