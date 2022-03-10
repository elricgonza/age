// Para visor en asientos/recintos a partir de coordenadas
// -ric
function cargar(valor, data) {
    var x = event.keyCode;
    if (x == 27 || x == 9 || 'undefined') {
        if (data == 0) {
            $('#iprovincia').html('');
            $('#imunicipio').html('');
            $.getJSON("/get_provincias_all", function(datos) {
                var i = 1;
                $("#iprovincia").append('<option></option>');
                $.each(datos, function(index, obj) {
                    if (valor == obj[0]) {
                        $("#iprovincia").append('<option value="' + obj[1] + '">' + obj[2] + '</option>');
                        i++;
                    }
                });
            });
        } else if (data == 1) {
            var dp = document.getElementById("idpto").value;
            $('#imunicipio').html('');
            $.getJSON("/get_municipios_all", function(datos1) {
                var j = 1;
                $("#imunicipio").append('<option></option>');
                $.each(datos1, function(index1, obj1) {
                    if (dp == obj1[0] && valor == obj1[1]) {
                        $("#imunicipio").append('<option value="' + obj1[2] + '">' + obj1[3] + '</option>');
                        j++;
                    }
                });
            });
        } else if (data == 3) {
            var sgrupo = document.getElementById("ipais").value;
            $('#idpto').html('');
            $.getJSON("/get_deptos_prov_all", {
                sgrupo: sgrupo
            }, function(datos3){
                $("#idpto").append('<option></option>');                
                $.each(datos3, function(index3, obj3){       
                    $("#idpto").append('<option value="' + obj3[0] + '">' + obj3[1] + '</option>');
                });
            });
        } else if (data == 4) {
            var sgrupo = document.getElementById("ipais").value;
            $('#idpto').html('');
            $('#iprov').html('');
            $.getJSON("/get_deptos_all", {
                sgrupo: sgrupo
            }, function(datos4){
                $("#idpto").append('<option></option>');                
                $.each(datos4, function(index4, obj4){       
                    $("#idpto").append('<option value="' + obj4[0] + '">' + obj4[1] + '</option>');
                });
            });
        } else if (data == 5) {
            var sgrupo = document.getElementById("idpto").value;
            $('#iprov').html('');
            $.getJSON("/get_provs_all", {
                sgrupo: sgrupo
            }, function(datos5){
                $("#iprov").append('<option></option>');                
                $.each(datos5, function(index5, obj5){       
                    $("#iprov").append('<option value="' + obj5[0] + '">' + obj5[1] + '</option>');
                });
            });
        } else if(data==13){
            var sgrupo = document.getElementById("ipais").value;
            $('#idescNivel').html('');
            $.getJSON("/get_desc_nivel_all", {
                sgrupo: sgrupo
            }, function(datos13){
                $("#idescNivel").append('<option></option>');                
                $.each(datos13, function(index13, obj13){       
                    $("#idescNivel").append('<option value="' + obj13[0] + '">' + obj13[1] + '</option>');
                });
            });
        } else if(data==14){
            var sgrupo = document.getElementById("ipais").value;
            $('#idescNivel').html('');
            $.getJSON("/get_desc_nivel_prov_all", {
                sgrupo: sgrupo
            }, function(datos14){
                $("#idescNivel").append('<option></option>');                
                $.each(datos14, function(index14, obj14){       
                    $("#idescNivel").append('<option value="' + obj14[0] + '">' + obj14[1] + '</option>');
                });
            });
        } else if(data==15){
            var sgrupo = document.getElementById("ipais").value;
            $('#idescNivel').html('');
            $.getJSON("/get_desc_nivel_mun_all", {
                sgrupo: sgrupo
            }, function(datos15){
                $("#idescNivel").append('<option></option>');                
                $.each(datos15, function(index15, obj15){       
                    $("#idescNivel").append('<option value="' + obj15[0] + '">' + obj15[1] + '</option>');
                });
            });
        }
    };
}
