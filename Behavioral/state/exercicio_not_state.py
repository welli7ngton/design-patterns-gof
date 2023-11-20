class Luz:
    def __init__(self):
        self.ligada = False

    def ligar(self):
        if not self.ligada:
            print("Luz ligada.")
            self.ligada = True
        else:
            print("A luz já está ligada.")

    def desligar(self):
        if self.ligada:
            print("Luz desligada.")
            self.ligada = False
        else:
            print("A luz já está desligada.")


# Uso da classe
luz = Luz()
luz.ligar()
luz.desligar()
