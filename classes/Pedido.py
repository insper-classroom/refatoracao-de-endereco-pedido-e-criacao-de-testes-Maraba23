#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  :
# Created Date:
# version ='1.0'
# ---------------------------------------------------------------------------

from classes.Endereco import Endereco
from classes.PessoaFisica import PessoaFisica
from classes.Carrinho import Carrinho
import re




class Pedido:
    EM_ABERTO = 1
    PAGO = 2

    def __init__(self, pessoa:PessoaFisica, endereco:Endereco, carrinho:Carrinho):
        self.__pessoa = pessoa
        self.__endereco = endereco
        self.__carrinho = carrinho
        
    @property
    def endereco_entrega(self):
        return self.__endereco

    @endereco_entrega.setter
    def endereco_entrega(self, novo_endereco:Endereco):
        self.__endereco = novo_endereco

    def endereco_faturamento(self):
        return self.__endereco

    def carrinho(self):
        return self.__carrinho

    def __str__(self):
        # imprime detalhes da compra - pessoa, endereço e produtos
        return f'{self.__pessoa}, {self.__endereco}, {self.__carrinho}'