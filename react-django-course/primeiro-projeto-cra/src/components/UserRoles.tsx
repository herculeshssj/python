type Props = {
    roles: {id: number, title: string}[]
}

export const UserRoles = (roles : Props) => {
    // const roles = ['CEO', 'CTO', 'admin'];

    const rolesMap = [
        { id: 1, name: 'CEO' },
        { id: 2, name: 'CTO' },
        { id: 3, name: 'admin' }
    ]

    const filterRoles = (value: {id: number, title: string}):boolean => {
        return value.title.includes('a');
    }

    const filteredRoles = rolesMap.filter(value => value.id == 1);
    
    return (
        <ul>
            {filteredRoles.map((value, key) => (
                <li key={key}>{value.name}</li>
            ))}
        </ul>
    );       
}