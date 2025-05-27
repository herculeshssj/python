import { use, useEffect, useState } from "react"

export const Card = () => {

    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [fullName, setFullName] = useState('');

    const [count, setCount] = useState(0);

    useEffect(() => {
        //console.log('Card foi renderizado')

        /*
        return () => {
            console.log('Card foi desmontado')
        }
        */
        setFullName(`${firstName} ${lastName}`);

        const intervalId = setInterval(() => {
            setCount((prevCount) => prevCount + 1);
            console.log('Contador atualizado:', count);
        }, 1000);

        return () => { 
            clearInterval(intervalId);
            console.log('useEffect foi executado!')
        }
    }, [firstName, lastName])


    return (
        <>
            {/* <p>Componente Card</p> */}

            <input
                type="text"
                placeholder="Nome"
                value={firstName}
                onChange={(e) => setFirstName(e.target.value)}
            />
            <input
                type="text"
                placeholder="Sobrenome"
                value={lastName}
                onChange={(e) => setLastName(e.target.value)}
            />
            <strong>{fullName}</strong>

            <br/>

            <p>Contador: {count}</p>
        </>
    )
}