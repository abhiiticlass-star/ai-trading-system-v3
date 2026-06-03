async function getSignal() {
    let pair = document.getElementById("pair").value;

    let res = await fetch(`http://localhost:5000/signal?pair=${pair}`);
    let data = await res.json();

    document.getElementById("result").innerHTML =
        `Signal: ${data.signal} <br> UP: ${data.up_probability}`;
}
