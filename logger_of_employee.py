
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s:%(message)s')
file_handler = logging.FileHandler('emp.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

class Employee:

    def __init__(self,first,last):
        self.first=first
        self.last=last
        logger.info('Created Employee: {} - {}'.format(self.fullname,self.email))
    
    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first,self.last)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

exp_1 = Employee('payal','kutana')
exp_2 = Employee('rima','jogani')