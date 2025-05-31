import { useDispatch, useSelector } from "react-redux";
import type { RootState } from "../redux/store";
import { setTheme } from "../redux/reducers/themeReducer";

export const Botao = ()=> {

    const {theme} = useSelector((state:RootState) => state.theme);

    const dispatch = useDispatch();

    const handleClick = () => {
        if (theme === 'light') {
            dispatch(setTheme('dark'));
        } else {
            dispatch(setTheme('light'));
        }
    }

  return (
    <div>

        O tema é {theme}
        <br />
        <button onClick={handleClick}>Mudar o tema</button>
    </div>
  );
}