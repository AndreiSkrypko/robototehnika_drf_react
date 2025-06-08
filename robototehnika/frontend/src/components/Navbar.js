// Подключаем React и хуки: useState — для хранения данных, useEffect — для загрузки данных с сервера
import React, { useEffect, useState } from "react"

// Подключаем библиотеку axios — она помогает делать HTTP-запросы к серверу
import axios from "axios"

// Объявляем компонент Navbar — он будет показывать логотип и меню
function Navbar() {
  // Создаём переменную состояния navData, где будут храниться данные меню
  // Пока данных нет — используем значение null
  const [navData, setNavData] = useState(null)

  // useEffect сработает сразу после первого показа компонента на странице
  useEffect(() => {
    // Делаем GET-запрос на адрес http://127.0.0.1:8000/api/navbar/
    // Ожидаем, что сервер вернёт JSON с логотипом и ссылками
    axios.get("http://127.0.0.1:8000/api/navbar/")
      .then(response => {
        // Если запрос успешен — сохраняем данные в состояние
        setNavData(response.data)
      })
      .catch(error => {
        // Если возникла ошибка — выводим её в консоль
        console.error("Ошибка при получении навбара", error)
      })
  }, [])  // Пустой массив зависимостей означает, что код внутри выполнится один раз

  // Пока данные ещё загружаются — показываем временное сообщение
  if (!navData) return <p>Загрузка меню...</p>

  // Как только данные загрузятся — отображаем логотип и ссылки
  return (
    <header style={{ backgroundColor: "#f0f0f0", padding: "10px" }}>
      {/* Отображаем логотип. Ссылка на картинку приходит с сервера */}
      <img src={navData.logo} alt="Logo" style={{ height: "50px" }} />

      {/* Рядом показываем список ссылок, которые пришли с сервера */}
      <nav style={{ display: "inline-block", marginLeft: "30px" }}>
        {/* Перебираем массив ссылок и для каждой создаём <a> */}
        {navData.links.map((link, idx) => (
          <a key={idx} href={link.url} style={{ marginRight: "15px" }}>
            {link.name}
          </a>
        ))}
      </nav>
    </header>
  )
}

// Экспортируем компонент, чтобы можно было использовать его в других файлах (например, в App.js)
export default Navbar
