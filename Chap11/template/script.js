document.getElementById('prediction-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const area = parseFloat(document.getElementById('area').value);
    const num_bedrooms = parseInt(document.getElementById('num_bedrooms').value);
    const num_bathrooms = parseInt(document.getElementById('num_bathrooms').value);

    const houseData = {
        area: area,
        num_bedrooms: num_bedrooms,
        num_bathrooms: num_bathrooms
    };
    console.log("house", houseData);

    fetch('http://127.0.0.1:8000/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify([houseData])
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('predicted-price').textContent = `${data.predicted_price[0].toFixed(2)}`;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
