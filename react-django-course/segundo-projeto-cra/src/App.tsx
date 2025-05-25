const App = () => {

  const handleClick = () => {
    alert('Button clicked');
  }

  return (
    <div>
      <button onClick={handleClick}>
        <span>Click me</span>
      </button>
    </div>
  )
}

export default App;
