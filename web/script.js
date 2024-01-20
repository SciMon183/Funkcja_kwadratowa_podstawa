
    // Pobierz guzik, modal i inputy
    var btn = document.getElementById('fnsqr');
    var modal = document.getElementById('myModal');
    var coefficientAInput = document.getElementById('coefficientA');
    var coefficientBInput = document.getElementById('coefficientB');
    var coefficientCInput = document.getElementById('coefficientC');
    var resultDiv = document.getElementById('result');
    var chartDiv = document.getElementById('chart'); // Dodane miejsce na wykres

    // Dodaj obsługę zdarzenia kliknięcia na guziku
    btn.addEventListener('click', function() {
        // Wyczyść poprzednie wartości inputów, wyniku i wykresu
        coefficientAInput.value = '';
        coefficientBInput.value = '';
        coefficientCInput.value = '';
        resultDiv.innerHTML = '';
        chartDiv.innerHTML = '';

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

    // Utwórz obiekt FormData i dodaj do niego dane
    var formData = new FormData();
    formData.append('a', a);
    formData.append('b', b);
    formData.append('c', c);

    // Wyślij dane do pliku Pythona za pomocą AJAX
    $.ajax({
        type: 'POST',
        url: 'app.py', // Zaktualizowana ścieżka do pliku Pythona
        data: formData,
        processData: false,
        contentType: false,
        success: function(response) {
            // Wyświetl wynik w divie
            resultDiv.innerHTML = 'Wynik z Pythona: ' + JSON.stringify(response);

            // Narysuj wykres
            drawChart(response);
        },
        error: function(error) {
            console.error('Błąd AJAX:', error);
        }
    });

    // Zamknij modal po wysłaniu danych
    closeModal();

    // Zapobiegaj domyślnemu zachowaniu formularza
    return false;
}


    // Funkcja do rysowania wykresu za pomocą Plotly
    function drawChart(response) {
        var delta = response.delta;
        var miejscaZerowe = response.miejsca_zerowe;

        var trace = {
            x: miejscaZerowe,
            y: [0, 0], // Linia pozioma na osi y
            type: 'scatter',
            mode: 'markers',
            marker: {
                color: 'red',
                size: 10,
            },
        };

        var layout = {
            title: 'Wykres miejsc zerowych',
            xaxis: {
                title: 'Miejsca zerowe',
                zeroline: false,
            },
            yaxis: {
                showgrid: false,
                zeroline: false,
            },
            showlegend: false,
        };

        Plotly.newPlot(chartDiv, [trace], layout);
    }

    // Dodaj obsługę zamykania modalu po kliknięciu poza nim
    window.addEventListener('click', function(event) {
        if (event.target === modal) {
            closeModal();
        }
    });

