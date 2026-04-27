class celula:
    def _int_(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.bateria = 100

    def fazer_chamada(self, duração):
        try:
            gasto = int(duração) * 2
            if self.bateria >= gasto:
                self.bateria -= gasto
                print(f"chamada feita por {duração} minutos. Bateria restante: {self.bateria}%")
            else:
                print("Bateria insuficiente.")
        except ValueError:
            print("erro a duraçao ser ser um numero inteiro!")


meu_celular = celula("samsung", "s24")
meu_celular.fazer_chamada("dez")  # Teste de erro