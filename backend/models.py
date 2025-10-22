class Usuario:
    def __init__(self, id_usuario, nome, email, tipo, curso_nome, departamento):
        self.id_usuario = id_usuario
        self.nome = nome
        self.email = email
        self.tipo = tipo
        self.curso_nome = curso_nome
        self.departamento = departamento


class LocalCampus:
    def __init__(self, id_local, nome, descricao, localizacao, categoria, url_image):
        self.id_local = id_local
        self.nome = nome
        self.descricao = descricao
        self.localizacao = localizacao
        self.categoria = categoria
        self.url_image = url_image


class Avaliacao:
    def __init__(self, id_avaliacao, id_usuario, id_local, nota, data_avaliacao):
        self.id_avaliacao = id_avaliacao
        self.id_usuario = id_usuario
        self.id_local = id_local
        self.nota = nota
        self.data_avaliacao = data_avaliacao
