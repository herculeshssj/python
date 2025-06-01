const App = () => {

  const handleGetPosts = async () => {
    const posts = await fetch('https://jsonplaceholder.typicode.com/posts',
      {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      })
      .then(response => response.json())
      .catch(error => console.error('Error fetching posts:', error));
    console.log(posts);
  }

  return (
    <div>
      <button onClick={handleGetPosts}>Get Posts</button>
    </div>
  );
}

export default App;