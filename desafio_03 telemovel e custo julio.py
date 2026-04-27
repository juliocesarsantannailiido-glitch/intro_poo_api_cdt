class Celular:
    def __init__(self,marca,modelo):
        self.marca, self.modelo = marca,modelo
        self.bateria = 100



    def fazer_Chamada(self,custo_bateria):
        print(f"\n-- Chamada no {self.modelo}--")
        try:
            self.bateria -= custo_bateria
        except TypeError:
            print("Erro: O custo da bateria deve ser um número inteiro.")
        else:
            print(f"Sucesso! Bateria atual: {self.bateria}%")
        finally:
            print("Sistema Finalizado.")
            meu_celular = Celular("samsung", "s24")
            meu_celular.fazer_Chamada("muito")