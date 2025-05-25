const App = () => {

  const handleClick = (value: string) => {
    alert(value);
  }

  return (
    <div>
      <button onClick={() => handleClick('Hello')}>
        <span>Click me</span>
      </button>
    </div>
  )
}

export default App;
