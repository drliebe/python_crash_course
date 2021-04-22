#import make_car
#import make_car as mc
#from make_car import make_car
#from make_car import make_car as m_car 
from make_car import *


#my_car = make_car.make_car('Chevy','Cavalier', color='red', year='1998')
#my_car = mc.make_car('Chevy','Cavalier', color='red', year='1998')
#my_car = make_car('Chevy','Cavalier', color='red', year='1998')
#my_car = m_car('Chevy','Cavalier', color='red', year='1998')
my_car = make_car('Chevy','Cavalier', color='red', year='1998')

print(my_car)