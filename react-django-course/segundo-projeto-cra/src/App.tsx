import { ChangeEvent, FormEvent } from "react";
import { Button } from "./components/Button";
import {useState} from 'react';
import { StateUpdater } from "./components/StateUpdater";
import { Fullname } from "./components/Fullname";
import { HookCondicional } from "./components/HookCondicional";
import { ExemploFormulario } from "./components/ExemploFormulario";
import { StateMatrizes } from "./components/StateMatrizes";
import { Card } from "./components/Card";
import { UseIdExemplo } from "./components/UseIdExemplo";

const App = () => {

  const [visible, setVisible] = useState(false);

  const handleVisible = () => {
    setVisible(!visible);
  }
  
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

      <hr/>
      <h2> Exemplo com matrizes / array </h2>

      <StateMatrizes />

      <hr/>
      <h2>Exemplo de UseEffect</h2>
      <button onClick={handleVisible}> Mostrar / Ocultar Card </button>

      {visible && <Card />}

      <hr/>
      <h2>Exemplo de UserID</h2>
      <UseIdExemplo />

    </div>
  )
}

export default App;
