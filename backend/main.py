from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from crud import criar_usuario, listar_usuarios, criar_local, listar_locais, criar_avaliacao, listar_avaliacoes

app = FastAPI()

# CORS para o front React
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# Rotas de teste
@app.get("/")
def read_root():
    return {"message": "API funcionando"}

@app.get("/usuarios")
def get_usuarios():
    return listar_usuarios()
