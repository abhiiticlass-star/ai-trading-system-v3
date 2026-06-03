const API = "https://your-render-url.onrender.com";

async function getSignal() {

    let pair = document.getElementById("pair").value;

    let res = await fetch(`${API}/signal?pair=${pair}`);
    let data = await res.json();

    document.getElementById("signalBox").innerHTML =
    `<h2>${data.signal}</h2>
     <p>UP: ${data.up_probability}</p>
     <p>DOWN: ${data.down_probability}</p>`;
}
