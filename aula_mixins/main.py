# from log import LogFileMixin, LogPrintMixin

# lp = LogPrintMixin()
# lp.log_error('Errado')
# lp.log_success('Correto')

# lf = LogFileMixin()
# lf.log_error('qualquer coisa')
# lf.log_success('Que legal')

from log import LogFileMixin, LogPrintMixin

from eletronico import Smartphone

samsung_s = Smartphone('Samsung S')
iphone = Smartphone('iPhone 13')

samsung_s.ligar()
iphone.desligar()