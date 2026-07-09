from flask import Flask, render_template, request, jsonify
import requests
from datetime import datetime
import sqlite3







app = Flask(__name__)


# ============================================
# DATABASE
# ============================================

DATABASE ="weather.db"


def get_connection():

    conn = sqlite3.connect(DATABASE)

    conn.row_factory = sqlite3.Row

    return conn

# ============================================
# CREATE TABLE
# ============================================

def create_table():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS searches(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            city TEXT NOT NULL,

            searched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )

    """)

    conn.commit()

    conn.close()

create_table()


# ============================================
# SAVE SEARCH
# ============================================

def save_search(city):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO searches(city)

        VALUES(?)

    """,(city,))

    conn.commit()

    conn.close()


# ============================================
# WEATHER CODE TO ICON
# ============================================

WEATHER_CODES = {
    0: ("Clear Sky", "https://openweathermap.org/img/wn/01d@2x.png"),
    1: ("Mainly Clear", "https://openweathermap.org/img/wn/02d@2x.png"),
    2: ("Partly Cloudy", "https://openweathermap.org/img/wn/03d@2x.png"),
    3: ("Overcast", "https://openweathermap.org/img/wn/04d@2x.png"),
    45: ("Fog", "https://openweathermap.org/img/wn/50d@2x.png"),
    48: ("Fog", "https://openweathermap.org/img/wn/50d@2x.png"),
    51: ("Light Drizzle", "https://openweathermap.org/img/wn/09d@2x.png"),
    61: ("Rain", "https://openweathermap.org/img/wn/10d@2x.png"),
    63: ("Moderate Rain", "https://openweathermap.org/img/wn/10d@2x.png"),
    65: ("Heavy Rain", "https://openweathermap.org/img/wn/10d@2x.png"),
    80: ("Rain Showers", "https://openweathermap.org/img/wn/09d@2x.png"),
    95: ("Thunderstorm", "https://openweathermap.org/img/wn/11d@2x.png")
}

# ============================================
# GET LATITUDE & LONGITUDE
# ============================================

def get_location(city):

    url = (
        "https://geocoding-api.open-meteo.com/v1/search"
        f"?name={city}&count=1"
    )

    print("URL:", url)

    response = requests.get(url, timeout=10)

    response.raise_for_status()

    data = response.json()

    print("Response:", data)

    if "results" not in data:
        return None

    return data["results"][0]


# ============================================
# GET WEATHER DATA
# ============================================

def get_weather(latitude, longitude):

    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        "&current=temperature_2m,"
        "relative_humidity_2m,"
        "apparent_temperature,"
        "weather_code,"
        "wind_speed_10m"
        "&daily=weather_code,"
        "temperature_2m_max,"
        "sunrise,"
        "sunset"
        "&timezone=auto"
    )

    response = requests.get(url, timeout=10)

    response.raise_for_status()

    return response.json()

@app.route("/weather")
def weather():

    city = request.args.get("city")
    print("User searched:", city)

    if not city:

        return jsonify({
            "error": "Please enter a city."
        }), 400

    try:

        # -----------------------------
        # Get City Coordinates
        # -----------------------------

        place = get_location(city)
        print(place)

        if place is None:

            return jsonify({
                "error": "City not found."
            }), 404

        latitude = place["latitude"]
        longitude = place["longitude"]
        city_name = place["name"]
        save_search(city_name)

        # -----------------------------
        # Get Weather
        # -----------------------------

        weather = get_weather(latitude, longitude)

        current = weather["current"]
        daily = weather["daily"]

        description, icon = WEATHER_CODES.get(
            current["weather_code"],
            ("Unknown",
             "https://openweathermap.org/img/wn/01d@2x.png")
        )

        forecast = []

        for i in range(7):

            date = datetime.strptime(
                daily["time"][i],
                "%Y-%m-%d"
            )

            day = date.strftime("%a")

            forecast_description, forecast_icon = WEATHER_CODES.get(
                daily["weather_code"][i],
                ("Unknown",
                 "https://openweathermap.org/img/wn/01d@2x.png")
            )

            forecast.append({

                "day": day,

                "temperature": daily["temperature_2m_max"][i],

                "description": forecast_description,

                "icon": forecast_icon

            })

        return jsonify({

            "city": city_name,

            "temperature": current["temperature_2m"],

            "description": description,

            "feels_like": current["apparent_temperature"],

            "humidity": current["relative_humidity_2m"],

            "wind": current["wind_speed_10m"],

            "sunrise": daily["sunrise"][0].split("T")[1],

            "sunset": daily["sunset"][0].split("T")[1],

            "icon": icon,

            "forecast": forecast

        })

    except requests.exceptions.Timeout:

        return jsonify({
            "error": "The weather service timed out."
        }), 504

    except requests.exceptions.ConnectionError:

        return jsonify({
            "error": "Unable to connect to the weather service."
        }), 503

    except requests.exceptions.HTTPError:

        return jsonify({
            "error": "Weather service returned an error."
        }), 502

    except Exception as e:

      print(e)

    return jsonify({
        "error": "Something went wrong."
    }), 500
    
# ============================================
# RECENT SEARCHES
# ============================================

def get_recent_searches(limit=10):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

        SELECT city,searched_at

        FROM searches

        ORDER BY searched_at DESC

        LIMIT ?

    """,(limit,))

    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]

@app.route("/history")
def history():

    return jsonify(

        get_recent_searches()

    )


# ============================================
# HOME PAGE
# ============================================

@app.route("/")
def home():
    return render_template("index.html")

# ============================================
# RUN FLASK
# ============================================

if __name__ == "__main__":
    app.run(debug=True)