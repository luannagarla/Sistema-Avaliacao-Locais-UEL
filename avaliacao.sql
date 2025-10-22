CREATE TABLE usuario (
    id_usuario SERIAL PRIMARY KEY, 
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,   
    tipo VARCHAR(20) NOT NULL,
    curso_nome VARCHAR(100),
    departamento VARCHAR(100),
    CONSTRAINT chk_tipo CHECK (tipo IN ('aluno', 'professor'))
);

CREATE TABLE localcampus (
    id_local SERIAL PRIMARY KEY,   
    nome VARCHAR(100) UNIQUE NOT NULL,      
    descricao TEXT,
    localizacao VARCHAR(100),
    categoria VARCHAR(50),
    url_image TEXT
);

CREATE TABLE questao (
    id_questao SERIAL PRIMARY KEY,
    texto VARCHAR(255) NOT NULL
);

CREATE TABLE avaliacao (
    id_avaliacao SERIAL PRIMARY KEY, 
    id_usuario INT NOT NULL,
    id_local INT NOT NULL,
    nota INT NOT NULL,
    data_avaliacao DATE NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuario (id_usuario) ON DELETE CASCADE,
    FOREIGN KEY (id_local) REFERENCES localcampus (id_local) ON DELETE CASCADE,
    CONSTRAINT chk_nota CHECK (nota BETWEEN 1 AND 5)
);

CREATE TABLE avaliacao_questao (
    id_avaliacao INT NOT NULL,
    id_questao INT NOT NULL,
    resposta INT CHECK (resposta BETWEEN 1 AND 5),
    FOREIGN KEY (id_avaliacao) REFERENCES avaliacao (id_avaliacao) ON DELETE CASCADE,
    FOREIGN KEY (id_questao) REFERENCES questao (id_questao) ON DELETE CASCADE,
    PRIMARY KEY (id_avaliacao, id_questao)
);

-- Insert de dados para entendermos melhor e implementar telas:

INSERT INTO usuario (nome, email, tipo, curso_nome, departamento)
VALUES 
('Luanna Garla', 'luanna@uel.br', 'aluno', 'Ciência de Dados e IA', 'Exatas'),
('Michele Silva', 'michele@uel.br', 'professor', 'Engenharia de Software', 'Tecnologia'),
('João Santos', 'joao@uel.br', 'aluno', 'Sistemas de Informação', 'Computação'),
('Carla Souza', 'carla@uel.br', 'professor', 'Arquitetura de Software', 'Computação');

INSERT INTO localcampus (nome, descricao, localizacao, categoria, url_image)
VALUES
('Restaurante Universitário (RU)', 'Local para refeições dos alunos e servidores', 'Bloco Central', 'Restaurante', 'https://exemplo.com/imagens/ru.jpg'),
('Biblioteca Central', 'Espaço para estudos e empréstimos de livros', 'Bloco B', 'Biblioteca', 'https://exemplo.com/imagens/biblioteca.jpg'),
('Cantina do Bloco C', 'Cantina com lanches e cafés', 'Bloco C', 'Cantina', 'https://exemplo.com/imagens/cantina.jpg'),
('Centro Acadêmico de Computação', 'Espaço de convivência e eventos dos alunos de Computação', 'Bloco D', 'Centro Acadêmico', 'https://exemplo.com/imagens/ca.jpg');

INSERT INTO questao (texto)
VALUES
('Qual sua nota geral para o local (1 a 5)?'),
('O local é confortável?'),
('O ambiente é limpo e bem cuidado?'),
('Você recomendaria este local para outras pessoas?');

INSERT INTO avaliacao (id_usuario, id_local, nota, data_avaliacao)
VALUES
(1, 1, 5, '2025-10-21'), -- Luanna (euuu) avaliou o RU (amooo)
(2, 2, 4, '2025-10-20'), -- Michele avaliou a Biblioteca
(3, 3, 3, '2025-10-19'), -- João avaliou a Cantina
(4, 4, 5, '2025-10-21'); -- Carla avaliou o Centro Acadêmico

INSERT INTO avaliacao_questao (id_avaliacao, id_questao, resposta)
VALUES
-- Avaliação 1 (Luanna no RU)
(1, 1, 5), (1, 2, 5), (1, 3, 4), (1, 4, 5),

-- Avaliação 2 (Michele na Biblioteca)
(2, 1, 4), (2, 2, 4), (2, 3, 5), (2, 4, 4),

-- Avaliação 3 (João na Cantina)
(3, 1, 3), (3, 2, 3), (3, 3, 2), (3, 4, 3),

-- Avaliação 4 (Carla no Centro Acadêmico)
(4, 1, 5), (4, 2, 5), (4, 3, 5), (4, 4, 5);
