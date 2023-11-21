"""
Chain of responsibility(COR) é um padrão comportamental que tema  aintenção de
evitar o acoplamento do remetende de uma solicitação ao seu receptor. ao dar
a mais de um objeto a oportunidade de tratar a solicitação. encadear os
objetos receptores repassando a solicitação ao longo da cadeia até que um
objeto a trate.
"""


def handler_ABC(letter: str):
    letters = ['a', 'b', 'c']
    if letter.lower() in letters:
        return f'consegui tratar a letra: {letter}'
    return handler_DEF(letter)


def handler_DEF(letter: str):
    letters = ['d', 'e', 'f']
    if letter.lower() in letters:
        return f'consegui tratar a letra: {letter}'
    return unsolved(letter)


def unsolved(letter: str):
    return f'não conseguimos tratar: {letter}'


if __name__ == '__main__':
    print(handler_ABC('g'))
    print(handler_ABC('b'))
    print(handler_ABC('f'))
