// React-компонент для навигационного меню
import React, { useEffect, useState } from "react";
import axios from "axios";

function Navbar() {
  const [navData, setNavData] = useState(null);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/api/navbar/")  // Запрос к Django
      .then(response => {
        setNavData(response.data);
      })
      .catch(error => console.error("Ошибка при получении навбара", error));
  }, []);

  if (!navData) return <p>Загрузка меню...</p>;

  return (
    <header style={{ backgroundColor: "#f0f0f0", padding: "10px" }}>
      <img src={navData.logo} alt="Logo" style={{ height: "50px" }} />
      <nav style={{ display: "inline-block", marginLeft: "30px" }}>
        {navData.links.map((link, idx) => (
          <a key={idx} href={link.url} style={{ marginRight: "15px" }}>
            {link.name}
          </a>
        ))}
      </nav>
    </header>
  );
}

export default Navbar;
