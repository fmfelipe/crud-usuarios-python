import unittest
from unittest.mock import patch
from src.lab_crud_usuarios import cadastrar, listar_todos_usuarios, listar_usuario, deletar_usuario


class TestApp(unittest.TestCase):


    def test_cadastro(self):
        self.assertEqual(cadastrar("Joe", "j@gmail.com", "Abc123", "213471283"), "sucesso")

    def test_cadastro_email_existente(self):
        cadastrar("Joe", "j@gmail.com", "Abc123", "213471283")
        resultado = cadastrar("Bob", "j@gmail.com", "Def456", "321347128")
        self.assertEqual(resultado, "email já cadastrado")



    def test_listar_todos(self):
        cadastrar("Joe", "j@gmail.com", "Abc123", "213471283")
        usuarios = listar_todos_usuarios()
        self.assertGreater(len(usuarios), 0)
    


    def test_listar_usuario(self):
        cadastrar("Joe", "j@gmail.com", "Abc123", "213471283")
        resultado = listar_usuario("213471283")
        self.assertEqual(resultado["nome"], "Joe")



    def test_listar_usuario_invalido(self):
        resultado = listar_usuario("234567800")
        self.assertEqual(resultado, "cpf não encontrado")



    def test_deletar_usuario(self):
        cadastrar("Joe", "j@gmail.com", "Abc123", "213471283")
        resultado = deletar_usuario("213471283")
        self.assertTrue(resultado)
        self.assertEqual(listar_usuario("213471283"), "cpf não encontrado")

#    @patch("src.app.save", return_value = True)
#    def test_cadastrar_usuario_valido(self, mock_salvar):
#        nome = "Carlos"
#        cpf = "213471283"
#        resultado = cadastro(nome, cpf)
#        self.assertTrue(resultado)
#        mock_salvar.assert_called_once_with({"nome":nome, "cpf":cpf})



if __name__ == '__main__':
    unittest.main()
