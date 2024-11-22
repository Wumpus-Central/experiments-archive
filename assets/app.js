function buildList(kind) {
    const pageMount = document.getElementById("page-mount");

    const listContainer = document.createElement("div");
    listContainer.className = "experimentsListContainer";

    const ul = document.createElement("ul");

    for (let i = 1; i <= 7; i++) {
        const li = document.createElement("li");
        li.className = "experimentsListItem"
        li.textContent = `Typ ${kind}, id ${i}`;
        ul.appendChild(li);
    }

    listContainer.appendChild(ul);

    pageMount.appendChild(listContainer);
}
