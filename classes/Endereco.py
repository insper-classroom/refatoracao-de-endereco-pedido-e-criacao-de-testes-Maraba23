#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------

from http.client import responses
import requests
import json


class Endereco: 
    '''
    Endereço de uma pessoa ou conta.
    Esta classe possui overload de Contrutor, caso envie apenas três parametros será encaminhado
    para o contrutor que consulta o cep para encontrar o endereço.
    '''

    def __init__(self, cep, numero ,rua='', estado='', cidade='', complemento=''):

        if (rua == '') or (estado == '') or (cidade == ''):
            if self.consultar_cep(cep):
                end_json = self.consultar_cep(cep)

                self.rua = end_json['logradouro']
                self.estado = end_json['uf']
                self.cidade = end_json['localidade']
                self.numero = numero
                self.complemento = complemento
                self.cep = str(cep)
                while len(self.cep) < 8:
                    self.cep = '0' + self.cep
            
            else:
                return None

        else:

            self.rua = rua
            self.estado = estado
            self.cidade = cidade
            self.numero = int(numero)
            self.complemento = complemento
            self.cep = str(cep)

    def to_dict(self):
        '''
        Metodo retorna um dicionario com as informações do endereço
        '''
        return {
            'rua': self.rua,
            'estado': self.estado,
            'cidade': self.cidade,
            'numero': self.numero,
            'complemento': self.complemento,
            'cep': self.cep
        }

    @classmethod
    def consultar_cep(cls, cep):
        '''
        Metodo realiza a consulta do cep em uma api publica para obter informações
        como estado, cidade e rua
        '''
        cep = str(cep)
        while len(cep) < 8:
            cep = '0' + cep

        # end point da API de consulta ao cep
        url_api = f'https://viacep.com.br/ws/{str(cep)}/json/'

        # Sem corpo na requisição
        # Não é necessario nenhum cabeçalho HTTP especial
        payload = {}
        headers = {}

        # requisição GET na url de pesquisa do cep. Doc.: https://viacep.com.br/ 
        response = requests.request("GET", url_api, headers=headers, data=payload)

        if response.json() == {"erro": "true"}:
            return False
        else:
            json_resp = response.json()
            return json_resp

    def __str__(self):
        '''
        Metodo retorna uma string com as informações do endereço
        '''
        return f'{self.rua}, {self.numero} - {self.cidade} - {self.estado}'
