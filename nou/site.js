(function(){
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  /* aparitie la scroll */
  var io = new IntersectionObserver(function(es){
    es.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('vis'); io.unobserve(e.target); } });
  },{threshold:.15, rootMargin:'0px 0px -40px 0px'});
  document.querySelectorAll('.rv,#steps').forEach(function(el){ reduce ? el.classList.add('vis') : io.observe(el); });

  /* cifrele numara pana la valoare */
  var ioN = new IntersectionObserver(function(es){
    es.forEach(function(e){
      if(!e.isIntersecting) return; ioN.unobserve(e.target);
      var el=e.target, t=+el.dataset.n, suf=el.dataset.suf||'', t0=null;
      if(reduce){ el.textContent=t+suf; return; }
      function f(ts){ if(!t0) t0=ts; var p=Math.min((ts-t0)/1300,1); el.textContent=Math.round(t*(1-Math.pow(1-p,3)))+suf; if(p<1) requestAnimationFrame(f); }
      requestAnimationFrame(f);
    });
  },{threshold:.6});
  document.querySelectorAll('[data-n]').forEach(function(el){ ioN.observe(el); });

  /* meniul de limbi */
  var lang=document.getElementById('lang'), lb=lang.querySelector('button');
  lb.addEventListener('click',function(e){ e.stopPropagation(); var o=lang.classList.toggle('open'); lb.setAttribute('aria-expanded',o); });
  document.addEventListener('click',function(){ lang.classList.remove('open'); lb.setAttribute('aria-expanded',false); });

  /* meniul mobil se inchide dupa click pe link */
  document.querySelectorAll('nav.main a').forEach(function(a){ a.addEventListener('click',function(){ document.getElementById('hd').classList.remove('open'); }); });
})();

/* Calculator de salariu (doar pe pagina de candidati) */
(function(){
  var ore=document.getElementById('ore'); if(!ore) return;
  var rate=15;
  function netGermania(brutLunar){
    var brutAn=brutLunar*12, sociale=brutAn*0.2145;
    var zvE=Math.max(0,brutAn-sociale-1230-36), est=0, G=12096;
    if(zvE>G){
      if(zvE<=17443){ var y=(zvE-G)/10000; est=(932.30*y+1400)*y; }
      else if(zvE<=68480){ var z=(zvE-17443)/10000; est=(176.64*z+2397)*z+1015.13; }
      else if(zvE<=277825){ est=0.42*zvE-10911.92; }
      else { est=0.45*zvE-19246.67; }
    }
    return Math.round((brutAn-sociale-est)/12);
  }
  function eur(v){ return Math.round(v).toLocaleString('de-DE')+' €'; }
  function calc(){
    var h=+ore.value, b=h*rate;
    document.getElementById('oreV').textContent=h;
    document.getElementById('brut').textContent=eur(b);
    document.getElementById('net').textContent='≈ '+eur(netGermania(b));
  }
  document.querySelectorAll('#rates button').forEach(function(bt){
    bt.addEventListener('click',function(){
      document.querySelectorAll('#rates button').forEach(function(x){ x.classList.remove('on'); });
      bt.classList.add('on'); rate=+bt.dataset.r; calc();
    });
  });
  ore.addEventListener('input',calc); calc();
})();

/* Butoanele "Aplica pentru ..." preselecteaza domeniul in formular */
document.querySelectorAll('[data-dom]').forEach(function(a){
  a.addEventListener('click',function(){ var s=document.getElementById('c-dom'); if(s) s.value=a.dataset.dom; });
});
