function buildList(kind) {
    const pageMount = document.getElementById("page-mount");

    const listContainer = document.createElement("div");
    listContainer.className = "experimentsListContainer";

    const ul = document.createElement("ul");

    for (let i = 1; i <= 11; i++) {
        const li = document.createElement("li");
        li.className = "experimentsListItem";
        li.textContent = `${kind}_${i}`;
        li.addEventListener("click", function(){
            openExperiment(li.textContent)
        })
        ul.appendChild(li);
    }

    listContainer.appendChild(ul);

    pageMount.appendChild(listContainer);
}

function openExperiment(exp_id){
    alert(exp_id)
    /*
        TODO
    */
   return;
}