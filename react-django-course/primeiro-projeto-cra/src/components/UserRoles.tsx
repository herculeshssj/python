export const UserRoles = () => {
    const roles = ['CEO', 'CTO', 'admin'];

    const rolesMap = [
        { id: 1, name: 'CEO' },
        { id: 2, name: 'CTO' },
        { id: 3, name: 'admin' }
    ]
    
    return (
        <ul>
            {rolesMap.map((value, key) => (
                <li key={key}>{value.name}</li>
            ))}
        </ul>
    );       
}