import {useId} from 'react'
import {useRef} from 'react'

export const UseIdExemplo = () => {
    const id = useId();
    const inputElemento = useRef<HTMLInputElement | null>(null);

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
        </>
    )
}