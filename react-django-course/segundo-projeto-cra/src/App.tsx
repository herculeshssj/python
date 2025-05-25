import { FormEvent } from "react";
import { Button } from "./components/Button";

const App = () => {

  const handleClick = (value: string) => {
    alert(value);
  }

  const tratarClique = (value: string) => {
    alert(value);
  }

  const handleSubmit = (e:FormEvent) => {
    e.preventDefault();
    alert('Formulário enviado');
  }

  return (
    <div>
      <Button
        onClique={tratarClique}
      />
      <form onSubmit={handleSubmit}>
        <input />
        <button>Enviar</button>
      </form>
    </div>
  )
}

export default App;
