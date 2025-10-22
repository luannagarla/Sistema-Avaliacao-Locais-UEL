import { useEffect, useState } from "react";

export default function UsuarioList() {
  const [usuarios, setUsuarios] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/usuarios") // sua API FastAPI
      .then(res => res.json())
      .then(data => setUsuarios(data));
  }, []);

  return (
    <ul>
      {usuarios.map(u => (
        <li key={u.id_usuario}>{u.nome} - {u.email}</li>
      ))}
    </ul>
  );
}
