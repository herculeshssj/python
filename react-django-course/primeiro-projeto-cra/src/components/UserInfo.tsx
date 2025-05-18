import { UserAge } from "./UserAge"
import { UserAvatar } from "./UserAvatar"
import { UserEmail } from "./UserEmail"
import { UserName } from "./UserName"

export const UserInfo = () => {
    return (
        <>
            <h2>Informações do usuário</h2>
            <UserAvatar />
            <UserName />
            <UserEmail />
            <UserAge />            
        </>
    )
}