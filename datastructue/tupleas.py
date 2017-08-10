from collections import namedtuple

Stock = namedtuple('Stock', 'symbol current high low')
stock = Stock('FB', 75.00, 75.03, 74.90)
