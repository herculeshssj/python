import { use, useEffect } from "react"

export const Card = () => {
    useEffect(() => {
        console.log('Card foi renderizado')

        return () => {
            console.log('Card foi desmontado')
        }
    }, [])


    return (
        <>
            <p>Componente Card</p>
        </>
    )
}