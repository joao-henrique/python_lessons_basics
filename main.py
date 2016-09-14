#!/usr/bin/python

from modulo import soma

def main():
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

if __name__ == '__main__' : main()
