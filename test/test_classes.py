import pytest
import re
import requests

from classes.PessoaFisica import PessoaFisica
from classes.Endereco import Endereco
from classes.Produto import Produto
from classes.Pedido import Pedido
from classes.Carrinho import Carrinho

@pytest.mark.exercicio_3
def test_pessoa_fisica():
    pf = PessoaFisica('Tiago', 'tiago@email.com', '524.222.452-6')
    assert pf.nome == 'Tiago'
    assert pf.email == 'tiago@email.com'
    assert pf.cpf == '524.222.452-6'

@pytest.mark.exercicio_3
def test_produto():
    produto = Produto('0010342967', 'Sabonete')
    assert produto.id == '0010342967'
    assert produto.nome == 'Sabonete'

@pytest.mark.exercicio_3
def test_carinho():
    sabonete = Produto('0010342967', 'Sabonete')
    carrinho = Carrinho()
    carrinho.adicionar_item(sabonete, 2)
    assert carrinho.produtos[0].id == '0010342967'
    assert carrinho.produtos[0].qtd == 2

@pytest.mark.exercicio_2
def test_endereco():
    end = Endereco('08320330', 430)
    assert end.cep == '08320330'
    assert end.numero == 430

@pytest.mark.exercicio_2
def test_endereco_consulta_cep_int():
    end = Endereco(int('08320330'), 430)
    assert end.cep == '08320330'
    assert end.numero == 430

@pytest.mark.exercicio_2
def test_endereco_nao_encontra_cep():
    assert Endereco.consultar_cep('00000000') == False

@pytest.mark.exercicio_2
def test_endereco_consulta_cep_nao_existe():
    assert Endereco.consultar_cep('830') == False

@pytest.mark.sem_conecxao
def test_endereco_consulta_cep_problema_de_conexao():
    assert pytest.raises(requests.exceptions.ConnectionError, Endereco('08320330', 430))

