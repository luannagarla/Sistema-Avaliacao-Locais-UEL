import UsuarioList from "../components/UsuarioList";
import UsuarioForm from "../components/UsuarioForm";

export default function UsuariosPage() {
  return (
    <div>
      <h1>Usuários</h1>
      <UsuarioForm />
      <UsuarioList />
    </div>
  );
}