import { useState } from "react";

export const StateUpdater = () => {

    const [count, setCount] = useState(0);

    const handleClickCount = () => {
        /*
        setCount(count + 1);
        setCount(count + 1);
        setCount(count + 1);
        */
       setCount(c => c + 1); // -> 0 + 1 = 1
       setCount(c => c + 1); // -> 1 + 1 = 2
       setCount(c => c + 1); // -> 2 + 1 = 3
       
    }

    return (
        <>
            <p>Olá</p>
            <p>{count}</p>
            <button onClick={handleClickCount}>Adicionar +3</button>
        </>
    )    
}