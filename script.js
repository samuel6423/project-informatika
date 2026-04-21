document.getElementById('generateBtn').addEventListener('click', function() {
    const vesValue = document.getElementById('vesInput').value;
    const statusEl = document.getElementById('status');
    const imageContainer = document.getElementById('imageContainer');
    
    if (!vesValue.trim()) {
        alert('Prosím, zadajte nejaký kód do poľa.');
        return;
    }

    statusEl.textContent = 'Spracovávam...';
    imageContainer.innerHTML = '';

    fetch('/generate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ ves_input: vesValue })
    })
    .then(response => {
        if (!response.ok) {
            return response.json().then(err => { throw new Error(err.error || 'Chyba servera'); });
        }
        return response.blob();
    })
    .then(blob => {
        const imageUrl = URL.createObjectURL(blob);
        const img = document.createElement('img');
        img.src = imageUrl;
        img.alt = 'Vygenerovaný obrázok';
        
        imageContainer.appendChild(img);
        statusEl.textContent = 'Obrázok bol úspešne vygenerovaný.';
    })
    .catch(error => {
        console.error('Chyba:', error);
        statusEl.textContent = 'Nastala chyba: ' + error.message;
    });
});

function getRandomColor() {
    const letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}

function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

document.getElementById('randomVesBtn').addEventListener('click', function() {
    const width = 500;
    const height = 500;
    let ves = `VES 1.0 ${width} ${height}\n`;
    ves += `CLEAR #FFFFFF\n`;
    
    const numShapes = getRandomInt(10, 20);
    const shapes = ['LINE', 'RECT', 'TRIANGLE', 'CIRCLE', 'FILL_CIRCLE', 'FILL_TRIANGLE', 'FILL_RECT'];
    
    for (let i = 0; i < numShapes; i++) {
        const shape = shapes[Math.floor(Math.random() * shapes.length)];
        const color = getRandomColor();
        const thickness = getRandomInt(2, 6);
        
        if (shape === 'LINE') {
            ves += `LINE ${getRandomInt(0, width)} ${getRandomInt(0, height)} ${getRandomInt(0, width)} ${getRandomInt(0, height)} ${thickness} ${color}\n`;
        } else if (shape === 'RECT') {
            ves += `RECT ${getRandomInt(0, width)} ${getRandomInt(0, height)} ${getRandomInt(20, 150)} ${getRandomInt(20, 150)} ${thickness} ${color}\n`;
        } else if (shape === 'TRIANGLE') {
            ves += `TRIANGLE ${getRandomInt(0, width)} ${getRandomInt(0, height)} ${getRandomInt(0, width)} ${getRandomInt(0, height)} ${getRandomInt(0, width)} ${getRandomInt(0, height)} ${thickness} ${color}\n`;
        } else if (shape === 'CIRCLE') {
            ves += `CIRCLE ${getRandomInt(0, width)} ${getRandomInt(0, height)} ${getRandomInt(10, 80)} ${thickness} ${color}\n`;
        } else if (shape === 'FILL_CIRCLE') {
            ves += `FILL_CIRCLE ${getRandomInt(0, width)} ${getRandomInt(0, height)} ${getRandomInt(10, 80)} ${color}\n`;
        } else if (shape === 'FILL_TRIANGLE') {
            ves += `FILL_TRIANGLE ${getRandomInt(0, width)} ${getRandomInt(0, height)} ${getRandomInt(0, width)} ${getRandomInt(0, height)} ${getRandomInt(0, width)} ${getRandomInt(0, height)} ${color}\n`;
        } else if (shape === 'FILL_RECT') {
            ves += `FILL_RECT ${getRandomInt(0, width)} ${getRandomInt(0, height)} ${getRandomInt(20, 150)} ${getRandomInt(20, 150)} ${color}\n`;
        }
    }
    
    document.getElementById('vesInput').value = ves;
    document.getElementById('generateBtn').click(); // Automaticky vygeneruje obrázok
});
