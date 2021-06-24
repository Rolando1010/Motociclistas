const nombre = document.querySelector(".nombre").innerText;

const filas = document.querySelectorAll(".fila");

var tomados = document.querySelector(".tomados").innerText.split(",");

if(tomados[0]!=""){
    for(var i=0;i<tomados.length;i++){
        tomados[i] = parseInt(tomados[i]);
        for(var j=0;j<filas[tomados[i]-1].children.length;j++){
            filas[tomados[i]-1].children[j].classList.add("verde");
        }
    }
}

var ocupados = [];

for(var i=0;i<filas.length;i++){
    if(parseInt(filas[i].children[2].innerText)==0 && !tomados.includes(parseInt(filas[i].children[0].innerText))){
        ocupados.push(parseInt(filas[i].children[0].innerText));
        for(var j=0;j<filas[i].children.length;j++){
            filas[i].children[j].classList.add("rojo");
        }
    }
}

for(var i=0;i<filas.length;i++){
    filas[i].addEventListener("click",(evento)=>{
        const fila = evento.path[1];
        const pos = parseInt(fila.children[0].innerText);
        if(!ocupados.includes(pos)){
            if(tomados.includes(pos)){
                for(var j=0;j<fila.children.length;j++){
                    fila.children[j].classList.remove("verde");
                }
                tomados = eliminarElemLista(pos,tomados);
                fila.children[2].innerText = parseInt(fila.children[2].innerText) + 1;
                solicitudMoto(pos,false)
            }else{
                tomados.push(pos);
                for(var j=0;j<fila.children.length;j++){
                    fila.children[j].classList.add("verde");
                }
                fila.children[2].innerText = parseInt(fila.children[2].innerText) - 1;
                solicitudMoto(pos,true)
            }
        }
    });
}

function eliminarElemLista(elem,lista){
    var nuevo = [];
    for(var i=0;i<lista.length;i++){
        if(lista[i]!=elem){
            nuevo.push(elem);
        }
    }
    return nuevo;
}

function solicitudMoto(pos, tomar){
    var solicitud = new XMLHttpRequest();
    solicitud.open('POST', '/'+nombre, true);
    solicitud.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
    solicitud.send("data=" + pos.toString()+"|"+tomar.toString());
}