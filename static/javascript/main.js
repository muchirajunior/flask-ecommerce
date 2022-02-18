function handleMenu(operation){
    var nav=document.getElementById('modal');
    nav.style.display=operation;       
}

async function onLoad(){
  await setTimeout(()=>console.log("print to console"),3000)
  var loader=document.getElementById('loading');
  loader.style.display="none";
}