import { useState, useEffect } from "react";

const UserList = () => {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    const getUsers = async () => {
      const url = "http://localhost:5555/api/v1/users";
      const response = await fetch(url);
      let json = await response.json();
      let users = json;
      setUsers(users);
    };

    getUsers();
  }, []);

  return (
    <section>
      <h1>Users</h1>
      <ul>
        {users.map((user) => (
          <li key={`${user.id}-${user.username}`}>
            <p>{user.id}</p>
            <p>{user.username}</p>
            <p>{user.first_name}</p>
            <p>{user.last_name}</p>
            <p>{user.email}</p>
          </li>
        ))}
      </ul>
    </section>
  );
};

export default UserList;
