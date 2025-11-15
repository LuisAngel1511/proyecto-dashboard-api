// frontend/app.js
console.log("--- EL SCRIPT HA INICIADO ---");
alert("¡El script está vivo!"); 

// ... aquí sigue el resto de tu código ...
document.addEventListener("DOMContentLoaded", () => {
    console.log("Intentando cargar datos...");
    cargarDatosDelDashboard();
});
// ...
/* frontend/app.js */
document.addEventListener("DOMContentLoaded", () => {
    cargarDatosDelDashboard();
});

async function cargarDatosDelDashboard() {
    try {
const response = await fetch('https://proyecto-dashboard-api.onrender.com/api/calidad-datos/');        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();

        pintarResumen(data.resumen);
        pintarGraficoNulos(data.valores_nulos_por_columna);
        pintarGraficoDuplicados(data.conteo_duplicados);
        pintarGraficoTipos(data.distribucion_tipos_datos);

    } catch (error) { console.error("Error:", error); }
}

function pintarResumen(resumen) {
    document.getElementById('nombre-dataset').textContent = `Dataset: ${resumen.dataset_nombre}`;
}

function pintarGraficoNulos(dataNulos) {
    const ctx = document.getElementById('graficoNulos').getContext('2d');
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: dataNulos.columnas,
            datasets: [{
                label: 'Cantidad de Nulos',
                data: dataNulos.conteo,
                backgroundColor: 'rgba(255, 99, 132, 0.6)'
            }]
        },
        options: { scales: { y: { beginAtZero: true } }, responsive: true }
    });
}

function pintarGraficoDuplicados(dataDuplicados) {
    const ctx = document.getElementById('graficoDuplicados').getContext('2d');
    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: dataDuplicados.etiquetas,
            datasets: [{
                data: dataDuplicados.conteo,
                backgroundColor: ['rgba(54, 162, 235, 0.6)', 'rgba(255, 206, 86, 0.6)']
            }]
        },
        options: { responsive: true }
    });
}

function pintarGraficoTipos(dataTipos) {
    const ctx = document.getElementById('graficoTiposDatos').getContext('2d');
    new Chart(ctx, {
        type: 'pie',
        data: {
            labels: dataTipos.etiquetas,
            datasets: [{
                data: dataTipos.conteo,
                backgroundColor: ['rgba(75, 192, 192, 0.6)', 'rgba(153, 102, 255, 0.6)', 'rgba(255, 159, 64, 0.6)']
            }]
        },
        options: { responsive: true }
    });
}