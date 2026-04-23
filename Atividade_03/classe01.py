class Retangulo:
    def __init__(self, b, h):
        self.set_base(b)
        self.set_altura(h)
    def set_base(self, v):
        if v >= 0: self.__b = v
        else: raise ValueError()
    def set_altura(self, v):
        if v >= 0: self.__h = v
        else: raise ValueError()
    def get_base(self):
        return self.__b
    def get_altura(self):
        return self.__h
    def calc_area(self):
        return self.__b * self.__h 
    def calc_diagonal(self):
        return math.sqrt(self.__b**2 + self.__h**2)
    
    def __str__(self):
        return f"Eu sou um Retângulo, minha base é {self.__b} e minha altura é {self.__h}"
def retangulo():
        print("Cálculo da área do Retângulo")
        b = float(input("Informe o valor da base: "))
        h = float(input("Informe o valor da altura: "))
        x = Retangulo(b, h)
        area = x.calc_area()
        print(x)
        print(f"Um retângulo com base {x.get_base()} e altura {x.get_altura()} tem área = {area}")
        print(f"Minha diagonal é: calc_diagonal():.2f)")
retangulo()