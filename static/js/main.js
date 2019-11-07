$('#botonSubmit').on('click', function enviarSolicitud() {
    var nombre = $('#campoNombre').val();
    var email = $('#campoEmail').val();
    var password = $('#campoPassword').val();
    var rol = $('#campoRol').val();

    var localData = JSON.stringify({
        "nombre": nombre,
        "email": email,
        "contrasena": password,
        "id_cargo": 1,
        "estado": "ACTIVO"
    });
    console.log(nombre + " // " + email + " // " + password + " // " + rol);
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