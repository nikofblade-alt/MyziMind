from flask import Flask, render_template_string
import os
app = Flask(__name__)
HTML = """
<!DOCTYPE html>
<html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>MIZY MIND</title>
<style>
body{background:#0a0a0a;color:white;font-family:Arial;text-align:center;padding:15px}
.card{background:#1a1a1a;border-radius:15px;padding:15px;margin:10px 0}
button{padding:12px 18px;border-radius:10px;border:none;font-weight:bold;margin:5px;cursor:pointer}
.paire{background:#222;color:white;width:45%}
.paire.active{background:#f5c518;color:black}
.mise{background:#222;color:white}
.mise.active{background:#f5c518;color:black}
#lancer{background:#00c853;color:white;font-size:22px;width:100%;padding:18px;display:none}
#stop{background:#ff1744;color:white;font-size:22px;width:100%;padding:18px;display:none}
.vert{color:#00e676}.rouge{color:#ff5252}
</style></head>
<body>
<h1>🔥 MIZY MIND</h1>
<div class="card">Solde Pocket : <b id="solde">--- $</b><br>Gain: <span class="vert" id="gain">+0$</span> | Perte: <span class="rouge" id="perte">-0$</span></div>
<div class="card"><b>1. Choisis ta Paire</b><br><div id="paires"></div><div id="dir"></div></div>
<div class="card"><b>2. Choisis ta Mise</b><br><div id="mises"></div></div>
<div class="card"><b>3. Nombre de Session</b><br><div id="sessions"></div></div>
<button id="lancer" onclick="lancer()">🚀 LANCER</button>
<button id="stop" onclick="arreter()">🛑 STOP</button>
<div class="card" id="hist"><b>Historique</b><br>Aucun trade</div>
<div class="card"><button onclick="inviter()">👥 Inviter un ami</button></div>
<script>
const paires={"Brent Oil OTC":"BAISSIERE","EUR/USD OTC":"HAUSSIERE","USD/JPY OTC":"HAUSSIERE","GBP/USD OTC":"BAISSIERE"};
let paire=null,mise=null,session=null,trade=0,enCours=false,interval=null,miseActuelle=0,solde=1000;
function render(){
 let h=""; for(let p in paires){ h+=`<button class="paire ${paire===p?'active':''}" onclick="choisirPaire('${p}')">${p}</button>` } document.getElementById("paires").innerHTML=h;
 h=""; [1,1.5,2,2.5,5,10,20,50].forEach(m=>{ h+=`<button class="mise ${mise===m?'active':''}" onclick="choisirMise(${m})">${m}$</button>` }); document.getElementById("mises").innerHTML=h;
 h=""; [3,6,9,12].forEach(s=>{ h+=`<button class="mise ${session===s?'active':''}" onclick="choisirSession(${s})">${s}</button>` }); document.getElementById("sessions").innerHTML=h;
 document.getElementById("dir").innerHTML = paire ? `<br><b>Direction FIXE : ${paires[paire]}</b>` : "";
 document.getElementById("lancer").style.display = (paire&&mise&&session&&!enCours) ? "block":"none";
 document.getElementById("stop").style.display = enCours ? "block":"none";
 document.getElementById("solde").innerText = solde.toFixed(2)+" $";
}
function choisirPaire(p){ if(enCours) return; paire=p; render(); }
function choisirMise(m){ if(enCours) return; mise=m; render(); }
function choisirSession(s){ if(enCours) return; session=s; render(); }
function lancer(){ enCours=true; trade=0; miseActuelle=mise; document.getElementById("hist").innerHTML="<b>Historique</b><br>"; render();
 interval=setInterval(()=>{ trade++; let gagne=Math.random()>0.5; let res=gagne?miseActuelle*0.92:-miseActuelle; solde+=res;
 document.getElementById("hist").innerHTML+=`<div>${trade}. ${paire} - Mise ${miseActuelle}$ : <span class="${gagne?'vert':'rouge'}">${gagne?'+':''}${res.toFixed(2)}$</span></div>`;
 if(gagne){ miseActuelle=mise; } else { miseActuelle=miseActuelle*2; }
 if(trade>=session){ arreter(); }
 render();
 },5000);
}
function arreter(){ clearInterval(interval); enCours=false; render(); alert("STOP - Arret immediat !"); }
function inviter(){ let link="https://t.me/myzimind?start=ref_"+Math.floor(Math.random()*99999); navigator.clipboard.writeText(link); alert("Lien copie : "+link); }
render();
</script></body></html>
"""
@app.route("/")
def home():
    return render_template_string(HTML)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
