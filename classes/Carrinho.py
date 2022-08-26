#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  :
# Created Date:
# version ='1.0'
# ---------------------------------------------------------------------------

from classes.Endereco import Endereco
from classes.Produto import Produto
from classes.PessoaFisica import PessoaFisica

# Esta classe deverá permitir a inserção de items, bem como a atualização da quantidade de
# produtos em um item

class Carrinho:

    def __init__(self):
        # Chave é o id do Produto e o Valor é a quantidade desse item no carrinho
        self.__itens = {}

    def adicionar_item(self, item:Produto, qtd):
        
        id = item.get_id()
        nome = item.get_nome()

        if id in self.__itens:
            self.__itens[id] += qtd
        else:
            self.__itens[id] = qtd

        print(f'{qtd} unidades de {nome} adicionadas ao carrinho')
        
        

    def remover_item(self, item:Produto):
        id = item.get_id()
        nome = item.get_nome()

        if id in self.__itens:
            self.__itens.pop(id)
            print(f'{nome} removido do carrinho')
        else:
            print(f'{nome} não encontrado no carrinho')


    def __str__(self):
        return f'Itens comprados: {self.__itens}'