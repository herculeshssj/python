import { ChangeEvent, FormEvent } from "react";
import { Button } from "./components/Button";
import {useState} from 'react';
import { StateUpdater } from "./components/StateUpdater";

const App = () => {

  // Hooks são funções que permitem usar o estado e outros recursos do React sem escrever uma classe.
  const [count, setCount] = useState(0)

  const [logged, setLogged] = useState(false);

  const [value, setValue] = useState('');

  const handleInputChange = (e: ChangeEvent<HTMLInputElement>) => {
    setValue(e.target.value);
  } 

  const handleClickCount = () => {
    setCount(count + 1);
  }

  const handleLogin = () => {
    setLogged(!logged);
  }

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

      <h2>{count} cliques</h2>
      <button onClick={handleClickCount}>
        Usando Hooks - adicionar mais um
      </button>

      <h2>{logged ? 'Usuário logado' : 'Usuário não logado'}</h2>
      <button onClick={handleLogin}>
        {logged ? 'Deslogar' : 'Logar'}
      </button>

      <form onSubmit={handleSubmit}>
        <input />
        <button>Enviar</button>
      </form>

      <input
        value={value}
        onChange={handleInputChange}
      />
      <h2>{value}</h2>

      <hr/>

      <StateUpdater />
    </div>
  )
}

export default App;
