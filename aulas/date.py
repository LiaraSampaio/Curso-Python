# datetime(ano, mes, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# timezones (pytz)

from datetime import datetime, timedelta
from pytz import timezone

data_br = '24/09/1991'
data_fmt = '%d/%m/%Y'
data = datetime.strptime(data_br, data_fmt)
print(data.strftime(data_fmt))

dt = datetime.now(timezone('America/Sao_Paulo'))
print(dt)

delta = timedelta(days=10, hours=2)
print(dt - delta)