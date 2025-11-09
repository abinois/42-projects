var bouton = document.getElementById("new");
bouton.addEventListener("click", ft_Add);
var index = 0;

function ft_Cookie() {
    if (document.cookie)
    {
        var cookies = document.cookie.split(';');
        var tab = [];
        for (i in cookies)
        {
            var cooky = cookies[i].trim(); 
            var eq = cooky.indexOf("=");
            tab.push(cooky.substr(eq + 1));
            var key = eq > 1 ? cooky.substr(0, eq) : cooky[0];
            document.cookie = key + "=; expires=Thu, 01 Jan 1970 00:00:00 GMT";
        }
        for (n in tab)
            ft_Setelem(tab[n]);
    }
}

function ft_Add() {
    var tache = prompt("Ajouter une tache");
    if (tache && tache.trim())
        ft_Setelem(tache);
}

function ft_Del() {
    if (confirm("Ceci à l'air urgent, êtes-vous sûr de vouloir le supprimer?"))
    {
        this.remove();
        document.cookie = this.id + "=; expires=Thu, 01 Jan 1970 00:00:00 GMT";
    }
}

function ft_Setelem(data) {
    var date = new Date();
    date.setTime(date.getTime() + (1000*1*60*60));
    var end = "; expires=" + date.toUTCString();
    document.cookie = index + "=" + data + end;
    var node = document.createElement("div");
    node.innerHTML = data;
    node.setAttribute("class", "todo");
    node.setAttribute("id", index++);
    node.setAttribute("title", "click to delete the task");
    node.addEventListener("click", ft_Del);
    var grosse_list = document.getElementById("ft_list");
    grosse_list.insertBefore(node, grosse_list.firstChild);
}