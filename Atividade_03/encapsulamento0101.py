class Viagem:
    """Representa uma viagem de automóvel para cálculo do consumo médio de combustível."""

    def __init__(self, destino: str, distancia_km: float, litros: float):
        self.set_destino(destino)
        self.set_distancia_km(distancia_km)
        self.set_litros(litros)

    # Métodos de acesso (gets e sets) com validação
    def get_destino(self) -> str:
        return self.__destino

    def set_destino(self, destino: str) -> None:
        if not isinstance(destino, str) or destino.strip() == "":
            raise ValueError("Destino deve ser uma string não vazia.")
        self.__destino = destino.strip()

    def get_distancia_km(self) -> float:
        return self.__distancia_km

    def set_distancia_km(self, distancia_km: float) -> None:
        if not isinstance(distancia_km, (int, float)) or distancia_km <= 0:
            raise ValueError("Distância deve ser um número positivo (em km).")
        self.__distancia_km = float(distancia_km)

    def get_litros(self) -> float:
        return self.__litros

    def set_litros(self, litros: float) -> None:
        if not isinstance(litros, (int, float)) or litros <= 0:
            raise ValueError("Quantidade de combustível (litros) deve ser um número positivo.")
        self.__litros = float(litros)

    # Método para calcular o consumo médio (km por litro)
    def consumo(self) -> float:
        return self.__distancia_km / self.__litros


class ViagemUI:
    def menu(self) -> int:
        while True:
            print("\n=== MENU ===")
            print("1 - Calcular")
            print("2 - Fim")
            opcao = input("Escolha uma opção: ").strip()

            if opcao in ("1", "2"):
                return int(opcao)
            else:
                print("Opção inválida. Digite 1 para Calcular ou 2 para Fim.")

    def calculo(self) -> None:
        print("\n--- Cálculo de Consumo Médio ---")

        destino = input("Destino da viagem: ").strip()
        distancia = float(input("Distância percorrida (km): ").replace(",", "."))
        litros = float(input("Quantidade de combustível gasta (litros): ").replace(",", "."))

        try:
            viagem = Viagem(destino, distancia, litros)
        except ValueError as e:
            print(f"Erro: {e}")
            return

        print("\n--- Dados da Viagem ---")
        print(f"Destino: {viagem.get_destino()}")
        print(f"Distância percorrida: {viagem.get_distancia_km():.2f} km")
        print(f"Combustível gasto: {viagem.get_litros():.2f} litros")

        consumo_medio = viagem.consumo()
        print(f"Consumo médio: {consumo_medio:.2f} km por litro")

    def main(self) -> None:
        print("Aplicação para calcular o consumo médio de combustível em uma viagem.")

        while True:
            opcao = self.menu()
            if opcao == 1:
                self.calculo()
            else:
                print("\nPrograma finalizado. Até logo!")
                break


if __name__ == "__main__":
    ui = ViagemUI()
    ui.main()