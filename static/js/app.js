// ======================================
// SELECT HTML ELEMENTS
// ======================================

const cityInput = document.getElementById("city");

const searchBtn = document.getElementById("search-btn");

const cityName = document.getElementById("city-name");

const temperature = document.getElementById("temperature");

const description = document.getElementById("description");

const feelsLike = document.getElementById("feels-like");

const humidity = document.getElementById("humidity");

const wind = document.getElementById("wind");

const sunrise = document.getElementById("sunrise");

const sunset = document.getElementById("sunset");

const weatherIcon = document.getElementById("weather-icon");

const themeBtn = document.getElementById("theme-btn");


// ======================================
// WEATHER API
// ======================================

// We will replace this later with Flask API.

const API_URL = "/weather";


// ======================================
// SEARCH BUTTON
// ======================================




// ======================================
// PRESS ENTER TO SEARCH
// ======================================

cityInput.addEventListener("keypress", function(event){

    if(event.key === "Enter"){

        searchWeather();

    }

});


// ======================================
// SEARCH WEATHER
// ======================================

async function searchWeather(){

    const city = cityInput.value.trim();

    if(city === ""){

        alert("Please enter a city name.");

        return;

    }

    try{

        const response = await fetch(`/weather?city=${encodeURIComponent(city)}`);

        if(!response.ok){

            throw new Error("Weather not found");

        }

        const data = await response.json();

        updateUI(data);

    }

    catch(error){

        alert(error.message);

    }

}


// ======================================
// UPDATE UI
// ======================================

function updateUI(data){

    cityName.textContent = data.city;

    temperature.textContent = data.temperature + "°C";

    description.textContent = data.description;

    feelsLike.textContent = data.feels_like + "°C";

    humidity.textContent = data.humidity + "%";

    wind.textContent = data.wind + " km/h";

    sunrise.textContent = data.sunrise;

    sunset.textContent = data.sunset;

    weatherIcon.src = data.icon;

}


// ======================================
// DARK MODE
// ======================================

themeBtn.addEventListener("click", function(){

    document.body.classList.toggle("dark-mode");

});


// ======================================
// TEMPERATURE CHART
// ======================================

let tempChart = null;


// ======================================
// SHOW LOADING
// ======================================

function showLoading(){

    searchBtn.innerHTML = `
        <i class="fa-solid fa-spinner fa-spin"></i>
        Loading...
    `;

    searchBtn.disabled = true;

}


// ======================================
// HIDE LOADING
// ======================================

function hideLoading(){

    searchBtn.innerHTML = `
        <i class="fa-solid fa-magnifying-glass"></i>
        Search
    `;

    searchBtn.disabled = false;

}


// ======================================
// UPDATED SEARCH FUNCTION
// ======================================

async function searchWeather(){

    const city = cityInput.value.trim();

    if(city === ""){

        alert("Please enter a city name.");

        return;

    }

    showLoading();

    try{

        const response = await fetch(`/weather?city=${city}`);

        if(!response.ok){

            throw new Error("City not found.");

        }

        const data = await response.json();

        updateUI(data);

        updateForecast(data.forecast);

        drawChart(data.forecast);

    }

    catch(error){

        alert(error.message);

    }

    finally{

        hideLoading();

    }

}

// ======================================
// UPDATE FORECAST
// ======================================

function updateForecast(forecast){

    const container = document.querySelector(".forecast-container");

    container.innerHTML = "";

    forecast.forEach(day =>{

        container.innerHTML += `

        <div class="forecast-card">

            <h3>${day.day}</h3>

            <img
                src="${day.icon}"
                width="60">

            <p>${day.temperature}°C</p>

        </div>

        `;

    });

}

// ======================================
// DRAW CHART
// ======================================

function drawChart(forecast){

    const ctx = document.getElementById("tempChart");

    const labels = forecast.map(day => day.day);

    const temps = forecast.map(day => day.temperature);

    if(tempChart){

        tempChart.destroy();

    }

    tempChart = new Chart(ctx,{

        type:"line",

        data:{

            labels:labels,

            datasets:[{

                label:"Temperature",

                data:temps,

                fill:false,

                borderColor:"#3B82F6",

                tension:0.4,

                borderWidth:3

            }]

        },

        options:{

            responsive:true,

            maintainAspectRatio:false,

            plugins:{

                legend:{

                    display:true

                }

            }

        }

    });

}

// ======================================
// LOAD DEFAULT CITY
// ======================================

window.onload = function(){

    cityInput.value = "Kozhikode";

    searchWeather();

};