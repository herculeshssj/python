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

      {isLoggedIn ? <UserInfo
        age={30}
        email="johndoe@teste.com"
        name="João da Silva"
        url="https://www.w3schools.com/howto/img_avatar.png"
        roles={[{ id: 1, title: "Admin" }, { id: 2, title: "User" }]}
      /> : <h2>Você não está logado</h2>}

    </div>
  );
}

export default App;