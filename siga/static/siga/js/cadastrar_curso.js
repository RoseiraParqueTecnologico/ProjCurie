

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
        url: '/api/cursos/cadastrar',
        data: JSON.stringify(json), 
        success: function(data) { 
            $('.alert-container').html(
                `<div class="alert alert-success alert-dismissible fade show" role="alert">
                    ${data.nome} cadastrado com sucesso! Codigo = ${data.codigo}
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