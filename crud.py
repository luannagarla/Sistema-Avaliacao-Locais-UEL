from database import get_connection

# === CRUD USUÁRIO ===
def criar_usuario(nome, email, tipo, curso_nome, departamento):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO usuario (nome, email, tipo, curso_nome, departamento)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING id_usuario;
    """, (nome, email, tipo, curso_nome, departamento))
    conn.commit()
    novo_id = cur.fetchone()[0]
    cur.close()
    conn.close()
    return novo_id


def listar_usuarios():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id_usuario, nome, email, tipo FROM usuario;")
    usuarios = cur.fetchall()
    cur.close()
    conn.close()
    return usuarios


# === CRUD LOCAL ===
def criar_local(nome, descricao, localizacao, categoria, url_image):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO localcampus (nome, descricao, localizacao, categoria, url_image)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING id_local;
    """, (nome, descricao, localizacao, categoria, url_image))
    conn.commit()
    novo_id = cur.fetchone()[0]
    cur.close()
    conn.close()
    return novo_id


def listar_locais():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id_local, nome, categoria, localizacao FROM localcampus;")
    locais = cur.fetchall()
    cur.close()
    conn.close()
    return locais


# === CRUD AVALIAÇÃO ===
def criar_avaliacao(id_usuario, id_local, nota, data_avaliacao):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO avaliacao (id_usuario, id_local, nota, data_avaliacao)
        VALUES (%s, %s, %s, %s)
        RETURNING id_avaliacao;
    """, (id_usuario, id_local, nota, data_avaliacao))
    conn.commit()
    novo_id = cur.fetchone()[0]
    cur.close()
    conn.close()
    return novo_id


def listar_avaliacoes():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT a.id_avaliacao, u.nome AS usuario, l.nome AS local, a.nota, a.data_avaliacao
        FROM avaliacao a
        JOIN usuario u ON a.id_usuario = u.id_usuario
        JOIN localcampus l ON a.id_local = l.id_local;
    """)
    avaliacoes = cur.fetchall()
    cur.close()
    conn.close()
    return avaliacoes
