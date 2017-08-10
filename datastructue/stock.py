import datetime


def middle(stock, date):
    symbol, current, high, low = stock
    return ((high + low) / 2, date)


stock = ('FB', 75.00, 75.03, 74.90)
mid_value, date = middle(stock, datetime.date(2014, 1, 2))
print(mid_value)
