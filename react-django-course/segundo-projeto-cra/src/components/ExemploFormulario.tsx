import { FormEvent } from "react";

export const ExemploFormulario = () => {

    const handleSubmit = (e:FormEvent) => {
        e.preventDefault();
        alert('Formulário enviado');
    }

    return (
        <>
        <h2>Exemplo de formulário</h2>

        <form onSubmit={handleSubmit}>
            <input />
            <button>Enviar</button>
        </form>
        </>
)}