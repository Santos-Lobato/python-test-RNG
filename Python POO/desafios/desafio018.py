class churras:
    consumo_padrao: float = 0.400
    preco_kg: float = 82.40

    def __init__(self, titulo, quant=0):
        self.titulo = titulo
        self.quant = quant

    def __str__(self):
        return f'Esse é o {self.titulo}, com {self.quant} pessoas. NÃO PERCA!'

    def calcular_qtd_carne(self) -> float:
        return self.quant * churras.consumo_padrao

    def calcular_custo_total(self) -> float:
        return self.calcular_qtd_carne() * churras.preco_kg

    def calcular_custo_individual(self) -> float:
        return self.calcular_custo_total() / self.quant

    def analisar(self):
        print(f'===========Analisando {self.titulo}=============')
        print(f'Cada participante comerá {churras.consumo_padrao}KG e cada KG custa R$: {churras.preco_kg:,.2f}')
        print(f'Recomendo comprar {self.calcular_qtd_carne():.3f}KG de carne')
        print(f'O custo total será de R$: {self.calcular_custo_total():,.2f}')
        print(f'Cada pessoa pagará R$: {self.calcular_custo_individual():.2f} para participar.')


c1 = churras('Churras Regadão', 100)
c1.analisar()
print(c1)

#CONSIDERE:
# Consumo padrão: 400g por pessoa
# Preço: R$: 82,40/KG

