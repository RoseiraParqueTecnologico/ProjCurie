$(document).ready(() => {
    const cursos = $("#cursos");
    let html = cursos.html();
    $.ajax({
        url: '/api/curso',
        success: data => {
            data.forEach(curso => {
                html += `<option value="${curso.id}">${curso.nome}</option>`
            });
            cursos.html(html);
            cursos.prop('disabled', false);
        }
    })
});



$('#enviar').click((e) => {
    e.preventDefault()
    let array = $("#form").serializeArray();
    let json = {};
    array.forEach(c => {
        json[c.name] = c.value || '';
    });
    // console.log(json)
    // console.table(json)

    $.ajax({
        type: 'POST',
        url: '/api/disciplina/',
        dataType: 'json',
        data: JSON.stringify(json), 
        success: function(data) { 
            $('.alert-container').html(
                `<div class="alert alert-success alert-dismissible fade show" role="alert">
                    ${data.nome_disc} cadastrado com sucesso! Codigo = ${data.cod_disc}
                    <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>`
            )
         },
        contentType: "application/json",
        dataType: 'json'
    });
});