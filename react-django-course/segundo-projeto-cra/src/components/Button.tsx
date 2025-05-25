type Props = {
    //label: string;
    onClique: (label: string) => void;
}

export const Button = ({onClique}: Props) => {

    const label = "Meu texto do botão"

    return (
        <button onClick={() => onClique('Meu texto do alerta')}>
            {label}
        </button>
    )
}