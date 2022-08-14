def sayName1():
    print(f'__name__ in first.py is: {__name__}')

sayName1()

from second import sayName2
from third import sayName3