#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------

from classes.Endereco import Endereco
import re


class PessoaFisica:
    '''Esta classe implementa uma pessoa no contexto de uma compra em e-commerce.
    
    As propriedades email e cpf estão privadas para previnir o usuário da classe de 
    acessar e alterar diretamente a propriedade sem uma verificação.
    '''
    lista_pessoas = []

    def __init__(self, nome, email, cpf):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.__enderecos = {}
        PessoaFisica.lista_pessoas.append(self)

    # escolher o estilo de retorno

    def adicionar_endereco(self, apelido_endereco, end:Endereco):
        self.__enderecos[apelido_endereco] = end.to_dict()

    def remover_endereco(self, apelido_endereco):
        self.__enderecos.pop(apelido_endereco)

    def get_endereco(self, apelido_endereco):
        self.__enderecos[apelido_endereco]

    def listar_enderecos(self):
        return self.__enderecos

    def __len__(self):
        return len(PessoaFisica.lista_pessoas)

    def busca_nome(nome):
        for p in PessoaFisica.lista_pessoas:
            if p.nome.lower() == nome.lower() or nome.lower() in p.nome.lower():
                return p
        return None

    def __str__(self):
        return f'Cliente: {self.nome}, Email: {self.email}, Cpf: {self.cpf}'


        
    