import logging

logging.basicConfig(filename='emp.log',level=logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s')
class Employee:

    def __init__(self,first,last):
        self.first=first
        self.last=last
        logging.info('Created Employee: {} - {}'.format(self.fullname,self.email))
    
    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first,self.last)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

exp_1 = Employee('payal','kutana')
exp_2 = Employee('rima','jogani')