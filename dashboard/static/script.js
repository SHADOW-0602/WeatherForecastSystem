document.addEventListener('DOMContentLoaded', function() {
    // Update time display
    document.getElementById('update-time').textContent = new Date().toLocaleString();
    
    // Handle location form submission
    document.getElementById('location-form').addEventListener('submit', function(e) {
        e.preventDefault();
        const location = document.getElementById('location-input').value;
        fetchWeatherData(location);
    });
    
    // Initialize with default data if available
    if (window.initialData) {
        renderCharts(window.initialData);
        renderForecastTable(window.initialData);
    }
});

function fetchWeatherData(location) {
    fetch(`/api/weather?location=${encodeURIComponent(location)}`)
        .then(response => response.json())
        .then(data => {
            renderCharts(data);
            renderForecastTable(data);
            updateCurrentWeather(data.current);
        })
        .catch(error => {
            console.error('Error fetching weather data:', error);
            alert('Failed to fetch weather data. Please try again.');
        });
}

function renderCharts(data) {
    // Temperature chart
    const tempTrace = {
        x: data.hourly.time,
        y: data.hourly.temperature,
        type: 'line',
        name: 'Temperature (°C)',
        line: {color: '#e74c3c'}
    };
    
    Plotly.newPlot('temperature-chart', [tempTrace], {
        title: 'Temperature Forecast',
        xaxis: {title: 'Time'},
        yaxis: {title: 'Temperature (°C)'}
    });
    
    // Precipitation chart
    const precipTrace = {
        x: data.hourly.time,
        y: data.hourly.precipitation,
        type: 'bar',
        name: 'Precipitation (mm)',
        marker: {color: '#3498db'}
    };
    
    Plotly.newPlot('precipitation-chart', [precipTrace], {
        title: 'Precipitation Forecast',
        xaxis: {title: 'Time'},
        yaxis: {title: 'Precipitation (mm)'}
    });
}

function renderForecastTable(data) {
    const tableBody = document.getElementById('forecast-data');
    tableBody.innerHTML = '';
    
    // Sample implementation - would use actual forecast data in real app
    for (let i = 0; i < 7; i++) {
        const row = document.createElement('tr');
        
        const dateCell = document.createElement('td');
        dateCell.textContent = new Date(Date.now() + i * 24 * 60 * 60 * 1000).toLocaleDateString();
        
        const tempCell = document.createElement('td');
        tempCell.textContent = `${Math.round(15 + Math.random() * 15)}°C`;
        
        const condCell = document.createElement('td');
        condCell.textContent = ['Sunny', 'Cloudy', 'Rainy'][Math.floor(Math.random() * 3)];
        condCell.className = `condition ${condCell.textContent.toLowerCase()}`;
        
        const precipCell = document.createElement('td');
        precipCell.textContent = `${Math.round(Math.random() * 10)} mm`;
        
        row.appendChild(dateCell);
        row.appendChild(tempCell);
        row.appendChild(condCell);
        row.appendChild(precipCell);
        
        tableBody.appendChild(row);
    }
}

function updateCurrentWeather(current) {
    document.getElementById('current-temp').textContent = current.temperature.toFixed(1);
    const conditionElement = document.getElementById('weather-condition');
    conditionElement.textContent = current.condition;
    conditionElement.className = `condition ${current.condition.toLowerCase().replace(' ', '-')}`;
}
