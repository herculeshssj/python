import { useState } from "react";

export const HookCondicional = () => {

    const [logged, setLogged] = useState(false);

    const handleLogin = () => {
        setLogged(!logged);
    }

    return(
        <>
            <h2>{logged ? 'Usuário logado' : 'Usuário não logado'}</h2>
            <button onClick={handleLogin}>
                {logged ? 'Deslogar' : 'Logar'}
            </button>
        </>
    )
}