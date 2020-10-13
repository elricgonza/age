// Para visor en asientos/recintos a partir de coordenadas
// -ric
function cargar(valor, data) {
    var x = event.keyCode;
    if (x == 27 || x == 9 || 'undefined') {
        if(data==0){
            $('#iprovincia').html('');
            $('#imunicipio').html('');
            $.getJSON("/get_provincias_all", function(datos){
                var i=1;
                $("#iprovincia").append('<option></option>');
                $.each(datos, function(index, obj){
                    if(valor==obj[0]){
                        $("#iprovincia").append('<option value="' + i + '">' + obj[1] + '</option>');    
                        i++;
                    }
                });
            });
        }else if(data==1){
            var dp = document.getElementById("idpto").value;
            $('#imunicipio').html('');
            $.getJSON("/get_municipios_all", function(datos1){
                var j=1;
                $("#imunicipio").append('<option></option>');                
                $.each(datos1, function(index1, obj1){                 
                    if(dp==obj1[0] && valor==obj1[1]){
                        $("#imunicipio").append('<option value="' + j + '">' + obj1[2] + '</option>');
                        j++;    
                    }
                });
            });
        } 
    };
} 



