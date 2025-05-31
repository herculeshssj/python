import { Provider } from "react-redux";
import { store } from "./redux/store";
import { Botao } from "./components/Botao";

const App = () => {
  return (
    <Provider store={store}>
      <div>
        <Botao />
      </div>
    </Provider>
  );
}

export default App;