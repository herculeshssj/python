import { ChangeEvent, FormEvent } from "react";
import { Button } from "./components/Button";
import {useState} from 'react';
import { StateUpdater } from "./components/StateUpdater";
import { Fullname } from "./components/Fullname";
import { HookCondicional } from "./components/HookCondicional";
import { ExemploFormulario } from "./components/ExemploFormulario";

const App = () => {

  // Hooks são funções que permitem usar o estado e outros recursos do React sem escrever uma classe.
  const [count, setCount] = useState(0)

  const [value, setValue] = useState('');

  const handleInputChange = (e: ChangeEvent<HTMLInputElement>) => {
    setValue(e.target.value);
  } 

  const handleClickCount = () => {
    setCount(count + 1);
  }

  const handleClick = (value: string) => {
    alert(value);
  }

  const tratarClique = (value: string) => {
    alert(value);
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

      <hr/>
      <h2>Hook Condicional</h2>
      <p>Exemplo de hook condicional</p>

      <HookCondicional />

      <hr/>

      <ExemploFormulario />

      <input
        value={value}
        onChange={handleInputChange}
      />
      <h2>{value}</h2>

      <hr/>

      <h2>State Updater</h2>
      <StateUpdater />

      <hr/>

      <Fullname />

    </div>
  )
}

export default App;
