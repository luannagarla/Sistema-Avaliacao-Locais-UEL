import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import UsuariosPage from "./pages/UsuariosPage";

function App() {
  return (
    <Router>
      <nav>
        <Link to="/usuarios">Usuários</Link> | 
      </nav>
      <Routes>
        <Route path="/usuarios" element={<UsuariosPage />} />
      </Routes>
    </Router>
  );
}

export default App;
