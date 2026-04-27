class celular:
    def __init__(self, marca, modelo):
        self.marca, self.modelo = marca, modelo

    def verificar_status(self):
        try:
            entrada = input(f"bateria do {self.modelo}:")
            nivel = float(entrada)
            if nivel < 0 or nivel > 100:
                print(f"valor invalido! digite de 0 a 100.")
            elif nivel < 15:
                print(f"bateria em {nivel}%! carrega isso ae!")
            elif nivel > 85:
                print(f"bateria em {nivel}%! ta mec")
            else:
                print(f"bateira em {nivel}% ta suave")
        except ValueError:
            print("erro: erro digite apenas numeros!")

cell = celular("samsung", "s24")
cell.verificar_status()