let count = 1;
$(document).ready(() => {
    $.ajax({
        type: 'GET',
        url: '/api/cursos/get/',
        success: function(data) { 
            let html = $('#curso').html();
            data.forEach(curso => {
                html += `<option value="${curso.codigo}">${curso.nome}</option>`
            });
            $('#curso').html(html)
            },
        contentType: "application/json",
        dataType: 'json'
    });
});

$('#add-pre-req').click(() => {
    let clone = $('.pre-req-1').clone();
    // let clone = $('.pre-req').clone();
    clone.find('pre-requisito-1').first().attr('id', `pre-requisito-${++count}`);
    clone.removeClass('pre-req-1').addClass(`pre-req-${count}`);
    clone.children().attr('name', `pre-requisito-${count}`);
    clone.children().attr('id', `pre-requisito-${count}`);
    clone.appendTo('#pre-requisitos');
})

$('#curso').change(() => {
    $.ajax({
        type: 'GET',
        url: `/api/disciplinas/listar/curso/${$('#curso').val()}`,
        success: function(data) {
            let htmlDisciplina = $('#disciplina').html();
            let htmlPreRequisitos = $('#pre-requisito-1').html();
            data.data.forEach(disciplina => {
                htmlDisciplina += `<option value="${disciplina.codDisc}">${disciplina.nomeDisc}</option>`
                htmlPreRequisitos += `<option value="${disciplina.codDisc}">${disciplina.nomeDisc}</option>`
            });
            $('#disciplina').html(htmlDisciplina);
            $("#disciplina").prop('disabled', false);
            $('#pre-requisito-1').html(htmlPreRequisitos);
            $("#pre-requisito-1").prop('disabled', false);
            // $('#pre-requisito').html(htmlPreRequisitos);
            // $("#pre-requisito").prop('disabled', false);
            $("#add-pre-req").prop('disabled', false);
            },
        contentType: "application/json",
        dataType: 'json'
    });
});



$('#enviar').click((e) => {
    e.preventDefault()
    // let array = $("#form").serializeArray();
    // let json = {};
    // array.forEach(c => {
    //     json[c.name] = c.value || '';
    // });
    // console.log(json)
    // console.table(json)

    let preReqsSelects = $('.pre-requisito');
    let preReqs = [];
    preReqsSelects.each((index, value)=> {
        preReqs.push($(value).val());
     });

    let json = {
        "cod-disciplina": $('#disciplina').val(),
        "pre-requisitos": [... new Set(preReqs)]
    }

    // console.log(json);
    $.ajax({
        type: 'POST',
        url: '/api/disciplinas/cadastrar/pre-requisitos',
        data: JSON.stringify(json), 
        success: function(data) { 
            $('.alert-container').html(
                `<div class="alert alert-success alert-dismissible fade show" role="alert">
                    Pre Requisitos Cadastrados com sucesso
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



{
    "cpf": "123",
    "nome": "jose",
    "endereco": "nao te interessa",
    "dt_nasc": "2018-02-20",
    "email_institucional": "seu@email.com",
    "senha": "serio?",
    "ra": "1234",
}