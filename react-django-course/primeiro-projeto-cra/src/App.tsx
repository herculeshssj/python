// import { UserName } from "./UserName";
import { UserName as Us, UserEmail as Eu } from "./UserName";
import UserAge from "./UserName";

const App = () => {
  return (
    <div className="App">
      <h1>Meu primeiro componente de usuário</h1>

      <Us />
      <Eu />
      <UserAge />
    </div>
  );
}

export default App;