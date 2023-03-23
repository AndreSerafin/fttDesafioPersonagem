# nome, descrição, link para imagem, programa e animador.

class Personagem():
    def __init__(self, nome, descricao, link, programa, animador):
        self._nome = nome
        self._descricao = descricao
        self._link = link
        self._programa = programa
        self._animador = animador
        
    def vizualiza_personagem(self):
        print(f"Nome do personagem: {self._nome}")
        print(f'Descrição do personagem: {self._descricao}')
        print(f'Link: {self._link}')
        print(f'Programa: {self._programa}')
        print(f'Animador: {self._animador}')


op = 0
lista_personagens = []

while (op != 3):
    print('Menu de opções:')
    print('1. Cadastro de personagem ')
    print('2. Vizualização de personagens')
    print('3. Encerrar programa')
    print()

    op_valido = False

    while (not op_valido):
        try:
            op = int(input())
            op_valido = True
        except Exception:
            print('Opção inválida! Digite Novamente.')

    match(op):
        case 1:
            p1 = Personagem(input('Nome do Personagem: '),
                            input('Descrição do Personagem: '),
                            input('Link: '),
                            input('Programa: '),
                            input('Animador: '))
            lista_personagens.append(p1)
        case 2:

            j = 1
            for i in lista_personagens:
                print(f'Personagem {j}')
                i.vizualiza_personagem()
                j += 1
                print()
        case 3:
            pass
        case _:
            print('Opção Inválida:')
    print()
