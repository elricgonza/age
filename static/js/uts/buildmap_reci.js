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


function getLocMunicipio(event) {
  // Invocado por recinto.html/evento click: get "Asientos"

    var x = event.keyCode;
    var idloc = document.getElementById("ireci_idasiento").value;
    if (x == 27 || x == 9 || 'undefined') {
        if($('input[name="load"]').val()=='True'){ // EDIT
            asiento_reci(idloc, $('input[name="circun"]').val());
        }else{ // NEW
            loadLocMunicipio();
            //loadLocMunicipio($('input[name="deploc"]').val(), $('input[name="provloc"]').val(), $('input[name="secloc"]').val(), $('input[name="tipoCir"]'));
            /*
            $('#iasiento').html('');
            $.getJSON("/get_loc_municipio", { 
                    dep: $('input[name="deploc"]').val(),
                    prov: $('input[name="provloc"]').val(),
                    sec: $('input[name="secloc"]').val(),
                    tipoCir: $('input[name="tipoCir"]'),
                tipoCir: 'uninominal/mixto'
                }, function(datos){
                $("#iasiento").append('<option></option>');
                    $.each(datos, function(index, obj){
                        $("#iasiento").append('<option value=' + obj[3]'>' + obj[4] + '</option>');
                        alert(obj[3] + "---" + obj[4])
                    });
                });
            */
        };
    };
}


function getgeoreci2(event) {
    var x = event.keyCode;
    var idloc = document.getElementById("ireci_idasiento").value;
    if (x == 27 || x == 9 || 'undefined') {
        if($('input[name="load"]').val()=='True'){
            asiento_reci(idloc, $('input[name="circun"]').val());            
        }else{
            asientosReci2($('input[name="deploc"]').val(), $('input[name="provloc"]').val(), $('input[name="secloc"]').val(), $('input[name="circun"]').val());
        };             
    };
}

function getgeoreci4(event) {
    var x = event.keyCode;
    var idloc = document.getElementById("ireci_idasiento").value;
    if (x == 27 || x == 9 || 'undefined') {
        if($('input[name="load"]').val()=='True'){
            asiento_reci(idloc, $('input[name="circun"]').val());            
        }else{
            asientosReci4($('input[name="deploc"]').val(), $('input[name="provloc"]').val(), $('input[name="secloc"]').val(), $('input[name="circun"]').val());
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

/*
// invocado x get asientos (recinto.html)
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
*/

// invocado x get asientos (recinto.html) new recinto - recodificado
// invocado cuando recinto es new 
//function loadLocMunicipio(dep, prov, sec, cir) {
function loadLocMunicipio() {
    var x = event.keyCode;
    if (x == 27 || x == 9 || 'undefined') {
        $('#iasiento').html('');
        $.getJSON("/get_loc_municipio", { 
                dep: $('input[name="deploc"]').val(),
                prov: $('input[name="provloc"]').val(),
                sec: $('input[name="secloc"]').val(),
                tipoCir: $('input[name="tipoCir"]'),
            tipoCir: 'uninominal/mixto'
            }, function(datos){
            $("#iasiento").append('<option></option>');
                $.each(datos, function(index, obj){
                    $("#iasiento").append('<option value="' + cir+':'+obj[3] + '">' + obj[4] + '</option>');
                    alert(obj[3] + "---" + obj[4])
                });
            });
    };
}


function asientosReci2(dep, prov, sec, cir) {
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

function asientosReci4(dep, prov, sec, cir) {
    var x = event.keyCode;
    if (x == 27 || x == 9 || 'undefined') {
        $('#iasiento').html('');
        $.getJSON("/get_asientos_all4", {
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
