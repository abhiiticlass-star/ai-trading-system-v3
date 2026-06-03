const API = "https://ai-trading-system-v3.onrender.com";

let chart;

// 🔥 GET SIGNAL + UPDATE CHART
async function getSignal() {

    let pair = document.getElementById("pair").value;

    let res = await fetch(`${API}/signal?pair=${pair}`);
    let data = await res.json();

    document.getElementById("signalBox").innerHTML =
        `<h2>${data.signal}</h2>
         <p>UP: ${data.up_probability || 0}</p>
         <p>DOWN: ${data.down_probability || 0}</p>`;

    loadChart(pair);
}


// 🔥 LOAD CHART
async function loadChart(pair) {

    let res = await fetch(`${API}/candles?pair=${pair}`);
    let data = await res.json();

    let candles = data.candles || [];

    let labels = candles.map(c => c.datetime || "");
    let prices = candles.map(c => c.close);

    if (chart) chart.destroy();

    chart = new Chart(document.getElementById("chart"), {
        type: "line",
        data: {
            labels: labels.reverse(),
            datasets: [{
                label: "Price",
                data: prices.reverse(),
                borderWidth: 2
            }]
        }
    });
}


// 🔥 AUTO UPDATE EVERY 5 SEC
setInterval(() => {

    let pair = document.getElementById("pair").value;

    loadChart(pair);

}, 5000);
