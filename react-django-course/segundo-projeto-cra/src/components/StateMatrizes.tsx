import { useState } from "react"

export const StateMatrizes = () => {

    const [tasks, setTasks] = useState<string[]>([])
    const [inputValue, setInputValue] = useState('')

    const handleAdd = () => {
        if (inputValue == '') return;

        // Método 1
        //setTasks([...tasks, inputValue])
        //setInputValue('')

        // Método 2
        //setTasks(tasks.concat(inputValue))
        //setInputValue('')

        // Método 3
        const newTasks = [...tasks]
        newTasks.push(inputValue)
        setTasks(newTasks)
        setInputValue('')

    }

    const handleRemove = (key: number) => {
        setTasks(tasks.filter((value, index) => index !== key))
    }

    return(
        <div>
            <h2>Minha lista de tarefas</h2>
            <input 
                type="text" 
                value={inputValue} 
                onChange={(e) => setInputValue(e.target.value)} 
            />
            <button onClick={handleAdd}>Adicionar</button>
            <ul>
                {tasks.map((task, index) => (
                    <li key={index}>
                        {task}
                        <button onClick={() => handleRemove(index)}>Remover</button>
                    </li>
                ))}
            </ul>
        </div>
    )
}