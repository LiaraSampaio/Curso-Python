# Em classe normais, __call__ 

class CallMe:
    def __init__(self, phone):
        self.phone = phone
    
    def __call__(self, nome):
        print(nome,'está chamando...', self.phone)

call1 = CallMe('62982692003')
call1('Liara')