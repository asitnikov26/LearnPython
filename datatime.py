#Напечатайте в консоль даты: вчера, сегодня, месяц назад
from datetime import datetime, timedelta
import dateutil.relativedelta
import locale
locale.setlocale(locale.LC_ALL, "russian")

delta = timedelta(days=1)
delta1 = timedelta(weeks=4)
delta12 = dateutil.relativedelta.relativedelta(months=1)

dt_now = datetime.now()

dt_tom = dt_now + delta
dt_yest = dt_now - delta
dt_month = dt_now - delta1
dt_month1 = dt_now - delta12

print(dt_tom.strftime('%A %d %B %Y'))
print(dt_yest.strftime('%A %d %B %Y'))
print(dt_month.strftime('%A %d %B %Y'))
print(dt_month1.strftime('%A %d %B %Y'))
