import urllib3
from bs4 import BeautifulSoup
from sqlighter import SQLighter
from parser1 import parser1
from parser2 import parser2
from parser3 import parser3
db = SQLighter('db.db')
db.clearcomp()
db.clearcours()
parser1()
parser3()
parser2()



