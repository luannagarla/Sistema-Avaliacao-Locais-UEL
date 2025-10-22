import { useState } from "react";

export default function UsuarioForm() {
  const [nome, setNome] = useState("");
  const [email, setEmail] = useState("");
  const [tipo, setTipo] = useState("");
  const [curso, setCurso] = useState("");
  const [departamento, setDepartamento] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    await fetch("http://localhost:8000/usuarios", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ nome, email, tipo, curso_nome: curso, departamento })
    });
    setNome(""); setEmail(""); setTipo(""); setCurso(""); setDepartamento("");
    alert("Usuário criado!");
  };

  return (
    <form onSubmit={handleSubmit}>
      <input placeholder="Nome" value={nome} onChange={e => setNome(e.target.value)} />
      <input placeholder="Email" value={email} onChange={e => setEmail(e.target.value)} />
      <input placeholder="Tipo" value={tipo} onChange={e => setTipo(e.target.value)} />
      <input placeholder="Curso" value={curso} onChange={e => setCurso(e.target.value)} />
      <input placeholder="Departamento" value={departamento} onChange={e => setDepartamento(e.target.value)} />
      <button type="submit">Criar</button>
    </form>
  );
}
