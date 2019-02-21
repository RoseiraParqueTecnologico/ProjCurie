

$('#enviar').click((e) => {
    e.preventDefault()
    let array = $("#form").serializeArray();
    let json = {};
    array.forEach(c => {
        json[c.name] = c.value || '';
    });

    $.ajax({
        type: 'POST',
        url: '/api/alunos/cadastrar',
        data: JSON.stringify(json), 
        success: function(response) {
            if(response.status == 'success') {
                $('.alert-container').html(
                    `<div class="alert alert-success alert-dismissible fade show" role="alert">
                        ${response.data.nome} cadastrado com sucesso!
                        <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>`
                )
            }
        },
        error: (response) => {
            console.log(response.responseJSON);
                $('.alert-container').html(
                    `<div class="alert alert-danger alert-dismissible fade show" role="alert">
                        ${response.responseJSON.msg}
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
