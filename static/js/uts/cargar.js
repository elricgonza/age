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
                        console.log(obj[0]+', '+obj[2]);
                        $("#iprovincia").append('<option value="' + obj[1] + '">' + obj[2] + '</option>');    
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
                        $("#imunicipio").append('<option value="' + obj1[2] + '">' + obj1[3] + '</option>');
                        j++;    
                    }
                });
            });
        }else if(data==2){
            var pa = document.getElementById("ipais").value;
            $('#idpto').html('');
            $('#iprovincia').html('');
            $('#imunicipio').html('');
            $.getJSON("/get_departamentos_all", function(datos2){
                var j=1;
                $("#idpto").append('<option></option>');                
                $.each(datos2, function(index2, obj2){           
                    if(pa==obj2[2]){
                        console.log(obj2[0]+', '+obj2[2]);
                        $("#idpto").append('<option value="' + obj2[0] + '">' + obj2[1] + '</option>');
                        j++;    
                    }
                });
            });
        }else if(data==5){
            var ia = document.getElementById("iasiento").value;
            var cir = ia.split(':');
            console.log(cir[0]+', '+cir[1]);
            document.getElementById('iidloc').value = cir[1];
            document.getElementById('iidlocreci').value = cir[1];
            document.getElementById('inrodist').value = cir[0];
            $('#izonareci').html('');
            $.getJSON("/get_zonas_all", function(datos5){
                $("#izonareci").append('<option></option>');                
                $.each(datos5, function(index5, obj5){           
                    if(cir[0]==obj5[3] && cir[1]==obj5[0]){
                        $("#izonareci").append('<option value="' + obj5[1] + '">' + obj5[2] + '('+ 'Dist ' + cir[0] +')'+'</option>');
                    }
                });
            });
        } 
    };
} 



