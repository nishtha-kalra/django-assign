function DeleteEntry(id) {
    //alert($("input[name=csrfmiddlewaretoken]").val());
    var con = confirm("Are you sure you want to delete entry at " + id + "?");
    if (con) {
        $.post("/polls/delete",
        {
            'csrfmiddlewaretoken':$("input[name=csrfmiddlewaretoken]").val(),
            'id'                : id
        },
        function(data, status){
            var response = jQuery.parseJSON(data);
            if(response.status == true){
                location.reload();
            }
        });
    }
    else {
        alert("Entry not deleted");
    }
}


function EditEntry(id) {
    alert($("input[name=csrfmiddlewaretoken]").val());
    $.post("/polls/edit",
    {
        'csrfmiddlewaretoken':$("input[name=csrfmiddlewaretoken]").val(),
         'id'                : id
    },
    function(data, status){
        var response = jQuery.parseJSON(data);
        if(response.status == true){
                location.reload();
            }
    });
}

/*function EditEntry(id) {
    alert("in js");
    //alert($("input[name=csrfmiddlewaretoken]").val());
    $.post("/polls/delete",
        {
            'csrfmiddlewaretoken':$("input[input[name=csrfmiddlewaretoken]").val(),
            'id'                 : id
        },
        function(data, status) {
            var result = jQuery.parseJSON(data);
            alert(result);
    });
    alert("after post");
}
*/
/*function getDetails(id){
    // sending ajax request got get customer details

    $.get("directory/" + id,
        {},
        function(data, status){
            $("#bodyEditModel").html(data);
    });
}
function ShowEntry(id){
    $('#EditDetails').modal('show');
    getDetails(id);
}*/
