// call new/upd recinto datos complementarios 
// -ric parc/recodif


function getZonasIdloc(idloc) {
    // carga cbo zonas de asiento - recinto.html 
    document.getElementById('iidloc').value = idloc;
    document.getElementById('iidlocreci').value = idloc;
    document.getElementById('idlocDist').value = idloc;

    $('#izonareci').html('');
    $.getJSON("/get_zonas_idloc", {
        idloc: idloc
    }, function(zonas){
        $("#izonareci").append('<option></option>');                
        $.each(zonas, function(index, obj){       
            $("#izonareci").append('<option value="' + obj[1] + '">' + obj[2] +' - '+ obj[4] +'</option>');
        });
    });

    getDistsIdloc();
}

function getDistsIdloc() {
    // carga dists de asiento
    $('#inomdist').html('');
    $.getJSON("/get_dists_idloc", {
        idloc: document.getElementById("iidlocreci").value
    }, function(datos7){
        $("#inomdist").append('<option></option>');                
        $.each(datos7, function(index7, obj7){           
            $("#inomdist").append('<option value="' + obj7[1] + '">' + obj7[3] +'</option>');
        });
    });
}


function getLocMunicipio() {
  // Invocado por recinto.html/evento click: get "Asientos/Zonas" en combo

    var idloc = document.getElementById("ireci_idasiento").value;
    if($('input[name="load"]').val()=='True'){ // EDIT
        getLocNom(idloc);  // reload combo humm
    }else{ // NEW
        loadLocMunicipio();
    };
}


function loadLocMunicipio() {
    // call by (recinto.html) si NEW 
    var x = event.keyCode;
    const inputTipoCir = document.getElementById('itipoCir');
    const paramTipoCir = inputTipoCir.value;
    if (x == 27 || x == 9 || 'undefined') {
        $('#iasiento').html('');
        $.getJSON("/get_loc_municipio", { 
                dep: $('input[name="deploc"]').val(),
                prov: $('input[name="provloc"]').val(),
                sec: $('input[name="secloc"]').val(),
                tipoCir: paramTipoCir
            }, function(datos){
            $("#iasiento").append('<option></option>');
                $.each(datos, function(index, obj){
                    $("#iasiento").append('<option value="' + obj[3] + '">' + obj[4] + '</option>');  
                });
            });
    };
}


function getLocNom(idloc) {
    // call by: recinto.html
    $('#iasiento').html('');
    $.getJSON("/get_loc_nom", {
            idloc: idloc
        }, function(datos){
        $("#iasiento").append('<option></option>');
            $.each(datos, function(index, obj){
                $("#iasiento").append('<option value="' + obj[3] + '">' + obj[4] + '</option>');
            });
        });
}


function loadPueblos() {
    var dep = document.getElementById("ideploc").value;
    $('#ipueblo').html('');
    $.getJSON("/get_pueblos_all", {
        dep: dep
    }, function(datos8){
        $("#ipueblo").append('<option></option>');                
        $.each(datos8, function(index8, obj8){           
            $("#ipueblo").append('<option value="' + obj8[0] + '">' + obj8[1] + '</option>');
        });
    });
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
