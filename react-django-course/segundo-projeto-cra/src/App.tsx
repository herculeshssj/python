import { Button } from "./components/Button";

const App = () => {

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
    </div>
  )
}

export default App;
