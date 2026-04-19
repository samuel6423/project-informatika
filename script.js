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
