import {useId, useState} from 'react'
import {useRef} from 'react'

export const UseIdExemplo = () => {
    const id = useId();
    const inputElemento = useRef<HTMLInputElement | null>(null);

    const [time, setTime] = useState(0);
    const intervalRef = useRef(0);

    const handleStart = () => {
        if (intervalRef.current) handleStop();

        /*const intervalID =*/ setInterval(() => {
            setTime(t => t + 1)
        }, 1000);

        //intervalRef.current = intervalID;
    }

    const handleStop = () => {
        clearInterval(intervalRef.current);
    }

    const handleClick = () => {
        if (inputElemento.current) {
            inputElemento.current.focus();
        }
    }

    return (
        <>
            <label htmlFor={id}>Informe seu nome</label>
            <input placeholder="Digite seu nome" id={id} />

            <br/>
            <input id="input-1" placeholder="Input 1" ref={inputElemento} />
            <button onClick={handleClick}>Focar no Input</button>

            <br/>
            <h2>Contador: {time}</h2>
            <div style={{display: 'flex', gap: '10px'}}>
                <button onClick={handleStart}>Iniciar</button>
                <button onClick={handleStop}>Parar</button>
            </div>
        </>
    )
}