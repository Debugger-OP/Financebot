const canvas = document.getElementById("waveCanvas");
const ctx = canvas.getContext("2d");
const noise = new SimplexNoise();
let w = window.innerWidth;
let h = window.innerHeight;
canvas.width = w;
canvas.height = h;
ctx.filter = "blur(10px)";

let t = 0;
function draw() {
  ctx.fillStyle = "black";
  ctx.globalAlpha = 0.5;
  ctx.fillRect(0, 0, w, h);
  ctx.lineWidth = 50;

  const colors = ["#38bdf8", "#818cf8", "#c084fc", "#e879f9", "#22d3ee"];

  for (let i = 0; i < 5; i++) {
    ctx.beginPath();
    ctx.strokeStyle = colors[i % colors.length];
    for (let x = 0; x < w; x += 5) {
      const y = noise.noise3D(x / 800, i * 0.3, t) * 100 + h / 2;
      ctx.lineTo(x, y);
    }
    ctx.stroke();
    ctx.closePath();
  }

  t += 0.002;
  requestAnimationFrame(draw);
}
draw();

window.addEventListener("resize", () => {
  w = canvas.width = window.innerWidth;
  h = canvas.height = window.innerHeight;
  ctx.filter = "blur(10px)";
});
