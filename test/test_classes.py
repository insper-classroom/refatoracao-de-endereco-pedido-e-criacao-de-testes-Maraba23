import pytest
import re
import requests

from classes.PessoaFisica import PessoaFisica
from classes.Endereco import Endereco
from classes.Produto import Produto
from classes.Pedido import Pedido
from classes.Carrinho import Carrinho

def test_pessoa_fisica():
    pf = PessoaFisica('Tiago', 'tiago@email.com', '524.222.452-6')
    assert pf.nome == 'Tiago'
    assert pf.email == 'tiago@email.com'
    assert pf.cpf == '524.222.452-6'

def test_endereco():
    end = Endereco('08320330', 430)
    assert end.cep == '08320330'
    assert end.numero == 430

def test_endereco_consulta_cep_int():
    end = Endereco(int('08320330'), 430)
    assert end.cep == '08320330'
    assert end.numero == 430

def test_endereco_nao_encontra_cep():
    assert Endereco('00000000', 430) == False

@pytest.mark.sem_conecxao
def test_endereco_consulta_cep_problema_de_conexao():
    assert pytest.raises(requests.exceptions.ConnectionError, Endereco('08320330', 430))

