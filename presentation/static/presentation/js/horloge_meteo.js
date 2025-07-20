console.log("✅ Script horloge_meteo.js chargé");

// === Horloge ===
function updateClock() {
    const now = new Date();
    const options = { hour: '2-digit', minute: '2-digit', second: '2-digit' };
    const timeString = now.toLocaleTimeString([], options);
    document.getElementById('horloge').textContent = 'Heure locale : ' + timeString;
}
setInterval(updateClock, 1000);
updateClock();

// === Météo ===
const apiKey = '884384c38cbbd67ed9a36d2708dd045a'; // Remplace par ta clé OpenWeatherMap
const ville = 'Abidjan,CI';

async function fetchWeather() {
    try {
        console.log("🌍 Récupération des données météo...");
        const response = await fetch(`https://api.openweathermap.org/data/2.5/weather?q=${ville}&units=metric&lang=fr&appid=${apiKey}`);
        const data = await response.json();
        console.log("Réponse API météo :", data);

        if (data.cod === 200) {
            const desc = data.weather[0].description;
            const temp = Math.round(data.main.temp);
            document.getElementById('meteo').textContent = `Météo à ${ville} : ${desc}, ${temp}°C`;
        } else {
            document.getElementById('meteo').textContent = '❌ Impossible de récupérer la météo.';
        }
    } catch (error) {
        console.error("Erreur lors de la récupération météo:", error);
        document.getElementById('meteo').textContent = '⚠️ Erreur lors de la récupération météo.';
    }
}

fetchWeather();
