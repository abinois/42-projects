$(document).ready(function(){
$("#new").click(ft_Add);
var index = 0;

$.ajax({
    url: 'select.php',
    datatype: 'JSON',
    success: function(tab){
        var tab2 = $.parseJSON(tab);
        for (n in tab2)
            if (tab2[n])
                ft_Setelem(tab2[n]);
    }
});
    
function ft_Add() {
    var tache = prompt("Ajouter une tache");
    if (tache && tache.trim())
    {
        $.ajax({
            url: 'insert.php',
            type: 'GET',
            data: {id:index, val:tache}
        });
        ft_Setelem(tache);
    }
}

function ft_Del() {
    if (confirm("Ceci à l'air urgent, êtes-vous sûr de vouloir le supprimer?")) {
        $(this).remove();
        $.ajax({
            url: 'delete.php',
            type: 'POST',
            data: {id:$(this).attr('id')}
        });
    }
}
    
function ft_Setelem(data) {
    $("#ft_list").prepend("<div class='todo' id='"+index+"' title='click to delete the task'>"+data+"</div>");
    $("#"+index).click(ft_Del);
    index++;
}
});