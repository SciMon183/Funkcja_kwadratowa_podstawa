    // Pobierz guzik, modal i inputy
    var btn = document.getElementById('fnsqr');
    var modal = document.getElementById('myModal');
    var coefficientAInput = document.getElementById('coefficientA');
    var coefficientBInput = document.getElementById('coefficientB');
    var coefficientCInput = document.getElementById('coefficientC');
    var resultDiv = document.getElementById('result');

    // Dodaj obsługę zdarzenia kliknięcia na guziku
    btn.addEventListener('click', function() {
        // Wyczyść poprzednie wartości inputów i wyniku
        coefficientAInput.value = '';
        coefficientBInput.value = '';
        coefficientCInput.value = '';
        resultDiv.innerHTML = '';

        // Pokaż modal
        modal.style.display = 'block';
    });

    // Funkcja do zamykania modalu
    function closeModal() {
        modal.style.display = 'none';
    }

    // Funkcja do obliczania równania kwadratowego
    function calculateQuadraticEquation() {
        var a = parseFloat(coefficientAInput.value);
        var b = parseFloat(coefficientBInput.value);
        var c = parseFloat(coefficientCInput.value);

        // Wyślij dane do pliku Python za pomocą AJAX
        $.ajax({
            type: 'POST',
            url: 'process.py', // Adres pliku Python
            data: { a: a, b: b, c: c },
            success: function(response) {
                // Wyświetl wynik w divie
                resultDiv.innerHTML = 'Wynik z Pythona: ' + response;
            },
            error: function(error) {
                console.error('Błąd AJAX:', error);
            }
        });

        // Zamknij modal po wysłaniu danych
        closeModal();
    }

    // Dodaj obsługę zamykania modalu po kliknięciu poza nim
    window.addEventListener('click', function(event) {
        if (event.target === modal) {
            closeModal();
        }
    });