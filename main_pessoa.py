from pessoa import Pessoa
from pessoa_fisica import PessoaFisica
from pessoa_juridica import PessoaJuridica

pessoa1 = Pessoa("João", 3, "2024-01-01", True)
pessoa1.imprimir_valores()

pessoa_fisica1 = PessoaFisica("Maria", 2, "2023-02-02", True, "2000-01-01", "333.444.555-66", "123")
pessoa_fisica1.imprimir_valores()

pessoa_juridica1 = PessoaJuridica("Bemol", 1, "2020-03-03", True, "1990-04-04", "34.456.789/0001-12")
pessoa_juridica1.imprimir_valores()


pessoa1.nome = "Pedro"
pessoa1.status = False
pessoa1.data_abertura_conta = "2024-02-02"
pessoa1.imprimir_valores()

pessoa_fisica1.nome = "Tereza"
pessoa_fisica1.cpf = "123.456.789-10"
pessoa_fisica1.imprimir_valores()

pessoa_juridica1.cnpj = "12.345.678/0001-90"
pessoa_juridica1.imprimir_valores()
