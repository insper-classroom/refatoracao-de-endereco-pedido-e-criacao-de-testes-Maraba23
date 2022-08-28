#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------



import re


class Produto:

    lista_produtos = []

    def __init__(self, id, nome, descricao='', preco='0.00'):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        Produto.lista_produtos.append(self)

    def set_id(self, id_novo):
        self.id = id_novo

    def get_id(self):
        return self.id

    def get_nome(self):
        return self.nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        if not isinstance(novo_nome, str):
            raise TypeError('Nome deve ser uma string')
        if re.search(r'[^a-zA-Z0-9 ]', novo_nome):
            raise ValueError('Nome invalido')
        self.__nome = novo_nome

    def to_dict(self):
        return {
            'id': self.__id,
            'nome': self.nome,
            'descricao': self.descricao,
            'preco': self.preco
        }

    def __len__(self):
        return len(Produto.lista_produtos)

    def busca_nome(nome):
        for p in Produto.lista_produtos:
            if p.nome.lower() == nome.lower() or nome.lower() in p.nome.lower():
                return p
        return None

    def __str__(self):
        return f'Produto -> id: {self.id}, nome: {self.nome}, descrição: {self.descricao}, preço: {self.preco}'


