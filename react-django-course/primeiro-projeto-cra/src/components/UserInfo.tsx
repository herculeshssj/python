import { UserAge } from "./UserAge"
import { UserEmail } from "./UserEmail"
import { UserName } from "./UserName"

export const UserInfo = () => {
    return (
        <>
            <h2>Informações do usuário</h2>
            <UserName />
            <UserEmail />
            <UserAge />            
        </>
    )
}