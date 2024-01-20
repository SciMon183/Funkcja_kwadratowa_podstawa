// Pobierz guzik i modal
var btn = document.getElementById('fnsqr');
var modal = document.getElementById('oknofnsqr');

// Dodaj obsługę zdarzenia kliknięcia na guziku
btn.addEventListener('click', function() {
    modal.style.display = 'block';
});

// Funkcja do zamykania modalu
function closeModal() {
    modal.style.display = 'none';
}

// Dodaj obsługę zamykania modalu po kliknięciu poza nim
window.addEventListener('click', function(event) {
    if (event.target === modal) {
        closeModal();
    }
});