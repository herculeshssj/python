import { ChangeEvent, useState } from "react";

export const Fullname = () => {

    const [fullname, setFullname] = useState({
        firstName: '',
        lastName: ''
    });

    const handleChangeFirstName = (e: ChangeEvent<HTMLInputElement>) => {
    setFullname({
        ...fullname,
        firstName: e.target.value
    });
    }

    const handleChangeLastName = (e: ChangeEvent<HTMLInputElement>) => {
    setFullname({
        ...fullname,
        lastName: e.target.value
    });
    }

    return (
        <>
            <h2>Nome completo</h2>
            <span>Primeiro Nome: </span>
            <input value={fullname.firstName} onChange={handleChangeFirstName}/>
            <br/>
            <span>Último Nome: </span>
            <input value={fullname.lastName} onChange={handleChangeLastName}/>
        </>
    )
}