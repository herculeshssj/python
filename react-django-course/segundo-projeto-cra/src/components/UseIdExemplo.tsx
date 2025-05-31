import {useId} from 'react'

export const UseIdExemplo = () => {
    const id = useId();

    return (
        <>
            <label htmlFor={id}>Informe seu nome</label>
            <input placeholder="Digite seu nome" id={id} />
        </>
    )
}