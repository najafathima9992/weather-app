# 🌦️ Weather Dashboard

A modern Weather Dashboard built using **Python Flask**, **HTML**, **CSS**, **JavaScript**, and **SQLite**. The application provides real-time weather information and a 7-day forecast for any city using the Open-Meteo API. It is deployed on **AWS EC2** using **Gunicorn** and **Nginx** with a custom **DuckDNS** domain.

---

## 🚀 Live Demo

**URL:** http://weatherforcast.duckdns.org


# ✨ Features

- 🌍 Search weather by city name
- 🌡️ Current temperature
- ☁️ Weather condition
- 💧 Humidity
- 🌬️ Wind Speed
- 🌅 Sunrise Time
- 🌇 Sunset Time
- 📅 7-Day Weather Forecast
- 📈 Temperature Trend Chart
- 🌙 Dark Mode
- 💾 Stores search history using SQLite
- 📱 Responsive UI
- ☁️ Deployed on AWS EC2
- 🔄 Reverse Proxy using Nginx
- ⚡ Production deployment using Gunicorn

---

# 🛠 Technologies Used

## Backend

- Python 3
- Flask
- Requests
- SQLite

## Frontend

- HTML5
- CSS3
- JavaScript
- Font Awesome
- Chart.js

## Deployment

- AWS EC2
- Gunicorn
- Nginx
- DuckDNS

---

# 📂 Project Structure

```
weather-app/
│
├── app.py
├── weather.db
├── requirements.txt
├── README.md
│
├── static/
│   ├── css/
│   │     └── style.css
│   │
│   ├── js/
│   │     └── script.js
│   │
│   └── images/
│
├── templates/
│   ├── base.html
│   └── index.html
│
└── venv/
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/weather-dashboard.git
```

```bash
cd weather-dashboard
```

---

## Create Virtual Environment

Linux

```bash
python3 -m venv venv
```

Windows

```bash
python -m venv venv
```

---

## Activate Virtual Environment

Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
python app.py
```

Application runs on

```
http://127.0.0.1:5000
```

---

# ☁️ Deployment

The application is deployed using

- AWS EC2
- Gunicorn
- Nginx
- DuckDNS

Gunicorn Command

```bash
gunicorn --bind 127.0.0.1:8000 app:app
```

Nginx Reverse Proxy

```nginx
server {

    listen 80;

    server_name weatherforcast.duckdns.org;

    location / {

        proxy_pass http://127.0.0.1:8000;

        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

    }

}
```

Restart Nginx

```bash
sudo nginx -t
sudo systemctl restart nginx
```

---

# 🌐 Weather API

This project uses

**Open-Meteo API**

Features used

- Current Weather
- Weather Codes
- Temperature
- Humidity
- Wind Speed
- Sunrise
- Sunset
- Daily Forecast

---

# 📊 Database

SQLite Database

Table

```
searches
```

Columns

| Column | Type |
|---------|------|
| id | INTEGER |
| city | TEXT |
| searched_at | TIMESTAMP |

---

# 📡 API Endpoints

## Home

```
GET /
```

Returns the Weather Dashboard.

---

## Weather

```
GET /weather?city=London
```

Returns weather details for a city.

---

## Search History

```
GET /history
```

Returns recently searched cities.

---

# 🖥 Application Workflow

```
User
   │
   ▼
Browser
   │
   ▼
JavaScript Fetch API
   │
   ▼
Flask Backend
   │
   ▼
Open-Meteo API
   │
   ▼
Weather Data
   │
   ▼
JSON Response
   │
   ▼
Frontend UI
```

---

# AWS Deployment Architecture

```
                Internet
                     │
                     ▼
      weatherforcast.duckdns.org
                     │
                     ▼
            Nginx (Port 80)
                     │
             Reverse Proxy
                     │
                     ▼
     Gunicorn (127.0.0.1:8000)
                     │
                     ▼
            Flask Application
                     │
         ┌───────────┴───────────┐
         ▼                       ▼
     SQLite Database       Open-Meteo API
```

---

# Future Improvements

- HTTPS using Let's Encrypt
- User Authentication
- Favourite Cities
- Air Quality Index
- Hourly Forecast
- Weather Notifications
- Docker Support
- CI/CD using GitHub Actions
- AWS CloudWatch Monitoring

---

# Skills Demonstrated

- Python
- Flask
- REST API
- SQLite
- HTML
- CSS
- JavaScript
- JSON
- API Integration
- Linux
- Gunicorn
- Nginx
- AWS EC2
- DNS Configuration
- Reverse Proxy
- Web Deployment

---


# License

This project is developed for educational and portfolio purposes.
