
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


$("#cursos").change(() => {
    const disciplinas = $("#disciplinas");
    let html = `<option value="0" disabled selected>Escolha um Curso</option>`;
    $.ajax({
        type: 'GET',
        url: `/api/disciplina/`,
        data: 'curso=' + $('#cursos').val(),
        success: data => {
            data.forEach(disciplina => {
                html += `<option value="${disciplina.cod_disc}">${disciplina.nome_disc}</option>`
            });
            disciplinas.html(html);
            disciplinas.prop('disabled', false);
        }
    })
})



$("#disciplinas").change(() => {
    const curso = $("#cursos option:selected").text();
    const disciplina = $("#disciplinas option:selected").text() 
    const turmas = $("#turmas");
    let html = `<option disabled selected>Turma</option>`;
    $.ajax({
        type: 'GET',
        url: `/api/grade-aulas/`,
        data: 'disciplina=' + $('#disciplinas').val(),
        success: data => {
            data.forEach(turma => {
                html += `<option value="${turma.cod_grade_aulas}">${disciplina} ${turma.periodo} ${curso}</option>`
            });
            turmas.html(html);
            turmas.prop('disabled', false);
        }
    })
})


$('#enviar').click((e) => {
    e.preventDefault();
    const json = {
        "data": $("#data").val(),
        "descricao": $("#descricao").val(),
        "grade_aulas": $("#turmas").val()
    };
    $.ajax({
        type: 'POST',
        url: '/api/aula/',
        dataType: 'json',
        data: JSON.stringify(json), 
        success: function(data) { 
            $('.alert-container').html(
                `<div class="alert alert-success alert-dismissible fade show" role="alert">
                    Aula cadastrada com sucesso! 
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