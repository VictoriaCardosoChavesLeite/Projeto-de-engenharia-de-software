const jsonData = require('database.json'); 
console.log(jsonData);

function listaTabela() {
    let tbody = document.getElementById("tbody");
    tbody.innerText='';

    for(let i = 0;i<jsonData.Livros.length;i++){
       let tr = tbody.insertRow();

       let td_Titulo = tr.insertCell();
       let td_Autor = tr.insertCell();
       let td_Editora = tr.insertCell();
       let td_Estoque = tr.insertCell();

       td_Titulo.innerText = jsonData.Livros[i].Titulo;
       td_Autor.innerText = jsonData.Livros[i].Autor;
       td_Editora.innerText = jsonData.Livros[i].Editora;
       td_Estoque.innerText = jsonData.Livros[i].Estoque;

    }

    return td_Titulo,td_Autor,td_Editora,td_Estoque;
}

listaTabela();