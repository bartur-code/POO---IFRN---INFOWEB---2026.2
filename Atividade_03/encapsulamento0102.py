class Pais:
    """Representa um país para cálculo da densidade demográfica."""

    def __init__(self, nome: str, populacao: int, area: float):
        self.set_nome(nome)
        self.set_populacao(populacao)
        self.set_area(area)

    # Métodos de acesso (gets e sets) com validação
    def get_nome(self) -> str:
        return self.__nome

    def set_nome(self, nome: str) -> None:
        if not isinstance(nome, str) or nome.strip() == "":
            raise ValueError("Nome deve ser uma string não vazia.")
        self.__nome = nome.strip()

    def get_populacao(self) -> int:
        return self.__populacao

    def set_populacao(self, populacao: int) -> None:
        if not isinstance(populacao, int) or populacao <= 0:
            raise ValueError("População deve ser um número inteiro positivo.")
        self.__populacao = populacao

    def get_area(self) -> float:
        return self.__area

    def set_area(self, area: float) -> None:
        if not isinstance(area, (int, float)) or area <= 0:
            raise ValueError("Área deve ser um número positivo (em km²).")
        self.__area = float(area)

    # Método para calcular a densidade demográfica (hab/km²)
    def densidade(self) -> float:
        return self.__populacao / self.__area


class PaisUI:
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
        print("\n--- Cálculo de Densidade Demográfica ---")

        nome = input("Nome do país: ").strip()
        populacao = int(input("População (habitantes): "))
        area = float(input("Área (km²): ").replace(",", "."))

        try:
            pais = Pais(nome, populacao, area)
        except ValueError as e:
            print(f"Erro: {e}")
            return

        print("\n--- Dados do País ---")
        print(f"Nome: {pais.get_nome()}")
        print(f"População: {pais.get_populacao()}")
        print(f"Área: {pais.get_area():.2f} km²")

        densidade = pais.densidade()
        print(f"Densidade demográfica: {densidade:.2f} hab/km²")

    def main(self) -> None:
        print("Aplicação para calcular a densidade demográfica de um país.")

        while True:
            opcao = self.menu()
            if opcao == 1:
                self.calculo()
            else:
                print("\nPrograma finalizado. Até logo!")
                break


if __name__ == "__main__":
    ui = PaisUI()
    ui.main()