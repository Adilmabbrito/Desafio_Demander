class ConversorRomano_Arabico:
    def __init__(self):
        self.romano_para_arabico = {
            'I': 1, 
            'V': 5, 
            'X': 10, 
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000}

    def converter(self, numero_romano):
        arabico = 0
        numero_anterior = 0

        for caractere in reversed(numero_romano):
            valor_atual = self.romano_para_arabico.get(caractere, 0)

            if valor_atual < numero_anterior:
                arabico -= valor_atual
            else:
                arabico += valor_atual

            numero_anterior = valor_atual

        return arabico


numero_romano = input("Digite um número romano: ")


conversor = ConversorRomano_Arabico()

try:
    resultado_arabico = conversor.converter(numero_romano)
    print(f'O número romano "{numero_romano}" é equivalente a {resultado_arabico} em algarismos arábicos.')
except Exception as e:
    print(f"Erro: {e}")
