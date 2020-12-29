// Para visor en asientos/recintos a partir de coordenadas
// -ric 
function getgeoreci(event) {
    var x = event.keyCode;
    //alert(x)
    if (x == 27 || x == 9 || 'undefined') {          
        asientosReci($('input[name="deploc"]').val(), $('input[name="provloc"]').val(), $('input[name="secloc"]').val(), $('input[name="circun"]').val());
    };
} 

function getgeoreci1(event) {
    var x = event.keyCode;
    //alert(x)
    if (x == 27 || x == 9 || 'undefined') {          
        asientosReci1($('input[name="deploc"]').val(), $('input[name="provloc"]').val(), $('input[name="secloc"]').val(), $('input[name="circun"]').val());
    };
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
                console.log(datos);
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

function asientoZona(event) {
    var x = event.keyCode;
    //alert(x)
    if (x == 27 || x == 9 || 'undefined') {
            console.log($('input[name="idloc"]').val());
            $.getJSON('/asientoz', {
                azona: $('input[name="idloc"]').val()
            }, function(data) {
                document.getElementById("inomloc").setAttribute("value", data.nomasi)
            });
    };
} 
