#!/usr/bin/python

from modulo import soma
agenda = {}

def busca(nome):
    if (nome in agenda):
      no = agenda[nome]
      print "Telefone: " + str(no)
      print " -----"
    else:
      print "Contato nao existe"

def insere(nome,tel):
    agenda[nome] = tel

def imprime_agenda():
  for k, v in agenda.iteritems():
    print k, v

def main():
    insere('Bruno',1588)
    insere('Joao',1088)

    imprime_agenda()
    print "Modulo Soma 3 e 4 "
    print soma(3,4)
    nome = raw_input("Digite seu nome ")
    print "Ola " + nome
    a = []
    print a
    a.append(10)
    a.append(100)
    a.append(99)
    print a
    a.remove(10)
    print a
    print a[0]
    print a[1]

    busca(nome)

if __name__ == '__main__' : main()
