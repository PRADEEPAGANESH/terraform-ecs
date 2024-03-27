window.onload = function() {
    fetch('/api/data')
    .then(response => response.json())
    .then(data => {
        const container = document.getElementById('data-container');
        container.innerHTML = `<p>Data from server: ${data.message}</p>`;
    })
    .catch(error => console.error('Error fetching data:', error));
};
    