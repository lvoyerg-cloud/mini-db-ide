# ⚡ Multi-DB IDE (SQL & NoSQL) - UMG

> Mini Entorno de Desarrollo (IDE) para Bases de Datos Relacionales (SQLite) y Orientadas a Documentos (MongoDB / JSON).

---

## 🎓 Información Académica
* **Universidad:** Universidad Mariano Gálvez de Guatemala (UMG)
* **Facultad:** Ingeniería en Sistemas de Información
* **Sede:** Retalhuleu
* **Curso:** Bases De Datos I
* **Catedrático:** Ing. Yoel Monzón
* **Integrantes:**
  * Louis Neil Voyer García (2890-24-16741)
  * Gabriel Polero (2890-24-8909)
  * Cristel Hayde Maldonado Zelada (2890-24-19621)

---

## 📜 Descripción del Proyecto
Aplicación de escritorio desarrollada en **Python (Tkinter)** que permite conectarse a bases de datos relacionales (**SQLite**) y de documentos (**MongoDB**), ejecutar sentencias DDL y DML, y visualizar los resultados en una interfaz gráfica estilizada en Dark Mode.

---

## 📸 Capturas de Pantalla del Sistema

### 🛢️ Consola SQL (SQLite)
![Ejecución SQL](img/sql_demo.png)

### 🍃 Consola NoSQL (MongoDB / JSON)
![Ejecución NoSQL](img/nosql_demo.png)

---

## 🛢️ Bases de Datos Utilizadas
| Característica | Base de Datos SQL | Base de Datos NoSQL |
| :--- | :--- | :--- |
| **Tecnología** | SQLite 3 | MongoDB / PyMongo |
| **Tipo** | Relacional (Tablas / Filas) | Documentos (JSON / BSON) |
| **Conexión** | Archivo .db | URI mongodb://localhost:27017 |

---

## 💻 Instalación y Ejecución
`ash
pip install pymongo
python main.py
`

---

## 🧠 Reflexión Personal sobre Retos y Aprendizajes
* **Reto Técnico:** Renderizar dinámicamente diferentes tipos de datos en la interfaz gráfica (Treeview de Tkinter) al recibir resultados de consultas SQL o documentos JSON con esquemas dinámicos.
* **Aprendizaje:** Comprensión práctica del manejo simultáneo de bases de datos relacionales transaccionales y bases de datos NoSQL de alta flexibilidad.
