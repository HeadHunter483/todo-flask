$(document).ready(function(){
    $(".task-checkbox").click(function(){
        var elemid = $(this).attr('id').substring(5)
        if ($(this).prop("checked")) {
            $.ajax({
                method: "POST",
                url: "/updateElemDone",
                data: {id: elemid, done: 1}
            }).done(function(data){
                let titleid = 'title'+elemid;
                $('#'+titleid).html("<s>"+$('#'+titleid).text()+"</s>");
            });
        }
        else {
            $.ajax({
                method: "POST",
                url: "/updateElemDone",
                data: {id: elemid, done: 0}
            }).done(function(data){
                let titleid = 'title'+elemid;
                $('#'+titleid).html($('#'+titleid).text());
            });
        }
    });
});