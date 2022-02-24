// Para visor en asientos/recintos a partir de coordenadas
// -ric 
function getgeoreci(event) {
    var x = event.keyCode;
    var idloc = document.getElementById("ireci_idasiento").value;
    if (x == 27 || x == 9 || 'undefined') {
        if($('input[name="load"]').val()=='True'){
            asiento_reci(idloc, $('input[name="circun"]').val());            
        }else{
            asientosReci($('input[name="deploc"]').val(), $('input[name="provloc"]').val(), $('input[name="secloc"]').val(), $('input[name="circun"]').val());
        };             
    };
} 

function getgeoreci1(event) {
    var x = event.keyCode;
    var idloc = document.getElementById("ireci_idasiento").value;
    if (x == 27 || x == 9 || 'undefined') {
        if($('input[name="load"]').val()=='True'){
            asiento_reci(idloc, $('input[name="circun"]').val());            
        }else{
            asientosReci1($('input[name="deploc"]').val(), $('input[name="provloc"]').val(), $('input[name="secloc"]').val(), $('input[name="circun"]').val());
        };             
    };
}

function asiento_reci(idloc, cir) {
    $('#iasiento').html('');
    $.getJSON("/get_asiento_one", {
            idloc: idloc
        }, function(datos){
        $("#iasiento").append('<option></option>');
            $.each(datos, function(index, obj){
                $("#iasiento").append('<option value="' + cir+':'+obj[3] + '">' + obj[4] + '</option>');
            });
        });
}

function asientosReci(dep, prov, sec, cir) {
    var x = event.keyCode;
    if (x == 27 || x == 9 || 'undefined') {
        $('#iasiento').html('');
        $.getJSON("/get_asientos_all1", {
                dpto: $('input[name="deploc"]').val(),
                provi: $('input[name="provloc"]').val(),
                secci: $('input[name="secloc"]').val()
            }, function(datos){
            $("#iasiento").append('<option></option>');
                $.each(datos, function(index, obj){
                    $("#iasiento").append('<option value="' + cir+':'+obj[3] + '">' + obj[4] + '</option>');
                });
            });
    };
}

function asientosReci1(dep, prov, sec, cir) {
    var x = event.keyCode;
    if (x == 27 || x == 9 || 'undefined') {
        $('#iasiento').html('');
        $.getJSON("/get_asientos_all2", {
                dpto: $('input[name="deploc"]').val(),
                provi: $('input[name="provloc"]').val(),
                secci: $('input[name="secloc"]').val()
            }, function(datos){
            $("#iasiento").append('<option></option>');
                $.each(datos, function(index, obj){
                    $("#iasiento").append('<option value="' + cir+':'+obj[3] + '">' + obj[4] + '</option>');
                });
            });
    };
}

function asientosReci_ext(event) {
    var x = event.keyCode;
    var pais = document.getElementById("ipais").value;
    var dpto = document.getElementById("idpto").value;
    var provi = document.getElementById("iprovincia").value;
    var secci = document.getElementById("imunicipio").value;
    if (x == 27 || x == 9 || 'undefined') {
        $('#iasiento').html('');
        $.getJSON("/get_asientos_all3", {
                pais: pais,
                dpto: dpto,
                provi: provi,
                secci: secci
            }, function(datos){
            $("#iasiento").append('<option></option>');
                $.each(datos, function(index, obj){
                    $("#iasiento").append('<option value="'+obj[4] + '">' + obj[5] + '</option>');
                });
            });
    };
}

function asientoZona(event) {
    var x = event.keyCode;
    //alert(x)
    if (x == 27 || x == 9 || 'undefined') {
            $.getJSON('/asientoz', {
                azona: $('input[name="idloc"]').val()
            }, function(data) {
                document.getElementById("inomloc").setAttribute("value", data.nomasi)
            });
    };
} 
