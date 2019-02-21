


$.getJSON( "/api/cursos/get", function( cursos ) {
    let s = ''
    cursos.forEach(curso => {
        s += `<tr>
                <td>${curso.codigo}</td>
                <td>${curso.nome}</td>
                <td>${curso.desc}</td>
                <td>${curso.link_plano_pedagogico}</td>
                `
        let body = $('#todosCursos>tbody');
        body.html(s)
    });

  let k = `</tbody>
    </table>`
  });