var title_edit_button = '<button class="btn btn-primary" title="редактировать" id="edit-title" onclick="edit_title()"><i class="fas fa-edit"></i></button>';
var title_save_button = '<button class="btn btn-primary" title="сохранить" id="save-title" onclick="save_title()"><i class="fas fa-save"></i></button>';
var content_edit_button = '<button class="btn btn-primary" title="редактировать" id="edit-content" onclick="edit_content()"><i class="fas fa-edit"></i></button>';
var content_save_button = '<button class="btn btn-primary" title="сохранить" id="save-content" onclick="save_content()"><i class="fas fa-save"></i></button>';

function ajax_call() {
    $.ajax({
        method: 'POST',
        url: '/editElem',
        data: {id: data.id, title: data.title, content: data.content, done: data.done}
    });
}

function edit_title() {
    $('#task-title').html("<input type='text' name='title' value='"+data.title+"' style='margin:2px;border-radius:10px;'>");
    $('#edit-title').parent().html(title_save_button);
}

function save_title() {
    title = $("#task-title input").prop('value');
    if (title != "" && title != data.title){
        data.title = title;
    }
    ajax_call();
    $("#task-title").html("<span>"+data.title+"</span>");
    $("#save-title").parent().html(title_edit_button);
}

function edit_content() {
    $('#task-content').html("<input type='text' name='content' value='"+data.content+"' style='margin:2px;border-radius:10px;'>");
    $('#edit-content').parent().html(content_save_button);
}

function save_content() {
    content = $("#task-content input").prop('value');
    if (content != "" && content != data.content){
        data.content = content;
    }
    ajax_call();
    $("#task-content").html("<span>"+data.content+"</span>");
    $("#save-content").parent().html(content_edit_button);
}

$(document).ready(function(){
    $("#edit-done option").click(function(){
        data.done = $("#edit-done option:selected").val();
        ajax_call();
    });

    $("#delete").click(function(){
        $(".modal").show();
    });

    $("#delete-yes").click(function(){
        $.ajax({
            method: 'POST',
            url: '/deleteElem',
            data: {id: data.id}
        }).done(function(){
            $(location).attr('href','/index');
        });
    });

    $("#delete-no").click(function(){
        $(".modal").hide();
    });

    $(".modal").click(function(){
        $(".modal").hide();
    });
});