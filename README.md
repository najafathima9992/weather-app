# 🌦️ Weather Dashboard

A modern, responsive Weather Dashboard built with **Python Flask**, **HTML**, **CSS**, and **JavaScript**. The application allows users to search for any city and view the current weather conditions, a 7-day forecast, and temperature trends using the Open-Meteo API.

---

## 🚀 Features

- 🌍 Search weather by city
- 🌡️ Current temperature
- ☁️ Weather description
- 🌬️ Wind speed
- 💧 Humidity
- 🌅 Sunrise & Sunset time
- 📅 7-Day Weather Forecast
- 📈 Temperature Trend Chart
- 🌙 Dark Mode
- 📱 Responsive Design
- 💾 SQLite Database for Search History
- ⚡ REST API using Flask
- 📝 Logging Support
- 🔒 Error Handling
- 🚀 Ready for AWS Deployment

---

## 🛠️ Tech Stack

### Frontend

- HTML5
- CSS3
- JavaScript (ES6)
- Font Awesome
- Chart.js

### Backend

- Python
- Flask
- SQLite3
- Requests Library

### Weather API

- Open-Meteo API
- Open-Meteo Geocoding API

---

## 📁 Project Structure

```
weather_dashboard/
│
├── static/
│   ├── css/
│   │    └── style.css
│   │
│   ├── js/
│   │    └── app.js
│   │
│   └── images/
│
├── templates/
│   ├── base.html
│   └── index.html
│
├── logs/
│   └── app.log
│
├── weather.db
├── app.py
├── config.py
├── requirements.txt
├── .env
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/weather-dashboard.git
```

```bash
cd weather-dashboard
```

---

### Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

## 🌐 Weather API

This project uses the free Open-Meteo API.

Current Weather

```
https://api.open-meteo.com/v1/forecast
```

Geocoding API

```
https://geocoding-api.open-meteo.com/v1/search
```

No API key is required.

---

## 💾 Database

SQLite is used to store user search history.

Table

```
searches
```

Columns

| Column | Type |
|---------|------|
| id | Integer |
| city | Text |
| searched_at | Timestamp |

---

## 📊 API Endpoints

### Home

```
GET /
```

Returns the main dashboard.

---

### Weather

```
GET /weather?city=London
```

Example Response

```json
{
  "city":"London",
  "temperature":22,
  "description":"Partly Cloudy",
  "humidity":72,
  "wind":18
}
```

---

### Search History

```
GET /history
```

Returns recent searches stored in SQLite.

---

## 🌙 Dark Mode

Click the moon icon to switch between Light Mode and Dark Mode.

---

## 📈 Temperature Chart

Chart.js is used to visualize the 7-day temperature forecast.

---

## 🚀 Deployment

The application can be deployed on:

- AWS EC2
- Nginx
- Gunicorn
- Docker
- Render
- Railway
- PythonAnywhere

---

## 🔒 Security Features

- Input Validation
- HTTP Error Handling
- Request Timeout
- Logging
- Environment Variables
- SQLite Parameterized Queries

---

## 📚 Learning Outcomes

This project demonstrates knowledge of:

- Python Programming
- Flask Framework
- REST APIs
- JSON Handling
- SQLite Database
- HTML
- CSS
- JavaScript
- AJAX (Fetch API)
- Chart.js
- Responsive Web Design
- Error Handling

---

## 📄 License

This project is licensed under the MIT License.

Feel free to use, modify, and distribute this project for educational purposes.
