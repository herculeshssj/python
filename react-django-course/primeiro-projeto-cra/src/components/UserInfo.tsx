import { UserAge } from "./UserAge"
import { UserAvatar } from "./UserAvatar"
import { UserEmail } from "./UserEmail"
import { UserName } from "./UserName"
import { UserRoles } from "./UserRoles"

type Props = {
    name: string;
    email: string;
    age: number;
    url: string;
    roles: {id: number, title: string}[]
}

export const UserInfo = (props: Props) => {
    return (
        <>
            <h2>Informações do usuário</h2>
            <UserAvatar 
                src={props.url}
            />
            <UserName 
                name={props.name}
            />
            <UserEmail 
                email={props.email}
            />
            <UserAge 
                age={props.age}
            />       
            <UserRoles 
                roles={props.roles}
            />     
        </>
    )
}