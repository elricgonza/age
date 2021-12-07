// Para visor en asientos/recintos a partir de coordenadas
// -ric
function cargaresp(valor, data) {
    var x = event.keyCode;
    if (x == 27 || x == 9 || 'undefined') {
        if(data==0){
            document.getElementById("ideploc").value=valor;
            $('#iprovincia').html('');
            $('#imunicipio').html('');
            $.getJSON("/get_provespeciales_all", function(datos){
                $("#iprovincia").append('<option></option>');
                $.each(datos, function(index, obj){
                    if(valor==obj[0]){
                        $("#iprovincia").append('<option value="' + obj[1] + '">' + obj[2] + '</option>');    
                    }
                });
            });
        }else if(data==1){
            document.getElementById("iprovloc").value=valor;
            var dp = document.getElementById("idepartamento").value;
            $('#imunicipio').html('');
            $.getJSON("/get_muniespeciales_all", function(datos1){
                $("#imunicipio").append('<option></option>');                
                $.each(datos1, function(index1, obj1){                 
                    if(dp==obj1[0] && valor==obj1[1]){
                        $("#imunicipio").append('<option value="' + obj1[2] + '">' + obj1[3] + '</option>');    
                    }
                });
            });
        }else if(data==2){
            document.getElementById("isecloc").value=valor;
        } 
    };
}
function cargarjuri(valor, data) {
    var x = event.keyCode;
    if (x == 27 || x == 9 || 'undefined') {
        if(data==0){
            document.getElementById("ideploc").value=valor;
            $('#iprovincia').html('');
            $('#imunicipio').html('');
            $("#icircun1").val('');
            $("#iidloc1").val('');
            $('#iasie').html('');
            $('#izonad').html('');
            $.getJSON("/get_provespeciales_all", function(datos){
                $("#iprovincia").append('<option></option>');
                $.each(datos, function(index, obj){
                    if(valor==obj[0]){
                        $("#iprovincia").append('<option value="' + obj[1] + '">' + obj[2] + '</option>');    
                    }
                });
            });
        }else if(data==1){
            document.getElementById("iprovloc").value=valor;
            var dp = document.getElementById("idepartamento").value;
            $('#imunicipio').html('');
            $("#icircun1").val('');
            $("#iidloc1").val('');
            $('#iasie').html('');
            $('#izonad').html('');
            $.getJSON("/get_muniespeciales_all", function(datos1){
                $("#imunicipio").append('<option></option>');                
                $.each(datos1, function(index1, obj1){                 
                    if(dp==obj1[0] && valor==obj1[1]){
                        $("#imunicipio").append('<option value="' + obj1[2] + '">' + obj1[3] + '</option>');    
                    }
                });
            });
        }else if(data==2){
            document.getElementById("isecloc").value=valor;
            var dp = document.getElementById("idepartamento").value;
            var pr = document.getElementById("iprovincia").value;
            var mu = valor;
            $("#icircun1").val('');
            $("#iidloc1").val('');
            $('#iasie').html('');
            $('#izonad').html('');
            $.getJSON("/get_asijuri_all", {
                dp: dp,
                pr: pr,
                mu: mu
            }, function(datos1){
                $("#iasie").append('<option></option>');                
                $.each(datos1, function(index1, obj1){                 
                    $("#iasie").append('<option value="'+obj1[0]+'">'+obj1[1]+'</option>');  
                });
            });
        }else if(data==3){
            var as = document.getElementById("iasie").value;
            document.getElementById('iidloc1').value = as;
            $('#izonad').html('');
            $.getJSON("/get_zondist_all", {
                as: as
            }, function(datos1){
                $("#izonad").append('<option></option>');                
                $.each(datos1, function(index1, obj1){                 
                    $("#izonad").append('<option value="'+obj1[1]+'">'+obj1[2]+'(Circun: '+obj1[3]+')'+'</option>');  
                });
            });
        } 
    };
} 
function cargarjuri_a(valor, data) {
    var x = event.keyCode;
    if (x == 27 || x == 9 || 'undefined') {
        if(data==0){
            document.getElementById("ideploc").value=valor;
            $('#iprovincia').html('');
            $('#imunicipio').html('');
            $('#icircu').html('');
            $('#izonade').html('');
            $.getJSON("/get_provespeciales_all", function(datos){
                $("#iprovincia").append('<option></option>');
                $.each(datos, function(index, obj){
                    if(valor==obj[0]){
                        $("#iprovincia").append('<option value="' + obj[1] + '">' + obj[2] + '</option>');    
                    }
                });
            });
        }else if(data==1){
            document.getElementById("iprovloc").value=valor;
            var dp = document.getElementById("idepartamento").value;
            $('#imunicipio').html('');
            $('#icircu').html('');
            $('#izonade').html('');
            $.getJSON("/get_muniespeciales_all", function(datos1){
                $("#imunicipio").append('<option></option>');                
                $.each(datos1, function(index1, obj1){                 
                    if(dp==obj1[0] && valor==obj1[1]){
                        $("#imunicipio").append('<option value="' + obj1[2] + '">' + obj1[3] + '</option>');    
                    }
                });
            });
        }else if(data==2){
            document.getElementById("isecloc").value=valor;
            var dp = document.getElementById("idepartamento").value;
            var pr = document.getElementById("iprovincia").value;
            var mu = valor;
            $('#icircu').html('');
            $('#izonade').html('');
            $.getJSON("/get_circuns_dps", {
                dp: dp,
                pr: pr,
                mu: mu
            }, function(datos1){
                $("#icircu").append('<option></option>');                
                $.each(datos1, function(index1, obj1){                 
                    $("#icircu").append('<option value="'+obj1[3]+'">'+obj1[3]+'</option>');  
                });
            });
        }else if(data==3){
            var dp = document.getElementById("idepartamento").value;
            var pr = document.getElementById("iprovincia").value;
            var mu = document.getElementById("imunicipio").value;
            var id_loc = document.getElementById("iidloc").value;
            $('#izonade').html('');
            $.getJSON("/get_zonas_dps", {
                dp: dp,
                pr: pr,
                mu: mu,
                id_loc: id_loc
            }, function(datos1){
                $("#izonade").append('<option></option>');                
                $.each(datos1, function(index1, obj1){                 
                    $("#izonade").append('<option value="'+obj1[1]+'">'+obj1[2]+'</option>');  
                });
            });
        } 
    };
}