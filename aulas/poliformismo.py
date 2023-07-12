
from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem
    
    @abstractmethod
    def enviar(self) -> bool:
        ...
    
class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print('E-mail: enviando -', self.mensagem)
        return True

class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print('SMS: enviando -', self.mensagem)
        return False

def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print('Notificação enviada')
    else:
        print('Notificação NÃO enviada')

notificacao_email = NotificacaoEmail('Testando email')
notificar(notificacao_email)
print()
notificacao_sms = NotificacaoSMS('Testando SMS')
notificar(notificacao_sms)