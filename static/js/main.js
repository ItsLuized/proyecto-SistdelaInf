$('#botonSubmit').on('click', function enviarSolicitud() {
    var nombre = $('#campoNombre').val();
    var email = $('#campoEmail').val();
    var password = $('#campoPassword').val();
    var rol = parseInt($('#campoRol').val());

    var localData = JSON.stringify({
        "nombre": nombre,
        "email": email,
        "contrasena": password,
        "id_cargo": rol
    });
    console.log(nombre + " // " + email + " // " + password + " // " + rol);
    console.log(localData);
    $.ajax({
        url: '/usuario/create',
        type: 'POST',
        dataType: 'json',
        contentType: 'application/json',
        data: localData,
        success: function (data) {
            console.log(data)
        },
        error: function (e) {
            console.log(e)
        }
    });
});

$('#createImperativo').on('click', function () {
    var nombre = $('#campoNombre').val();
    var fecha_inicio = $('#fecha_inicio').val();
    var fecha_fin = $('#fecha_fin').val();
    var id_usuario = parseInt($('#opcionLider').val());

    var localData = JSON.stringify({
        "nombre": nombre,
        "fecha_inicio": fecha_inicio,
        "fecha_fin": fecha_fin,
        "id_usuario": id_usuario
    });

    console.log(localData);

    $.ajax({
        url: '/api/imperativo',
        type: 'POST',
        dataType: 'json',
        contentType: 'application/json',
        data: localData,
        success: function (data) {
            console.log(data)
        },
        error: function (e) {
            console.log(e)
        }
    });

});

$('#editarImperativo').on('click', function () {
    var nombre = $('#campoNombre').val();
    var fecha_inicio = $('#fecha_inicio').val();
    var fecha_fin = $('#fecha_fin').val();
    var id_usuario = parseInt($('#opcionLider').val());
    var id_imperativo = parseInt($('#id_imperativo').val());

    var localData = JSON.stringify({
        "id_imperativo": id_imperativo,
        "nombre": nombre,
        "fecha_inicio": fecha_inicio,
        "fecha_fin": fecha_fin,
        "id_usuario": id_usuario
    });

    console.log(localData);

    $.ajax({
        url: '/masimperativos/' + id_imperativo,
        type: 'PUT',
        dataType: 'json',
        contentType: 'application/json',
        data: localData,
        success: function (data) {
            console.log(data)
        },
        error: function (e) {
            console.log(e)
        }
    });

});


$('#createObjetivo').on('click', function () {
    var nombre = $('#campoNombre').val();
    var completud_por = $('#completud_por').val();
    var id_imperativo = parseInt($('#id_imperativo').val());

    var localData = JSON.stringify({
        "id_imperativo": id_imperativo,
        "nombre": nombre,
        "completud_por": completud_por
    });

    console.log(localData);

    $.ajax({
        url: '/api/' + id_imperativo + '/objetivo',
        type: 'POST',
        dataType: 'json',
        contentType: 'application/json',
        data: localData,
        success: function (data) {
            console.log(data)
        },
        error: function (e) {
            console.log(e)
        }
    });

});