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
                        $("#idpto").append('<option value="' + obj2[0] + '">' + obj2[1] + '</option>');
                        j++;    
                    }
                });
            });
        }else if(data==5){
            var ia = document.getElementById("iasiento").value;
            var cir = ia.split(':');
            document.getElementById('iidloc').value = cir[1];
            document.getElementById('iidlocreci').value = cir[1];
            document.getElementById('inrodist').value = cir[0];
            document.getElementById('iidlocreci1').value = cir[1];
            document.getElementById('inrodist1').value = cir[0];
            $('#izonareci').html('');
            $.getJSON("/get_zonas_all1", {
                idloc: cir[1],
                circun: cir[0]
            }, function(datos5){
                $("#izonareci").append('<option></option>');                
                $.each(datos5, function(index5, obj5){       
                    $("#izonareci").append('<option value="' + obj5[1] + '">' + obj5[2] +' - '+ obj5[3] + '('+ 'Cir ' + cir[0] +')'+'</option>');
                });
            });
            $('#inomdist').html('');
            $.getJSON("/get_distritos_all", {
                circun: cir[0]
            }, function(datos6){
                $("#inomdist").append('<option></option>');                
                $.each(datos6, function(index6, obj6){           
                    $("#inomdist").append('<option value="' + obj6[1] + '">' + obj6[3] + '('+ 'Cir ' + obj6[2] +')'+'</option>');
                });
            });
        }else if(data==7){
            var circun = document.getElementById("inrodist").value;
            var idlocreci = document.getElementById("iidlocreci").value;
            $('#inomdist').html('');
            $.getJSON("/get_distritos_all", {
                circun: circun,
                idlocreci: idlocreci
            }, function(datos7){
                $("#inomdist").append('<option></option>');                
                $.each(datos7, function(index7, obj7){           
                    $("#inomdist").append('<option value="' + obj7[1] + '">' + obj7[1] +' - '+ obj7[3] +'('+ 'Cir ' + obj7[2] +')'+'</option>');
                });
            });
        }else if(data==8){
            var dep = document.getElementById("ideploc").value;
            $('#ipueblo').html('');
            $.getJSON("/get_pueblos_all", {
                dep: dep
            }, function(datos8){
                console.log(datos8);
                $("#ipueblo").append('<option></option>');                
                $.each(datos8, function(index8, obj8){           
                    $("#ipueblo").append('<option value="' + obj8[0] + '">' + obj8[1] + '</option>');
                });
            });
        }else if(data==9){
            var idloc = document.getElementById("iidloc").value;
            $('#inomdist').html('');
            $.getJSON("/get_distritos_all1", {
                idloc: idloc
            }, function(datos9){
                $("#inomdist").append('<option></option>');                
                $.each(datos9, function(index9, obj9){           
                    $("#inomdist").append('<option value="' + obj9[1] + ':' + obj9[2] + '">' + obj9[1] +' - '+ obj9[3] +'('+ 'Cir ' + obj9[2] +')'+'</option>');
                });
            });
        }else if(data==10){
            var circundist = document.form.circundist.value;
            var circundist1 = 0;
            var idloc = document.getElementById("iidloc").value;
            var dist = document.getElementById("inomdist").value;
            var cirs = dist.split(':');
            var recintos='Los siguientes Recintos, cambiaran de Circuns:\n';
            $.getJSON("/get_circundist", {
                idloc: idloc,
                circd: cirs[1]
            }, function(datos10){                
                $.each(datos10, function(index10, obj10){           
                        recintos=recintos+obj10[1]+'; ';
                        circundist1 = obj10[0];
                });
                if(circundist!=circundist1 && circundist!=''){
                    alert(recintos);
                }
            });
        } 
    };
} 



