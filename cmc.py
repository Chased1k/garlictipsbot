import urllib
import json
from utils import utils
from decimal import *

quanpriceurl = 'https://coinlib.io/api/v1/coin?key=fc23d7cb020f2ce1&symbol=QUAN'
dashpriceurl = 'https://coinlib.io/api/v1/coin?key=fc23d7cb020f2ce1&symbol=DASH'

utils = utils()
cursor = utils.get_mysql_cursor()

sql = "TRUNCATE TABLE rates"
cursor.execute(sql)

response = urllib.urlopen(quanpriceurl)
data = json.loads(response.read())
quanprice = round(Decimal(data[0]['price']),8)

response = urllib.urlopen(dashpriceurl)
data = json.loads(response.read())
dashprice = round(Decimal(data[0]['price']),8)

sql = "INSERT INTO rates (pair,rate) VALUES (%s, %s)"
pair = "QUAN/DASH"
rate = quanprice/dashprice
cursor.execute(sql, (pair,rate,))

pair = "DASH/QUAN"
rate = dashprice/quanprice
cursor.execute(sql, (pair,rate,))
