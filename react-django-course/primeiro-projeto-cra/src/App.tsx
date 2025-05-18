import { UserInfo } from "./components/UserInfo";

const App = () => {

  const isLoggedIn = true;

  /*
  const isLoggedIn = false;

  if (isLoggedIn) {

    return (
      <div className="App">
        <h1>Meu primeiro componente de usuário</h1>
        <UserInfo />
      </div>
    );
  } else {
    return (
      <div className="App">
        <h1>Meu primeiro componente de usuário</h1>
        <h2>Você não está logado</h2>
      </div>
    );
  }
    **/

  return (
    <div className="App">
      <h1>Meu primeiro componente de usuário</h1>

      {isLoggedIn ? <UserInfo/> : <h2>Você não está logado</h2>}

    </div>
  );
}

export default App;