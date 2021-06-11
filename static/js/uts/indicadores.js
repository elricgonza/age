/*function listado_indi() {
    var idloc=$('input[name="idloc"]').val();
    $.getJSON("/asiento_ind", {
        idloc: idloc
    }, function(datos){    
        $('#tabla_indi tbody').html("");            
        $.each(datos, function(index, obj){
            fila = '<tr>';
            fila += '<td>' + (index+1) + '</td>';
            fila += '<td>' + obj[1] + '</td>';
            fila += '<td>' + obj[2] + '</td>';
            fila += '<td>' + obj[3] + '</td>';
            fila += '<td><button class="btn btn-primary btn-sm btnEditar"><span class="fas fa-edit"></span></button></td>';
            fila += '<td><button class="btn btn-danger btn-sm btnBorrar"><i class="far fa-trash-alt"></i></button></td>';
            fila += '</tr>';
            $('#tabla_indi tbody').append(fila);
        });
    });
}

$(document).ready(function(){
    listado_indi();
});*/

function cargar(valor, data) {
    var x = event.keyCode;
    if (x == 27 || x == 9 || 'undefined') {
        if(data==0){
            var cate_id = document.getElementById("icategoria").value;
            $('#isubcategoria').html('');
            $.getJSON("/get_subcategorias_all", {
                cate_id: cate_id
            }, function(datos){
                $("#isubcategoria").append('<option></option>');                
                $.each(datos, function(index, obj){           
                    $("#isubcategoria").append('<option value="' + obj[0] + '">'+ obj[1] +'</option>');
                });
            });
        }
    }
}


function cargar2(cate_id, subcate_id) {
    $('#isubcategoria').html('');
    $.getJSON("/get_subcategorias_all", {
        cate_id: cate_id
    }, function(datos){                
        $.each(datos, function(index, obj){
            if(subcate_id == obj[0]){
                $("#isubcategoria").append('<option value="' + obj[0] + '" selected>'+ obj[1] +'</option>');
            }else{
                $("#isubcategoria").append('<option value="' + obj[0] + '">'+ obj[1] +'</option>');    
            }           
        });
    });
}
