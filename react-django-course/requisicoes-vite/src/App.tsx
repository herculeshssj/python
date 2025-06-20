import { useState } from "react";

type Post = {
  userId: number;
  id: number;
  title: string;
  body: string;
}

const App = () => {

  const [posts, setPosts] = useState<Post[]>([]);
  const [loading, setLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);

  const handleGetPosts = async () => {
    setLoading(true);
    const posts = await fetch('https://jsonplaceholder.typicode.com/posts',
      {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      })
      .then(response => response.json())
      .catch(error => {
        setErrorMessage('Failed to fetch posts');
        console.error('Error fetching posts:', error);
        return [];
      });
    
    setPosts(posts);
    setLoading(false);
  }

  return (
    <div>
      <button onClick={handleGetPosts}>Get Posts</button>
      {loading && <p>Loading...</p>}
      {errorMessage && <p>Error: {errorMessage}</p>}
      <ul>
        {posts.map(post => (
          <li key={post.id}>
            <h3>{post.title}</h3>
            <p>{post.body}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;