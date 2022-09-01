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
    assert carrinho.itens[sabonete.id] == 2

@pytest.mark.exercicio_3
def test_pedido():
    pf = PessoaFisica('Tiago', 'tiago@email.com', '524.222.452-6')
    end = Endereco('04546042', 300)
    sabonete = Produto('0010342967', 'Sabonete')
    carrinho = Carrinho()
    carrinho.adicionar_item(sabonete, 2)
    pedido = Pedido(pf, end, carrinho)
    assert pedido.pessoa.nome == 'Tiago'
    assert pedido.endereco.cep == '04546042'
    assert pedido.endereco.numero == 300
    assert pedido.carrinho.itens[sabonete.id] == 2

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
def test_endereco_consulta_cep_nao_existe():
    assert Endereco.consultar_cep('830') == False

@pytest.mark.sem_conexao
def test_endereco_consulta_cep_problema_de_conexao():
    with pytest.raises(requests.exceptions.ConnectionError):
        Endereco.consultar_cep('08320330')

