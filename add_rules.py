from rules import Rules, Rent, Job, Sell
#Object | Time | Fee | Place | Signature


def add_rules(): #testando, apenas com o contrato de locação
    print('Agora vamos adicionar as cláusulas.')
    a = str(input('Objeto: ->'))
    b = str(input('Tempo: ->'))
    c = str(input('Multa: ->'))
    d = str(input('Local: ->'))
    x = Rules(a, b, c, d)
    return x.place(), x.fee(), x.time(), x.object()


def add_specific():
    pass