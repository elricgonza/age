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



