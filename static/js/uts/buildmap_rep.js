// Para visor en asientos/recintos a partir de coordenadas
// -ric
function getgeoall(event) {
    var map;
    var Markers = {};
    var infowindow;
    var x = event.keyCode;
    var dpto = document.getElementById("idpto");
    var provincia = document.getElementById("iprovincia");
    var municipio = document.getElementById("imunicipio");
    var estado = document.getElementById("iestado");
    var dp = document.getElementById("idpto").value;
    var pr = document.getElementById("iprovincia").value;
    var mu = document.getElementById("imunicipio").value;
    var lo = document.getElementById("ilocalidad").value;
    var es = document.getElementById("iestado").value;
    var ci1 = document.getElementById("icir1").checked;
    var ci2 = document.getElementById("icir2").checked;
    var ci3 = document.getElementById("icir3").checked;
    var fi = document.getElementById("iinicio").value;
    var ff = document.getElementById("ifinal").value;
    var j=1;
    if (x == 27 || x == 9 || 'undefined') {
            $.getJSON("/get_geo_all", function(datos){
                var origin = new google.maps.LatLng(datos[0][8], datos[0][9]);
                function initialize(datos) {
                    var mapOptions = {
                      zoom: 6,
                      center: origin,
                      mapTypeId: google.maps.MapTypeId.TERRAIN
                    };
                    map = new google.maps.Map(document.getElementById('map'), mapOptions);
                    infowindow = new google.maps.InfoWindow();
                    for(i=0; i<datos.length; i++) {
                        if(document.getElementById("ilocalidad").value != ""){
                            if(lo==datos[i][7]){
                                var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                var marker = new google.maps.Marker({
                                    position: position,
                                    map: map,
                                    icon: 'static/iconos/IconoGoogle.png',
                                });
                                google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                    return function() {
                                        infowindow.setContent(
                                            '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                '<TR>'+
                                                     '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                     +'<div align="center">'
                                                        +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                     +'</div>'
                                                     +'</td>'+
                                                '</TR>'+
                                            '</TABLE>'
                                        );
                                        infowindow.setOptions({maxWidth: 200});
                                        infowindow.open(map, marker);
                                    }
                                }) (marker, i));
                                Markers[datos[i][7]] = marker;
                            }
                        }else{
                            if(dpto.options[dpto.selectedIndex].innerText != ""){
                                if(provincia.options[provincia.selectedIndex].innerText != ""){
                                    if(municipio.options[municipio.selectedIndex].innerText != ""){
                                        if(ci1 && ci2 && ci3){
                                            if(estado.options[estado.selectedIndex].innerText != ""){
                                                if(fi != "" && ff != ""){
                                                    if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && (datos[i][12]=="Uninominal" || datos[i][12]=="Especial" || datos[i][12]=="Uninominal/Especial") && es==datos[i][10] && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }else{
                                                    if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && (datos[i][12]=="Uninominal" || datos[i][12]=="Especial" || datos[i][12]=="Uninominal/Especial") && es==datos[i][10]){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }
                                            }else{
                                                if(fi != "" && ff != ""){
                                                    if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && (datos[i][12]=="Uninominal" || datos[i][12]=="Especial" || datos[i][12]=="Uninominal/Especial") && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }else{
                                                    if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && (datos[i][12]=="Uninominal" || datos[i][12]=="Especial" || datos[i][12]=="Uninominal/Especial")){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }
                                            }
                                        }
                                        if(ci1 && ci2 && ci3 == false){
                                            document.getElementsByName("cir3").value = 0;
                                            if(estado.options[estado.selectedIndex].innerText != ""){
                                                if(fi != "" && ff != ""){
                                                    if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && (datos[i][12]=="Uninominal" || datos[i][12]=="Especial") && es==datos[i][10] && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }else{
                                                    if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && (datos[i][12]=="Uninominal" || datos[i][12]=="Especial") && es==datos[i][10]){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }
                                            }else{
                                                if(fi != "" && ff != ""){
                                                    if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && (datos[i][12]=="Uninominal" || datos[i][12]=="Especial") && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }else{
                                                    if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && (datos[i][12]=="Uninominal" || datos[i][12]=="Especial")){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }
                                            }
                                        }
                                        if(ci1 && ci2 == false && ci3){
                                            if(estado.options[estado.selectedIndex].innerText != ""){
                                                if(fi != "" && ff != ""){
                                                    if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && (datos[i][12]=="Uninominal" || datos[i][12]=="Uninominal/Especial") && es==datos[i][10] && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }else{
                                                    if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && (datos[i][12]=="Uninominal" || datos[i][12]=="Uninominal/Especial") && es==datos[i][10]){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }
                                            }else{
                                                if(fi != "" && ff != ""){
                                                    if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && (datos[i][12]=="Uninominal" || datos[i][12]=="Uninominal/Especial") && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }else{
                                                    if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && (datos[i][12]=="Uninominal" || datos[i][12]=="Uninominal/Especial")){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }
                                            }
                                        }
                                        if(ci1 == false && ci2 && ci3){
                                            if(estado.options[estado.selectedIndex].innerText != ""){
                                                if(fi != "" && ff != ""){
                                                    if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && (datos[i][12]=="Especial" || datos[i][12]=="Uninominal/Especial") && es==datos[i][10] && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }else{
                                                    if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && (datos[i][12]=="Especial" || datos[i][12]=="Uninominal/Especial") && es==datos[i][10]){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }
                                            }else{
                                                if(fi != "" && ff != ""){
                                                    if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && (datos[i][12]=="Especial" || datos[i][12]=="Uninominal/Especial") && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }else{
                                                    if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && (datos[i][12]=="Especial" || datos[i][12]=="Uninominal/Especial")){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }
                                            }
                                        }
                                        if(ci1 && ci2 == false && ci3 == false){
                                            if(estado.options[estado.selectedIndex].innerText != ""){
                                                if(fi != "" && ff != ""){
                                                    if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && (datos[i][12]=="Uninominal") && es==datos[i][10] && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }else{
                                                    if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && (datos[i][12]=="Uninominal") && es==datos[i][10]){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }
                                            }else{
                                                if(fi != "" && ff != ""){
                                                    if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && (datos[i][12]=="Uninominal") && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }else{
                                                    if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && (datos[i][12]=="Uninominal")){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }
                                            }
                                        }
                                        if(ci1 == false && ci2 && ci3 == false){
                                            if(estado.options[estado.selectedIndex].innerText != ""){
                                                if(fi != "" && ff != ""){
                                                    if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && (datos[i][12]=="Especial") && es==datos[i][10] && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }else{
                                                    if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && (datos[i][12]=="Especial") && es==datos[i][10]){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }
                                            }else{
                                                if(fi != "" && ff != ""){
                                                    if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && (datos[i][12]=="Especial") && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }else{
                                                    if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && (datos[i][12]=="Especial")){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }
                                            }
                                        }
                                        if(ci1 == false && ci2 == false && ci3){
                                            if(estado.options[estado.selectedIndex].innerText != ""){
                                                if(fi != "" && ff != ""){
                                                    if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && (datos[i][12]=="Uninominal/Especial") && es==datos[i][10] && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }else{
                                                    if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && (datos[i][12]=="Uninominal/Especial") && es==datos[i][10]){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }
                                            }else{
                                                if(fi != "" && ff != ""){
                                                    if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && (datos[i][12]=="Uninominal/Especial") && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }else{
                                                    if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && (datos[i][12]=="Uninominal/Especial")){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }
                                            }
                                        }
                                        if(ci1 == false && ci2 == false && ci3 == false){
                                            if(estado.options[estado.selectedIndex].innerText != ""){
                                                if(fi != "" && ff != ""){
                                                    if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && es==datos[i][10] && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }else{
                                                    if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && es==datos[i][10]){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }
                                            }else{
                                                if(fi != "" && ff != ""){
                                                    if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }else{
                                                    if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5]){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }
                                            }
                                        }    
                                    }else{ 
                                        if(ci1 && ci2 && ci3){
                                            if(estado.options[estado.selectedIndex].innerText != ""){
                                                if(fi != "" && ff != ""){
                                                    if(dp==datos[i][1] && pr==datos[i][3] && (datos[i][12]=="Uninominal" || datos[i][12]=="Especial" || datos[i][12]=="Uninominal/Especial") && es==datos[i][10] && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }else{
                                                    if(dp==datos[i][1] && pr==datos[i][3] && (datos[i][12]=="Uninominal" || datos[i][12]=="Especial" || datos[i][12]=="Uninominal/Especial") && es==datos[i][10]){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }
                                            }else{
                                                if(fi != "" && ff != ""){
                                                    if(dp==datos[i][1] && pr==datos[i][3] && (datos[i][12]=="Uninominal" || datos[i][12]=="Especial" || datos[i][12]=="Uninominal/Especial") && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }else{
                                                    if(dp==datos[i][1] && pr==datos[i][3] && (datos[i][12]=="Uninominal" || datos[i][12]=="Especial" || datos[i][12]=="Uninominal/Especial")){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }
                                            }
                                        }
                                        if(ci1 && ci2 && ci3 == false){
                                            if(estado.options[estado.selectedIndex].innerText != ""){
                                                if(fi != "" && ff != ""){
                                                    if(dp==datos[i][1] && pr==datos[i][3] && (datos[i][12]=="Uninominal" || datos[i][12]=="Especial") && es==datos[i][10] && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }else{
                                                    if(dp==datos[i][1] && pr==datos[i][3] && (datos[i][12]=="Uninominal" || datos[i][12]=="Especial") && es==datos[i][10]){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }
                                            }else{
                                                if(fi != "" && ff != ""){
                                                    if(dp==datos[i][1] && pr==datos[i][3] && (datos[i][12]=="Uninominal" || datos[i][12]=="Especial") && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }else{
                                                    if(dp==datos[i][1] && pr==datos[i][3] && (datos[i][12]=="Uninominal" || datos[i][12]=="Especial")){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }
                                            }
                                        }
                                        if(ci1 && ci2 == false && ci3){
                                            if(estado.options[estado.selectedIndex].innerText != ""){
                                                if(fi != "" && ff != ""){
                                                    if(dp==datos[i][1] && pr==datos[i][3] && (datos[i][12]=="Uninominal" || datos[i][12]=="Uninominal/Especial") && es==datos[i][10] && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }else{
                                                    if(dp==datos[i][1] && pr==datos[i][3] && (datos[i][12]=="Uninominal" || datos[i][12]=="Uninominal/Especial") && es==datos[i][10]){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }
                                            }else{
                                                if(fi != "" && ff != ""){
                                                    if(dp==datos[i][1] && pr==datos[i][3] && (datos[i][12]=="Uninominal" || datos[i][12]=="Uninominal/Especial") && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }else{
                                                    if(dp==datos[i][1] && pr==datos[i][3] && (datos[i][12]=="Uninominal" || datos[i][12]=="Uninominal/Especial")){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }
                                            }
                                        }
                                        if(ci1 == false && ci2 && ci3){
                                            if(estado.options[estado.selectedIndex].innerText != ""){
                                                if(fi != "" && ff != ""){
                                                    if(dp==datos[i][1] && pr==datos[i][3] && (datos[i][12]=="Especial" || datos[i][12]=="Uninominal/Especial") && es==datos[i][10] && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }else{
                                                    if(dp==datos[i][1] && pr==datos[i][3] && (datos[i][12]=="Especial" || datos[i][12]=="Uninominal/Especial") && es==datos[i][10]){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }
                                            }else{
                                                if(fi != "" && ff != ""){
                                                    if(dp==datos[i][1] && pr==datos[i][3] && (datos[i][12]=="Especial" || datos[i][12]=="Uninominal/Especial") && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }else{
                                                    if(dp==datos[i][1] && pr==datos[i][3] && (datos[i][12]=="Especial" || datos[i][12]=="Uninominal/Especial")){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }
                                            }
                                        }
                                        if(ci1 && ci2 == false && ci3 == false){
                                            if(estado.options[estado.selectedIndex].innerText != ""){
                                                if(fi != "" && ff != ""){
                                                    if(dp==datos[i][1] && pr==datos[i][3] && (datos[i][12]=="Uninominal") && es==datos[i][10] && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }else{
                                                    if(dp==datos[i][1] && pr==datos[i][3] && (datos[i][12]=="Uninominal") && es==datos[i][10]){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }
                                            }else{
                                                if(fi != "" && ff != ""){
                                                    if(dp==datos[i][1] && pr==datos[i][3] && (datos[i][12]=="Uninominal") && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }else{
                                                    if(dp==datos[i][1] && pr==datos[i][3] && (datos[i][12]=="Uninominal")){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }
                                            }
                                        }
                                        if(ci1 == false && ci2 && ci3 == false){
                                            if(estado.options[estado.selectedIndex].innerText != ""){
                                                if(fi != "" && ff != ""){
                                                    if(dp==datos[i][1] && pr==datos[i][3] && (datos[i][12]=="Especial") && es==datos[i][10] && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }else{
                                                    if(dp==datos[i][1] && pr==datos[i][3] && (datos[i][12]=="Especial") && es==datos[i][10]){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }
                                            }else{
                                                if(fi != "" && ff != ""){
                                                    if(dp==datos[i][1] && pr==datos[i][3] && (datos[i][12]=="Especial") && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }else{
                                                    if(dp==datos[i][1] && pr==datos[i][3] && (datos[i][12]=="Especial")){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }
                                            }
                                        }
                                        if(ci1 == false && ci2 == false && ci3){
                                            if(estado.options[estado.selectedIndex].innerText != ""){
                                                if(fi != "" && ff != ""){
                                                    if(dp==datos[i][1] && pr==datos[i][3] && (datos[i][12]=="Uninominal/Especial") && es==datos[i][10] && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }else{
                                                    if(dp==datos[i][1] && pr==datos[i][3] && (datos[i][12]=="Uninominal/Especial") && es==datos[i][10]){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }
                                            }else{
                                                if(fi != "" && ff != ""){
                                                    if(dp==datos[i][1] && pr==datos[i][3] && (datos[i][12]=="Uninominal/Especial") && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }else{
                                                    if(dp==datos[i][1] && pr==datos[i][3] && (datos[i][12]=="Uninominal/Especial")){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }
                                            }
                                        }
                                        if(ci1 == false && ci2 == false && ci3 == false){
                                            if(estado.options[estado.selectedIndex].innerText != ""){
                                                if(fi != "" && ff != ""){
                                                    if(dp==datos[i][1] && pr==datos[i][3] && es==datos[i][10] && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }else{
                                                    if(dp==datos[i][1] && pr==datos[i][3] && es==datos[i][10]){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }
                                            }else{
                                                if(fi != "" && ff != ""){
                                                    if(dp==datos[i][1] && pr==datos[i][3] && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }else{
                                                    if(dp==datos[i][1] && pr==datos[i][3]){
                                                        var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                        var marker = new google.maps.Marker({
                                                            position: position,
                                                            map: map,
                                                            icon: 'static/iconos/IconoGoogle.png',
                                                        });
                                                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                            return function() {
                                                                infowindow.setContent(
                                                                    '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                        '<TR>'+
                                                                             '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                             +'<div align="center">'
                                                                                +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                                +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                             +'</div>'
                                                                             +'</td>'+
                                                                        '</TR>'+
                                                                    '</TABLE>'
                                                                );
                                                                infowindow.setOptions({maxWidth: 200});
                                                                infowindow.open(map, marker);
                                                            }
                                                        }) (marker, i));
                                                        Markers[datos[i][7]] = marker;
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }else{
                                    if(ci1 && ci2 && ci3){
                                        if(estado.options[estado.selectedIndex].innerText != ""){
                                            if(fi != "" && ff != ""){
                                                if(dp==datos[i][1] && (datos[i][12]=="Uninominal" || datos[i][12]=="Especial" || datos[i][12]=="Uninominal/Especial") && es==datos[i][10] && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                    var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                    var marker = new google.maps.Marker({
                                                        position: position,
                                                        map: map,
                                                        icon: 'static/iconos/IconoGoogle.png',
                                                    });
                                                    google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                        return function() {
                                                            infowindow.setContent(
                                                                '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                    '<TR>'+
                                                                         '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                         +'<div align="center">'
                                                                            +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                         +'</div>'
                                                                         +'</td>'+
                                                                    '</TR>'+
                                                                '</TABLE>'
                                                            );
                                                            infowindow.setOptions({maxWidth: 200});
                                                            infowindow.open(map, marker);
                                                        }
                                                    }) (marker, i));
                                                    Markers[datos[i][7]] = marker;
                                                }
                                            }else{
                                                if(dp==datos[i][1] && (datos[i][12]=="Uninominal" || datos[i][12]=="Especial" || datos[i][12]=="Uninominal/Especial") && es==datos[i][10]){
                                                    var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                    var marker = new google.maps.Marker({
                                                        position: position,
                                                        map: map,
                                                        icon: 'static/iconos/IconoGoogle.png',
                                                    });
                                                    google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                        return function() {
                                                            infowindow.setContent(
                                                                '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                    '<TR>'+
                                                                         '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                         +'<div align="center">'
                                                                            +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                         +'</div>'
                                                                         +'</td>'+
                                                                    '</TR>'+
                                                                '</TABLE>'
                                                            );
                                                            infowindow.setOptions({maxWidth: 200});
                                                            infowindow.open(map, marker);
                                                        }
                                                    }) (marker, i));
                                                    Markers[datos[i][7]] = marker;
                                                }
                                            }
                                        }else{
                                            if(fi != "" && ff != ""){
                                                if(dp==datos[i][1] && (datos[i][12]=="Uninominal" || datos[i][12]=="Especial" || datos[i][12]=="Uninominal/Especial") && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                    var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                    var marker = new google.maps.Marker({
                                                        position: position,
                                                        map: map,
                                                        icon: 'static/iconos/IconoGoogle.png',
                                                    });
                                                    google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                        return function() {
                                                            infowindow.setContent(
                                                                '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                    '<TR>'+
                                                                         '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                         +'<div align="center">'
                                                                            +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                         +'</div>'
                                                                         +'</td>'+
                                                                    '</TR>'+
                                                                '</TABLE>'
                                                            );
                                                            infowindow.setOptions({maxWidth: 200});
                                                            infowindow.open(map, marker);
                                                        }
                                                    }) (marker, i));
                                                    Markers[datos[i][7]] = marker;
                                                }
                                            }else{
                                                if(dp==datos[i][1] && (datos[i][12]=="Uninominal" || datos[i][12]=="Especial" || datos[i][12]=="Uninominal/Especial")){
                                                    var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                    var marker = new google.maps.Marker({
                                                        position: position,
                                                        map: map,
                                                        icon: 'static/iconos/IconoGoogle.png',
                                                    });
                                                    google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                        return function() {
                                                            infowindow.setContent(
                                                                '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                    '<TR>'+
                                                                         '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                         +'<div align="center">'
                                                                            +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                         +'</div>'
                                                                         +'</td>'+
                                                                    '</TR>'+
                                                                '</TABLE>'
                                                            );
                                                            infowindow.setOptions({maxWidth: 200});
                                                            infowindow.open(map, marker);
                                                        }
                                                    }) (marker, i));
                                                    Markers[datos[i][7]] = marker;
                                                }
                                            }
                                        }
                                    }
                                    if(ci1 && ci2 && ci3 == false){
                                        if(estado.options[estado.selectedIndex].innerText != ""){
                                            if(fi != "" && ff != ""){
                                                if(dp==datos[i][1] && (datos[i][12]=="Uninominal" || datos[i][12]=="Especial") && es==datos[i][10] && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                    var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                    var marker = new google.maps.Marker({
                                                        position: position,
                                                        map: map,
                                                        icon: 'static/iconos/IconoGoogle.png',
                                                    });
                                                    google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                        return function() {
                                                            infowindow.setContent(
                                                                '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                    '<TR>'+
                                                                         '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                         +'<div align="center">'
                                                                            +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                         +'</div>'
                                                                         +'</td>'+
                                                                    '</TR>'+
                                                                '</TABLE>'
                                                            );
                                                            infowindow.setOptions({maxWidth: 200});
                                                            infowindow.open(map, marker);
                                                        }
                                                    }) (marker, i));
                                                    Markers[datos[i][7]] = marker;
                                                }
                                            }else{
                                                if(dp==datos[i][1] && (datos[i][12]=="Uninominal" || datos[i][12]=="Especial") && es==datos[i][10]){
                                                    var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                    var marker = new google.maps.Marker({
                                                        position: position,
                                                        map: map,
                                                        icon: 'static/iconos/IconoGoogle.png',
                                                    });
                                                    google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                        return function() {
                                                            infowindow.setContent(
                                                                '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                    '<TR>'+
                                                                         '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                         +'<div align="center">'
                                                                            +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                         +'</div>'
                                                                         +'</td>'+
                                                                    '</TR>'+
                                                                '</TABLE>'
                                                            );
                                                            infowindow.setOptions({maxWidth: 200});
                                                            infowindow.open(map, marker);
                                                        }
                                                    }) (marker, i));
                                                    Markers[datos[i][7]] = marker;
                                                }
                                            }
                                        }else{
                                            if(fi != "" && ff != ""){
                                                if(dp==datos[i][1] && (datos[i][12]=="Uninominal" || datos[i][12]=="Especial") && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                    var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                    var marker = new google.maps.Marker({
                                                        position: position,
                                                        map: map,
                                                        icon: 'static/iconos/IconoGoogle.png',
                                                    });
                                                    google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                        return function() {
                                                            infowindow.setContent(
                                                                '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                    '<TR>'+
                                                                         '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                         +'<div align="center">'
                                                                            +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                         +'</div>'
                                                                         +'</td>'+
                                                                    '</TR>'+
                                                                '</TABLE>'
                                                            );
                                                            infowindow.setOptions({maxWidth: 200});
                                                            infowindow.open(map, marker);
                                                        }
                                                    }) (marker, i));
                                                    Markers[datos[i][7]] = marker;
                                                }
                                            }else{
                                                if(dp==datos[i][1] && (datos[i][12]=="Uninominal" || datos[i][12]=="Especial")){
                                                    var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                    var marker = new google.maps.Marker({
                                                        position: position,
                                                        map: map,
                                                        icon: 'static/iconos/IconoGoogle.png',
                                                    });
                                                    google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                        return function() {
                                                            infowindow.setContent(
                                                                '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                    '<TR>'+
                                                                         '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                         +'<div align="center">'
                                                                            +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                         +'</div>'
                                                                         +'</td>'+
                                                                    '</TR>'+
                                                                '</TABLE>'
                                                            );
                                                            infowindow.setOptions({maxWidth: 200});
                                                            infowindow.open(map, marker);
                                                        }
                                                    }) (marker, i));
                                                    Markers[datos[i][7]] = marker;
                                                }
                                            }
                                        }
                                    }
                                    if(ci1 && ci2 == false && ci3){
                                        if(estado.options[estado.selectedIndex].innerText != ""){
                                            if(fi != "" && ff != ""){
                                                if(dp==datos[i][1] && (datos[i][12]=="Uninominal" || datos[i][12]=="Uninominal/Especial") && es==datos[i][10] && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                    var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                    var marker = new google.maps.Marker({
                                                        position: position,
                                                        map: map,
                                                        icon: 'static/iconos/IconoGoogle.png',
                                                    });
                                                    google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                        return function() {
                                                            infowindow.setContent(
                                                                '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                    '<TR>'+
                                                                         '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                         +'<div align="center">'
                                                                            +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                         +'</div>'
                                                                         +'</td>'+
                                                                    '</TR>'+
                                                                '</TABLE>'
                                                            );
                                                            infowindow.setOptions({maxWidth: 200});
                                                            infowindow.open(map, marker);
                                                        }
                                                    }) (marker, i));
                                                    Markers[datos[i][7]] = marker;
                                                }
                                            }else{
                                                if(dp==datos[i][1] && (datos[i][12]=="Uninominal" || datos[i][12]=="Uninominal/Especial") && es==datos[i][10]){
                                                    var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                    var marker = new google.maps.Marker({
                                                        position: position,
                                                        map: map,
                                                        icon: 'static/iconos/IconoGoogle.png',
                                                    });
                                                    google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                        return function() {
                                                            infowindow.setContent(
                                                                '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                    '<TR>'+
                                                                         '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                         +'<div align="center">'
                                                                            +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                         +'</div>'
                                                                         +'</td>'+
                                                                    '</TR>'+
                                                                '</TABLE>'
                                                            );
                                                            infowindow.setOptions({maxWidth: 200});
                                                            infowindow.open(map, marker);
                                                        }
                                                    }) (marker, i));
                                                    Markers[datos[i][7]] = marker;
                                                }
                                            }
                                        }else{
                                            if(fi != "" && ff != ""){
                                                if(dp==datos[i][1] && (datos[i][12]=="Uninominal" || datos[i][12]=="Uninominal/Especial") && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                    var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                    var marker = new google.maps.Marker({
                                                        position: position,
                                                        map: map,
                                                        icon: 'static/iconos/IconoGoogle.png',
                                                    });
                                                    google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                        return function() {
                                                            infowindow.setContent(
                                                                '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                    '<TR>'+
                                                                         '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                         +'<div align="center">'
                                                                            +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                         +'</div>'
                                                                         +'</td>'+
                                                                    '</TR>'+
                                                                '</TABLE>'
                                                            );
                                                            infowindow.setOptions({maxWidth: 200});
                                                            infowindow.open(map, marker);
                                                        }
                                                    }) (marker, i));
                                                    Markers[datos[i][7]] = marker;
                                                }
                                            }else{
                                                if(dp==datos[i][1] && (datos[i][12]=="Uninominal" || datos[i][12]=="Uninominal/Especial")){
                                                    var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                    var marker = new google.maps.Marker({
                                                        position: position,
                                                        map: map,
                                                        icon: 'static/iconos/IconoGoogle.png',
                                                    });
                                                    google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                        return function() {
                                                            infowindow.setContent(
                                                                '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                    '<TR>'+
                                                                         '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                         +'<div align="center">'
                                                                            +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                         +'</div>'
                                                                         +'</td>'+
                                                                    '</TR>'+
                                                                '</TABLE>'
                                                            );
                                                            infowindow.setOptions({maxWidth: 200});
                                                            infowindow.open(map, marker);
                                                        }
                                                    }) (marker, i));
                                                    Markers[datos[i][7]] = marker;
                                                }
                                            }
                                        }
                                    }
                                    if(ci1 == false && ci2 && ci3){
                                        if(estado.options[estado.selectedIndex].innerText != ""){
                                            if(fi != "" && ff != ""){
                                                if(dp==datos[i][1] && (datos[i][12]=="Especial" || datos[i][12]=="Uninominal/Especial") && es==datos[i][10] && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                    var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                    var marker = new google.maps.Marker({
                                                        position: position,
                                                        map: map,
                                                        icon: 'static/iconos/IconoGoogle.png',
                                                    });
                                                    google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                        return function() {
                                                            infowindow.setContent(
                                                                '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                    '<TR>'+
                                                                         '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                         +'<div align="center">'
                                                                            +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                         +'</div>'
                                                                         +'</td>'+
                                                                    '</TR>'+
                                                                '</TABLE>'
                                                            );
                                                            infowindow.setOptions({maxWidth: 200});
                                                            infowindow.open(map, marker);
                                                        }
                                                    }) (marker, i));
                                                    Markers[datos[i][7]] = marker;
                                                }
                                            }else{
                                                if(dp==datos[i][1] && (datos[i][12]=="Especial" || datos[i][12]=="Uninominal/Especial") && es==datos[i][10]){
                                                    var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                    var marker = new google.maps.Marker({
                                                        position: position,
                                                        map: map,
                                                        icon: 'static/iconos/IconoGoogle.png',
                                                    });
                                                    google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                        return function() {
                                                            infowindow.setContent(
                                                                '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                    '<TR>'+
                                                                         '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                         +'<div align="center">'
                                                                            +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                         +'</div>'
                                                                         +'</td>'+
                                                                    '</TR>'+
                                                                '</TABLE>'
                                                            );
                                                            infowindow.setOptions({maxWidth: 200});
                                                            infowindow.open(map, marker);
                                                        }
                                                    }) (marker, i));
                                                    Markers[datos[i][7]] = marker;
                                                }
                                            }
                                        }else{
                                            if(fi != "" && ff != ""){
                                                if(dp==datos[i][1] && (datos[i][12]=="Especial" || datos[i][12]=="Uninominal/Especial") && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                    var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                    var marker = new google.maps.Marker({
                                                        position: position,
                                                        map: map,
                                                        icon: 'static/iconos/IconoGoogle.png',
                                                    });
                                                    google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                        return function() {
                                                            infowindow.setContent(
                                                                '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                    '<TR>'+
                                                                         '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                         +'<div align="center">'
                                                                            +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                         +'</div>'
                                                                         +'</td>'+
                                                                    '</TR>'+
                                                                '</TABLE>'
                                                            );
                                                            infowindow.setOptions({maxWidth: 200});
                                                            infowindow.open(map, marker);
                                                        }
                                                    }) (marker, i));
                                                    Markers[datos[i][7]] = marker;
                                                }
                                            }else{
                                                if(dp==datos[i][1] && (datos[i][12]=="Especial" || datos[i][12]=="Uninominal/Especial")){
                                                    var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                    var marker = new google.maps.Marker({
                                                        position: position,
                                                        map: map,
                                                        icon: 'static/iconos/IconoGoogle.png',
                                                    });
                                                    google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                        return function() {
                                                            infowindow.setContent(
                                                                '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                    '<TR>'+
                                                                         '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                         +'<div align="center">'
                                                                            +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                         +'</div>'
                                                                         +'</td>'+
                                                                    '</TR>'+
                                                                '</TABLE>'
                                                            );
                                                            infowindow.setOptions({maxWidth: 200});
                                                            infowindow.open(map, marker);
                                                        }
                                                    }) (marker, i));
                                                    Markers[datos[i][7]] = marker;
                                                }
                                            }
                                        }
                                    }
                                    if(ci1 && ci2 == false && ci3 == false){
                                        if(estado.options[estado.selectedIndex].innerText != ""){
                                            if(fi != "" && ff != ""){
                                                if(dp==datos[i][1] && (datos[i][12]=="Uninominal") && es==datos[i][10] && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                    var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                    var marker = new google.maps.Marker({
                                                        position: position,
                                                        map: map,
                                                        icon: 'static/iconos/IconoGoogle.png',
                                                    });
                                                    google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                        return function() {
                                                            infowindow.setContent(
                                                                '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                    '<TR>'+
                                                                         '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                         +'<div align="center">'
                                                                            +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                         +'</div>'
                                                                         +'</td>'+
                                                                    '</TR>'+
                                                                '</TABLE>'
                                                            );
                                                            infowindow.setOptions({maxWidth: 200});
                                                            infowindow.open(map, marker);
                                                        }
                                                    }) (marker, i));
                                                    Markers[datos[i][7]] = marker;
                                                }
                                            }else{
                                                if(dp==datos[i][1] && (datos[i][12]=="Uninominal") && es==datos[i][10]){
                                                    var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                    var marker = new google.maps.Marker({
                                                        position: position,
                                                        map: map,
                                                        icon: 'static/iconos/IconoGoogle.png',
                                                    });
                                                    google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                        return function() {
                                                            infowindow.setContent(
                                                                '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                    '<TR>'+
                                                                         '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                         +'<div align="center">'
                                                                            +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                         +'</div>'
                                                                         +'</td>'+
                                                                    '</TR>'+
                                                                '</TABLE>'
                                                            );
                                                            infowindow.setOptions({maxWidth: 200});
                                                            infowindow.open(map, marker);
                                                        }
                                                    }) (marker, i));
                                                    Markers[datos[i][7]] = marker;
                                                }
                                            }
                                        }else{
                                            if(fi != "" && ff != ""){
                                                if(dp==datos[i][1] && (datos[i][12]=="Uninominal") && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                    var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                    var marker = new google.maps.Marker({
                                                        position: position,
                                                        map: map,
                                                        icon: 'static/iconos/IconoGoogle.png',
                                                    });
                                                    google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                        return function() {
                                                            infowindow.setContent(
                                                                '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                    '<TR>'+
                                                                         '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                         +'<div align="center">'
                                                                            +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                         +'</div>'
                                                                         +'</td>'+
                                                                    '</TR>'+
                                                                '</TABLE>'
                                                            );
                                                            infowindow.setOptions({maxWidth: 200});
                                                            infowindow.open(map, marker);
                                                        }
                                                    }) (marker, i));
                                                    Markers[datos[i][7]] = marker;
                                                }
                                            }else{
                                                if(dp==datos[i][1] && (datos[i][12]=="Uninominal")){
                                                    var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                    var marker = new google.maps.Marker({
                                                        position: position,
                                                        map: map,
                                                        icon: 'static/iconos/IconoGoogle.png',
                                                    });
                                                    google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                        return function() {
                                                            infowindow.setContent(
                                                                '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                    '<TR>'+
                                                                         '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                         +'<div align="center">'
                                                                            +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                         +'</div>'
                                                                         +'</td>'+
                                                                    '</TR>'+
                                                                '</TABLE>'
                                                            );
                                                            infowindow.setOptions({maxWidth: 200});
                                                            infowindow.open(map, marker);
                                                        }
                                                    }) (marker, i));
                                                    Markers[datos[i][7]] = marker;
                                                }
                                            }
                                        }
                                    }
                                    if(ci1 == false && ci2 && ci3 == false){
                                        if(estado.options[estado.selectedIndex].innerText != ""){
                                            if(fi != "" && ff != ""){
                                                if(dp==datos[i][1] && (datos[i][12]=="Especial") && es==datos[i][10] && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                    var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                    var marker = new google.maps.Marker({
                                                        position: position,
                                                        map: map,
                                                        icon: 'static/iconos/IconoGoogle.png',
                                                    });
                                                    google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                        return function() {
                                                            infowindow.setContent(
                                                                '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                    '<TR>'+
                                                                         '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                         +'<div align="center">'
                                                                            +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                         +'</div>'
                                                                         +'</td>'+
                                                                    '</TR>'+
                                                                '</TABLE>'
                                                            );
                                                            infowindow.setOptions({maxWidth: 200});
                                                            infowindow.open(map, marker);
                                                        }
                                                    }) (marker, i));
                                                    Markers[datos[i][7]] = marker;
                                                }
                                            }else{
                                                if(dp==datos[i][1] && (datos[i][12]=="Especial") && es==datos[i][10]){
                                                    var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                    var marker = new google.maps.Marker({
                                                        position: position,
                                                        map: map,
                                                        icon: 'static/iconos/IconoGoogle.png',
                                                    });
                                                    google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                        return function() {
                                                            infowindow.setContent(
                                                                '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                    '<TR>'+
                                                                         '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                         +'<div align="center">'
                                                                            +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                         +'</div>'
                                                                         +'</td>'+
                                                                    '</TR>'+
                                                                '</TABLE>'
                                                            );
                                                            infowindow.setOptions({maxWidth: 200});
                                                            infowindow.open(map, marker);
                                                        }
                                                    }) (marker, i));
                                                    Markers[datos[i][7]] = marker;
                                                }
                                            }
                                        }else{
                                            if(fi != "" && ff != ""){
                                                if(dp==datos[i][1] && (datos[i][12]=="Especial") && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                    var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                    var marker = new google.maps.Marker({
                                                        position: position,
                                                        map: map,
                                                        icon: 'static/iconos/IconoGoogle.png',
                                                    });
                                                    google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                        return function() {
                                                            infowindow.setContent(
                                                                '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                    '<TR>'+
                                                                         '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                         +'<div align="center">'
                                                                            +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                         +'</div>'
                                                                         +'</td>'+
                                                                    '</TR>'+
                                                                '</TABLE>'
                                                            );
                                                            infowindow.setOptions({maxWidth: 200});
                                                            infowindow.open(map, marker);
                                                        }
                                                    }) (marker, i));
                                                    Markers[datos[i][7]] = marker;
                                                }
                                            }else{
                                                if(dp==datos[i][1] && (datos[i][12]=="Especial")){
                                                    var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                    var marker = new google.maps.Marker({
                                                        position: position,
                                                        map: map,
                                                        icon: 'static/iconos/IconoGoogle.png',
                                                    });
                                                    google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                        return function() {
                                                            infowindow.setContent(
                                                                '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                    '<TR>'+
                                                                         '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                         +'<div align="center">'
                                                                            +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                         +'</div>'
                                                                         +'</td>'+
                                                                    '</TR>'+
                                                                '</TABLE>'
                                                            );
                                                            infowindow.setOptions({maxWidth: 200});
                                                            infowindow.open(map, marker);
                                                        }
                                                    }) (marker, i));
                                                    Markers[datos[i][7]] = marker;
                                                }
                                            }
                                        }
                                    }
                                    if(ci1 == false && ci2 == false && ci3){
                                        if(estado.options[estado.selectedIndex].innerText != ""){
                                            if(fi != "" && ff != ""){
                                                if(dp==datos[i][1] && (datos[i][12]=="Uninominal/Especial") && es==datos[i][10] && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                    var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                    var marker = new google.maps.Marker({
                                                        position: position,
                                                        map: map,
                                                        icon: 'static/iconos/IconoGoogle.png',
                                                    });
                                                    google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                        return function() {
                                                            infowindow.setContent(
                                                                '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                    '<TR>'+
                                                                         '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                         +'<div align="center">'
                                                                            +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                         +'</div>'
                                                                         +'</td>'+
                                                                    '</TR>'+
                                                                '</TABLE>'
                                                            );
                                                            infowindow.setOptions({maxWidth: 200});
                                                            infowindow.open(map, marker);
                                                        }
                                                    }) (marker, i));
                                                    Markers[datos[i][7]] = marker;
                                                }
                                            }else{
                                                if(dp==datos[i][1] && (datos[i][12]=="Uninominal/Especial") && es==datos[i][10]){
                                                    var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                    var marker = new google.maps.Marker({
                                                        position: position,
                                                        map: map,
                                                        icon: 'static/iconos/IconoGoogle.png',
                                                    });
                                                    google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                        return function() {
                                                            infowindow.setContent(
                                                                '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                    '<TR>'+
                                                                         '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                         +'<div align="center">'
                                                                            +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                         +'</div>'
                                                                         +'</td>'+
                                                                    '</TR>'+
                                                                '</TABLE>'
                                                            );
                                                            infowindow.setOptions({maxWidth: 200});
                                                            infowindow.open(map, marker);
                                                        }
                                                    }) (marker, i));
                                                    Markers[datos[i][7]] = marker;
                                                }
                                            }
                                        }else{
                                            if(fi != "" && ff != ""){
                                                if(dp==datos[i][1] && (datos[i][12]=="Uninominal/Especial") && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                    var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                    var marker = new google.maps.Marker({
                                                        position: position,
                                                        map: map,
                                                        icon: 'static/iconos/IconoGoogle.png',
                                                    });
                                                    google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                        return function() {
                                                            infowindow.setContent(
                                                                '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                    '<TR>'+
                                                                         '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                         +'<div align="center">'
                                                                            +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                         +'</div>'
                                                                         +'</td>'+
                                                                    '</TR>'+
                                                                '</TABLE>'
                                                            );
                                                            infowindow.setOptions({maxWidth: 200});
                                                            infowindow.open(map, marker);
                                                        }
                                                    }) (marker, i));
                                                    Markers[datos[i][7]] = marker;
                                                }
                                            }else{
                                                if(dp==datos[i][1] && (datos[i][12]=="Uninominal/Especial")){
                                                    var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                    var marker = new google.maps.Marker({
                                                        position: position,
                                                        map: map,
                                                        icon: 'static/iconos/IconoGoogle.png',
                                                    });
                                                    google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                        return function() {
                                                            infowindow.setContent(
                                                                '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                    '<TR>'+
                                                                         '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                         +'<div align="center">'
                                                                            +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                         +'</div>'
                                                                         +'</td>'+
                                                                    '</TR>'+
                                                                '</TABLE>'
                                                            );
                                                            infowindow.setOptions({maxWidth: 200});
                                                            infowindow.open(map, marker);
                                                        }
                                                    }) (marker, i));
                                                    Markers[datos[i][7]] = marker;
                                                }
                                            }
                                        }
                                    }
                                    if(ci1 == false && ci2 == false && ci3 == false){
                                        if(estado.options[estado.selectedIndex].innerText != ""){
                                            if(fi != "" && ff != ""){
                                                if(dp==datos[i][1] && es==datos[i][10] && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                    var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                    var marker = new google.maps.Marker({
                                                        position: position,
                                                        map: map,
                                                        icon: 'static/iconos/IconoGoogle.png',
                                                    });
                                                    google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                        return function() {
                                                            infowindow.setContent(
                                                                '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                    '<TR>'+
                                                                         '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                         +'<div align="center">'
                                                                            +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                         +'</div>'
                                                                         +'</td>'+
                                                                    '</TR>'+
                                                                '</TABLE>'
                                                            );
                                                            infowindow.setOptions({maxWidth: 200});
                                                            infowindow.open(map, marker);
                                                        }
                                                    }) (marker, i));
                                                    Markers[datos[i][7]] = marker;
                                                }
                                            }else{
                                                if(dp==datos[i][1] && es==datos[i][10]){
                                                    var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                    var marker = new google.maps.Marker({
                                                        position: position,
                                                        map: map,
                                                        icon: 'static/iconos/IconoGoogle.png',
                                                    });
                                                    google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                        return function() {
                                                            infowindow.setContent(
                                                                '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                    '<TR>'+
                                                                         '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                         +'<div align="center">'
                                                                            +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                         +'</div>'
                                                                         +'</td>'+
                                                                    '</TR>'+
                                                                '</TABLE>'
                                                            );
                                                            infowindow.setOptions({maxWidth: 200});
                                                            infowindow.open(map, marker);
                                                        }
                                                    }) (marker, i));
                                                    Markers[datos[i][7]] = marker;
                                                }
                                            }
                                        }else{
                                            if(fi != "" && ff != ""){
                                                if(dp==datos[i][1] && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                    var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                    var marker = new google.maps.Marker({
                                                        position: position,
                                                        map: map,
                                                        icon: 'static/iconos/IconoGoogle.png',
                                                    });
                                                    google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                        return function() {
                                                            infowindow.setContent(
                                                                '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                    '<TR>'+
                                                                         '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                         +'<div align="center">'
                                                                            +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                         +'</div>'
                                                                         +'</td>'+
                                                                    '</TR>'+
                                                                '</TABLE>'
                                                            );
                                                            infowindow.setOptions({maxWidth: 200});
                                                            infowindow.open(map, marker);
                                                        }
                                                    }) (marker, i));
                                                    Markers[datos[i][7]] = marker;
                                                }
                                            }else{
                                                if(dp==datos[i][1]){
                                                    var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                    var marker = new google.maps.Marker({
                                                        position: position,
                                                        map: map,
                                                        icon: 'static/iconos/IconoGoogle.png',
                                                    });
                                                    google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                        return function() {
                                                            infowindow.setContent(
                                                                '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                    '<TR>'+
                                                                         '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                         +'<div align="center">'
                                                                            +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                            +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                         +'</div>'
                                                                         +'</td>'+
                                                                    '</TR>'+
                                                                '</TABLE>'
                                                            );
                                                            infowindow.setOptions({maxWidth: 200});
                                                            infowindow.open(map, marker);
                                                        }
                                                    }) (marker, i));
                                                    Markers[datos[i][7]] = marker;
                                                }
                                            }
                                        }
                                    }
                                }
                            }else{
                                if(ci1 && ci2 && ci3){
                                    if(estado.options[estado.selectedIndex].innerText != ""){
                                        if(fi != "" && ff != ""){
                                            if((datos[i][12]=="Uninominal" || datos[i][12]=="Especial" || datos[i][12]=="Uninominal/Especial") && es==datos[i][10] && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                var marker = new google.maps.Marker({
                                                    position: position,
                                                    map: map,
                                                    icon: 'static/iconos/IconoGoogle.png',
                                                });
                                                google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                    return function() {
                                                        infowindow.setContent(
                                                            '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                '<TR>'+
                                                                     '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                     +'<div align="center">'
                                                                        +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                     +'</div>'
                                                                     +'</td>'+
                                                                '</TR>'+
                                                            '</TABLE>'
                                                        );
                                                        infowindow.setOptions({maxWidth: 200});
                                                        infowindow.open(map, marker);
                                                    }
                                                }) (marker, i));
                                                Markers[datos[i][7]] = marker;
                                            }
                                        }else{
                                            if((datos[i][12]=="Uninominal" || datos[i][12]=="Especial" || datos[i][12]=="Uninominal/Especial") && es==datos[i][10]){
                                                var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                var marker = new google.maps.Marker({
                                                    position: position,
                                                    map: map,
                                                    icon: 'static/iconos/IconoGoogle.png',
                                                });
                                                google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                    return function() {
                                                        infowindow.setContent(
                                                            '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                '<TR>'+
                                                                     '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                     +'<div align="center">'
                                                                        +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                     +'</div>'
                                                                     +'</td>'+
                                                                '</TR>'+
                                                            '</TABLE>'
                                                        );
                                                        infowindow.setOptions({maxWidth: 200});
                                                        infowindow.open(map, marker);
                                                    }
                                                }) (marker, i));
                                                Markers[datos[i][7]] = marker;
                                            }
                                        }
                                    }else{
                                        if(fi != "" && ff != ""){
                                            if((datos[i][12]=="Uninominal" || datos[i][12]=="Especial" || datos[i][12]=="Uninominal/Especial") && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                var marker = new google.maps.Marker({
                                                    position: position,
                                                    map: map,
                                                    icon: 'static/iconos/IconoGoogle.png',
                                                });
                                                google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                    return function() {
                                                        infowindow.setContent(
                                                            '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                '<TR>'+
                                                                     '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                     +'<div align="center">'
                                                                        +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                     +'</div>'
                                                                     +'</td>'+
                                                                '</TR>'+
                                                            '</TABLE>'
                                                        );
                                                        infowindow.setOptions({maxWidth: 200});
                                                        infowindow.open(map, marker);
                                                    }
                                                }) (marker, i));
                                                Markers[datos[i][7]] = marker;
                                            }
                                        }else{
                                            if((datos[i][12]=="Uninominal" || datos[i][12]=="Especial" || datos[i][12]=="Uninominal/Especial")){
                                                var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                var marker = new google.maps.Marker({
                                                    position: position,
                                                    map: map,
                                                    icon: 'static/iconos/IconoGoogle.png',
                                                });
                                                google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                    return function() {
                                                        infowindow.setContent(
                                                            '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                '<TR>'+
                                                                     '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                     +'<div align="center">'
                                                                        +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                     +'</div>'
                                                                     +'</td>'+
                                                                '</TR>'+
                                                            '</TABLE>'
                                                        );
                                                        infowindow.setOptions({maxWidth: 200});
                                                        infowindow.open(map, marker);
                                                    }
                                                }) (marker, i));
                                                Markers[datos[i][7]] = marker;
                                            }
                                        }
                                    }
                                }
                                if(ci1 && ci2 && ci3 == false){
                                    if(estado.options[estado.selectedIndex].innerText != ""){
                                        if(fi != "" && ff != ""){
                                            if((datos[i][12]=="Uninominal" || datos[i][12]=="Especial") && es==datos[i][10] && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                var marker = new google.maps.Marker({
                                                    position: position,
                                                    map: map,
                                                    icon: 'static/iconos/IconoGoogle.png',
                                                });
                                                google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                    return function() {
                                                        infowindow.setContent(
                                                            '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                '<TR>'+
                                                                     '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                     +'<div align="center">'
                                                                        +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                     +'</div>'
                                                                     +'</td>'+
                                                                '</TR>'+
                                                            '</TABLE>'
                                                        );
                                                        infowindow.setOptions({maxWidth: 200});
                                                        infowindow.open(map, marker);
                                                    }
                                                }) (marker, i));
                                                Markers[datos[i][7]] = marker;
                                            }
                                        }else{
                                            if((datos[i][12]=="Uninominal" || datos[i][12]=="Especial") && es==datos[i][10]){
                                                var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                var marker = new google.maps.Marker({
                                                    position: position,
                                                    map: map,
                                                    icon: 'static/iconos/IconoGoogle.png',
                                                });
                                                google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                    return function() {
                                                        infowindow.setContent(
                                                            '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                '<TR>'+
                                                                     '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                     +'<div align="center">'
                                                                        +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                     +'</div>'
                                                                     +'</td>'+
                                                                '</TR>'+
                                                            '</TABLE>'
                                                        );
                                                        infowindow.setOptions({maxWidth: 200});
                                                        infowindow.open(map, marker);
                                                    }
                                                }) (marker, i));
                                                Markers[datos[i][7]] = marker;
                                            }
                                        }
                                    }else{
                                        if(fi != "" && ff != ""){
                                            if((datos[i][12]=="Uninominal" || datos[i][12]=="Especial") && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                var marker = new google.maps.Marker({
                                                    position: position,
                                                    map: map,
                                                    icon: 'static/iconos/IconoGoogle.png',
                                                });
                                                google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                    return function() {
                                                        infowindow.setContent(
                                                            '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                '<TR>'+
                                                                     '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                     +'<div align="center">'
                                                                        +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                     +'</div>'
                                                                     +'</td>'+
                                                                '</TR>'+
                                                            '</TABLE>'
                                                        );
                                                        infowindow.setOptions({maxWidth: 200});
                                                        infowindow.open(map, marker);
                                                    }
                                                }) (marker, i));
                                                Markers[datos[i][7]] = marker;
                                            }
                                        }else{
                                            if((datos[i][12]=="Uninominal" || datos[i][12]=="Especial")){
                                                var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                var marker = new google.maps.Marker({
                                                    position: position,
                                                    map: map,
                                                    icon: 'static/iconos/IconoGoogle.png',
                                                });
                                                google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                    return function() {
                                                        infowindow.setContent(
                                                            '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                '<TR>'+
                                                                     '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                     +'<div align="center">'
                                                                        +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                     +'</div>'
                                                                     +'</td>'+
                                                                '</TR>'+
                                                            '</TABLE>'
                                                        );
                                                        infowindow.setOptions({maxWidth: 200});
                                                        infowindow.open(map, marker);
                                                    }
                                                }) (marker, i));
                                                Markers[datos[i][7]] = marker;
                                            }
                                        }
                                    }
                                }
                                if(ci1 && ci2 == false && ci3){
                                    if(estado.options[estado.selectedIndex].innerText != ""){
                                        if(fi != "" && ff != ""){
                                            if((datos[i][12]=="Uninominal" || datos[i][12]=="Uninominal/Especial") && es==datos[i][10] && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                var marker = new google.maps.Marker({
                                                    position: position,
                                                    map: map,
                                                    icon: 'static/iconos/IconoGoogle.png',
                                                });
                                                google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                    return function() {
                                                        infowindow.setContent(
                                                            '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                '<TR>'+
                                                                     '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                     +'<div align="center">'
                                                                        +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                     +'</div>'
                                                                     +'</td>'+
                                                                '</TR>'+
                                                            '</TABLE>'
                                                        );
                                                        infowindow.setOptions({maxWidth: 200});
                                                        infowindow.open(map, marker);
                                                    }
                                                }) (marker, i));
                                                Markers[datos[i][7]] = marker;
                                            }
                                        }else{
                                            if((datos[i][12]=="Uninominal" || datos[i][12]=="Uninominal/Especial") && es==datos[i][10]){
                                                var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                var marker = new google.maps.Marker({
                                                    position: position,
                                                    map: map,
                                                    icon: 'static/iconos/IconoGoogle.png',
                                                });
                                                google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                    return function() {
                                                        infowindow.setContent(
                                                            '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                '<TR>'+
                                                                     '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                     +'<div align="center">'
                                                                        +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                     +'</div>'
                                                                     +'</td>'+
                                                                '</TR>'+
                                                            '</TABLE>'
                                                        );
                                                        infowindow.setOptions({maxWidth: 200});
                                                        infowindow.open(map, marker);
                                                    }
                                                }) (marker, i));
                                                Markers[datos[i][7]] = marker;
                                            }
                                        }
                                    }else{
                                        if(fi != "" && ff != ""){
                                            if((datos[i][12]=="Uninominal" || datos[i][12]=="Uninominal/Especial") && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                var marker = new google.maps.Marker({
                                                    position: position,
                                                    map: map,
                                                    icon: 'static/iconos/IconoGoogle.png',
                                                });
                                                google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                    return function() {
                                                        infowindow.setContent(
                                                            '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                '<TR>'+
                                                                     '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                     +'<div align="center">'
                                                                        +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                     +'</div>'
                                                                     +'</td>'+
                                                                '</TR>'+
                                                            '</TABLE>'
                                                        );
                                                        infowindow.setOptions({maxWidth: 200});
                                                        infowindow.open(map, marker);
                                                    }
                                                }) (marker, i));
                                                Markers[datos[i][7]] = marker;
                                            }
                                        }else{
                                            if((datos[i][12]=="Uninominal" || datos[i][12]=="Uninominal/Especial")){
                                                var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                var marker = new google.maps.Marker({
                                                    position: position,
                                                    map: map,
                                                    icon: 'static/iconos/IconoGoogle.png',
                                                });
                                                google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                    return function() {
                                                        infowindow.setContent(
                                                            '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                '<TR>'+
                                                                     '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                     +'<div align="center">'
                                                                        +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                     +'</div>'
                                                                     +'</td>'+
                                                                '</TR>'+
                                                            '</TABLE>'
                                                        );
                                                        infowindow.setOptions({maxWidth: 200});
                                                        infowindow.open(map, marker);
                                                    }
                                                }) (marker, i));
                                                Markers[datos[i][7]] = marker;
                                            }
                                        }
                                    }
                                }
                                if(ci1 == false && ci2 && ci3){
                                    if(estado.options[estado.selectedIndex].innerText != ""){
                                        if(fi != "" && ff != ""){
                                            if((datos[i][12]=="Especial" || datos[i][12]=="Uninominal/Especial") && es==datos[i][10] && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                var marker = new google.maps.Marker({
                                                    position: position,
                                                    map: map,
                                                    icon: 'static/iconos/IconoGoogle.png',
                                                });
                                                google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                    return function() {
                                                        infowindow.setContent(
                                                            '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                '<TR>'+
                                                                     '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                     +'<div align="center">'
                                                                        +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                     +'</div>'
                                                                     +'</td>'+
                                                                '</TR>'+
                                                            '</TABLE>'
                                                        );
                                                        infowindow.setOptions({maxWidth: 200});
                                                        infowindow.open(map, marker);
                                                    }
                                                }) (marker, i));
                                                Markers[datos[i][7]] = marker;
                                            }
                                        }else{
                                            if((datos[i][12]=="Especial" || datos[i][12]=="Uninominal/Especial") && es==datos[i][10]){
                                                var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                var marker = new google.maps.Marker({
                                                    position: position,
                                                    map: map,
                                                    icon: 'static/iconos/IconoGoogle.png',
                                                });
                                                google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                    return function() {
                                                        infowindow.setContent(
                                                            '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                '<TR>'+
                                                                     '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                     +'<div align="center">'
                                                                        +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                     +'</div>'
                                                                     +'</td>'+
                                                                '</TR>'+
                                                            '</TABLE>'
                                                        );
                                                        infowindow.setOptions({maxWidth: 200});
                                                        infowindow.open(map, marker);
                                                    }
                                                }) (marker, i));
                                                Markers[datos[i][7]] = marker;
                                            }
                                        }
                                    }else{
                                        if(fi != "" && ff != ""){
                                            if((datos[i][12]=="Especial" || datos[i][12]=="Uninominal/Especial") && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                var marker = new google.maps.Marker({
                                                    position: position,
                                                    map: map,
                                                    icon: 'static/iconos/IconoGoogle.png',
                                                });
                                                google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                    return function() {
                                                        infowindow.setContent(
                                                            '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                '<TR>'+
                                                                     '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                     +'<div align="center">'
                                                                        +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                     +'</div>'
                                                                     +'</td>'+
                                                                '</TR>'+
                                                            '</TABLE>'
                                                        );
                                                        infowindow.setOptions({maxWidth: 200});
                                                        infowindow.open(map, marker);
                                                    }
                                                }) (marker, i));
                                                Markers[datos[i][7]] = marker;
                                            }
                                        }else{
                                            if((datos[i][12]=="Especial" || datos[i][12]=="Uninominal/Especial")){
                                                var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                var marker = new google.maps.Marker({
                                                    position: position,
                                                    map: map,
                                                    icon: 'static/iconos/IconoGoogle.png',
                                                });
                                                google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                    return function() {
                                                        infowindow.setContent(
                                                            '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                '<TR>'+
                                                                     '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                     +'<div align="center">'
                                                                        +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                     +'</div>'
                                                                     +'</td>'+
                                                                '</TR>'+
                                                            '</TABLE>'
                                                        );
                                                        infowindow.setOptions({maxWidth: 200});
                                                        infowindow.open(map, marker);
                                                    }
                                                }) (marker, i));
                                                Markers[datos[i][7]] = marker;
                                            }
                                        }
                                    }
                                }
                                if(ci1 && ci2 == false && ci3 == false){
                                    if(estado.options[estado.selectedIndex].innerText != ""){
                                        if(fi != "" && ff != ""){
                                            if((datos[i][12]=="Uninominal") && es==datos[i][10] && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                var marker = new google.maps.Marker({
                                                    position: position,
                                                    map: map,
                                                    icon: 'static/iconos/IconoGoogle.png',
                                                });
                                                google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                    return function() {
                                                        infowindow.setContent(
                                                            '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                '<TR>'+
                                                                     '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                     +'<div align="center">'
                                                                        +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                     +'</div>'
                                                                     +'</td>'+
                                                                '</TR>'+
                                                            '</TABLE>'
                                                        );
                                                        infowindow.setOptions({maxWidth: 200});
                                                        infowindow.open(map, marker);
                                                    }
                                                }) (marker, i));
                                                Markers[datos[i][7]] = marker;
                                            }
                                        }else{
                                            if((datos[i][12]=="Uninominal") && es==datos[i][10]){
                                                var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                var marker = new google.maps.Marker({
                                                    position: position,
                                                    map: map,
                                                    icon: 'static/iconos/IconoGoogle.png',
                                                });
                                                google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                    return function() {
                                                        infowindow.setContent(
                                                            '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                '<TR>'+
                                                                     '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                     +'<div align="center">'
                                                                        +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                     +'</div>'
                                                                     +'</td>'+
                                                                '</TR>'+
                                                            '</TABLE>'
                                                        );
                                                        infowindow.setOptions({maxWidth: 200});
                                                        infowindow.open(map, marker);
                                                    }
                                                }) (marker, i));
                                                Markers[datos[i][7]] = marker;
                                            }
                                        }
                                    }else{
                                        if(fi != "" && ff != ""){
                                            if((datos[i][12]=="Uninominal") && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                var marker = new google.maps.Marker({
                                                    position: position,
                                                    map: map,
                                                    icon: 'static/iconos/IconoGoogle.png',
                                                });
                                                google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                    return function() {
                                                        infowindow.setContent(
                                                            '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                '<TR>'+
                                                                     '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                     +'<div align="center">'
                                                                        +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                     +'</div>'
                                                                     +'</td>'+
                                                                '</TR>'+
                                                            '</TABLE>'
                                                        );
                                                        infowindow.setOptions({maxWidth: 200});
                                                        infowindow.open(map, marker);
                                                    }
                                                }) (marker, i));
                                                Markers[datos[i][7]] = marker;
                                            }
                                        }else{
                                            if((datos[i][12]=="Uninominal")){
                                                var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                var marker = new google.maps.Marker({
                                                    position: position,
                                                    map: map,
                                                    icon: 'static/iconos/IconoGoogle.png',
                                                });
                                                google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                    return function() {
                                                        infowindow.setContent(
                                                            '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                '<TR>'+
                                                                     '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                     +'<div align="center">'
                                                                        +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                     +'</div>'
                                                                     +'</td>'+
                                                                '</TR>'+
                                                            '</TABLE>'
                                                        );
                                                        infowindow.setOptions({maxWidth: 200});
                                                        infowindow.open(map, marker);
                                                    }
                                                }) (marker, i));
                                                Markers[datos[i][7]] = marker;
                                            }
                                        }
                                    }
                                }
                                if(ci1 == false && ci2 && ci3 == false){
                                    if(estado.options[estado.selectedIndex].innerText != ""){
                                        if(fi != "" && ff != ""){
                                            if((datos[i][12]=="Especial") && es==datos[i][10] && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                var marker = new google.maps.Marker({
                                                    position: position,
                                                    map: map,
                                                    icon: 'static/iconos/IconoGoogle.png',
                                                });
                                                google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                    return function() {
                                                        infowindow.setContent(
                                                            '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                '<TR>'+
                                                                     '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                     +'<div align="center">'
                                                                        +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                     +'</div>'
                                                                     +'</td>'+
                                                                '</TR>'+
                                                            '</TABLE>'
                                                        );
                                                        infowindow.setOptions({maxWidth: 200});
                                                        infowindow.open(map, marker);
                                                    }
                                                }) (marker, i));
                                                Markers[datos[i][7]] = marker;
                                            }
                                        }else{
                                            if((datos[i][12]=="Especial") && es==datos[i][10]){
                                                var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                var marker = new google.maps.Marker({
                                                    position: position,
                                                    map: map,
                                                    icon: 'static/iconos/IconoGoogle.png',
                                                });
                                                google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                    return function() {
                                                        infowindow.setContent(
                                                            '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                '<TR>'+
                                                                     '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                     +'<div align="center">'
                                                                        +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                     +'</div>'
                                                                     +'</td>'+
                                                                '</TR>'+
                                                            '</TABLE>'
                                                        );
                                                        infowindow.setOptions({maxWidth: 200});
                                                        infowindow.open(map, marker);
                                                    }
                                                }) (marker, i));
                                                Markers[datos[i][7]] = marker;
                                            }
                                        }
                                    }else{
                                        if(fi != "" && ff != ""){
                                            if((datos[i][12]=="Especial") && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                var marker = new google.maps.Marker({
                                                    position: position,
                                                    map: map,
                                                    icon: 'static/iconos/IconoGoogle.png',
                                                });
                                                google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                    return function() {
                                                        infowindow.setContent(
                                                            '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                '<TR>'+
                                                                     '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                     +'<div align="center">'
                                                                        +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                     +'</div>'
                                                                     +'</td>'+
                                                                '</TR>'+
                                                            '</TABLE>'
                                                        );
                                                        infowindow.setOptions({maxWidth: 200});
                                                        infowindow.open(map, marker);
                                                    }
                                                }) (marker, i));
                                                Markers[datos[i][7]] = marker;
                                            }
                                        }else{
                                            if((datos[i][12]=="Especial")){
                                                var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                var marker = new google.maps.Marker({
                                                    position: position,
                                                    map: map,
                                                    icon: 'static/iconos/IconoGoogle.png',
                                                });
                                                google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                    return function() {
                                                        infowindow.setContent(
                                                            '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                '<TR>'+
                                                                     '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                     +'<div align="center">'
                                                                        +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                     +'</div>'
                                                                     +'</td>'+
                                                                '</TR>'+
                                                            '</TABLE>'
                                                        );
                                                        infowindow.setOptions({maxWidth: 200});
                                                        infowindow.open(map, marker);
                                                    }
                                                }) (marker, i));
                                                Markers[datos[i][7]] = marker;
                                            }
                                        }
                                    }
                                }
                                if(ci1 == false && ci2 == false && ci3){
                                    if(estado.options[estado.selectedIndex].innerText != ""){
                                        if(fi != "" && ff != ""){
                                            if((datos[i][12]=="Uninominal/Especial") && es==datos[i][10] && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                var marker = new google.maps.Marker({
                                                    position: position,
                                                    map: map,
                                                    icon: 'static/iconos/IconoGoogle.png',
                                                });
                                                google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                    return function() {
                                                        infowindow.setContent(
                                                            '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                '<TR>'+
                                                                     '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                     +'<div align="center">'
                                                                        +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                     +'</div>'
                                                                     +'</td>'+
                                                                '</TR>'+
                                                            '</TABLE>'
                                                        );
                                                        infowindow.setOptions({maxWidth: 200});
                                                        infowindow.open(map, marker);
                                                    }
                                                }) (marker, i));
                                                Markers[datos[i][7]] = marker;
                                            }
                                        }else{
                                            if((datos[i][12]=="Uninominal/Especial") && es==datos[i][10]){
                                                var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                var marker = new google.maps.Marker({
                                                    position: position,
                                                    map: map,
                                                    icon: 'static/iconos/IconoGoogle.png',
                                                });
                                                google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                    return function() {
                                                        infowindow.setContent(
                                                            '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                '<TR>'+
                                                                     '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                     +'<div align="center">'
                                                                        +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                     +'</div>'
                                                                     +'</td>'+
                                                                '</TR>'+
                                                            '</TABLE>'
                                                        );
                                                        infowindow.setOptions({maxWidth: 200});
                                                        infowindow.open(map, marker);
                                                    }
                                                }) (marker, i));
                                                Markers[datos[i][7]] = marker;
                                            }
                                        }
                                    }else{
                                        if(fi != "" && ff != ""){
                                            if((datos[i][12]=="Uninominal/Especial") && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                var marker = new google.maps.Marker({
                                                    position: position,
                                                    map: map,
                                                    icon: 'static/iconos/IconoGoogle.png',
                                                });
                                                google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                    return function() {
                                                        infowindow.setContent(
                                                            '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                '<TR>'+
                                                                     '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                     +'<div align="center">'
                                                                        +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                     +'</div>'
                                                                     +'</td>'+
                                                                '</TR>'+
                                                            '</TABLE>'
                                                        );
                                                        infowindow.setOptions({maxWidth: 200});
                                                        infowindow.open(map, marker);
                                                    }
                                                }) (marker, i));
                                                Markers[datos[i][7]] = marker;
                                            }
                                        }else{
                                            if((datos[i][12]=="Uninominal/Especial")){
                                                var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                var marker = new google.maps.Marker({
                                                    position: position,
                                                    map: map,
                                                    icon: 'static/iconos/IconoGoogle.png',
                                                });
                                                google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                    return function() {
                                                        infowindow.setContent(
                                                            '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                '<TR>'+
                                                                     '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                     +'<div align="center">'
                                                                        +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                     +'</div>'
                                                                     +'</td>'+
                                                                '</TR>'+
                                                            '</TABLE>'
                                                        );
                                                        infowindow.setOptions({maxWidth: 200});
                                                        infowindow.open(map, marker);
                                                    }
                                                }) (marker, i));
                                                Markers[datos[i][7]] = marker;
                                            }
                                        }
                                    }
                                }
                                if(ci1 == false && ci2 == false && ci3 == false){
                                    if(estado.options[estado.selectedIndex].innerText != ""){
                                        if(fi != "" && ff != ""){
                                            if(es==datos[i][10] && (datos[i][11]>=fi && datos[i][11]<=ff)){
                                                var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                var marker = new google.maps.Marker({
                                                    position: position,
                                                    map: map,
                                                    icon: 'static/iconos/IconoGoogle.png',
                                                });
                                                google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                    return function() {
                                                        infowindow.setContent(
                                                            '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                '<TR>'+
                                                                     '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                     +'<div align="center">'
                                                                        +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                     +'</div>'
                                                                     +'</td>'+
                                                                '</TR>'+
                                                            '</TABLE>'
                                                        );
                                                        infowindow.setOptions({maxWidth: 200});
                                                        infowindow.open(map, marker);
                                                    }
                                                }) (marker, i));
                                                Markers[datos[i][7]] = marker;
                                            }
                                        }else{
                                            if(es==datos[i][10]){
                                                var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                var marker = new google.maps.Marker({
                                                    position: position,
                                                    map: map,
                                                    icon: 'static/iconos/IconoGoogle.png',
                                                });
                                                google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                    return function() {
                                                        infowindow.setContent(
                                                            '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                '<TR>'+
                                                                     '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                     +'<div align="center">'
                                                                        +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                     +'</div>'
                                                                     +'</td>'+
                                                                '</TR>'+
                                                            '</TABLE>'
                                                        );
                                                        infowindow.setOptions({maxWidth: 200});
                                                        infowindow.open(map, marker);
                                                    }
                                                }) (marker, i));
                                                Markers[datos[i][7]] = marker;
                                            }
                                        }
                                    }else{
                                        if(fi != "" && ff != ""){
                                            if((datos[i][11]>=fi && datos[i][11]<=ff)){
                                                var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                                var marker = new google.maps.Marker({
                                                    position: position,
                                                    map: map,
                                                    icon: 'static/iconos/IconoGoogle.png',
                                                });
                                                google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                    return function() {
                                                        infowindow.setContent(
                                                            '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                                '<TR>'+
                                                                     '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                     +'<div align="center">'
                                                                        +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                        +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                     +'</div>'
                                                                     +'</td>'+
                                                                '</TR>'+
                                                            '</TABLE>'
                                                        );
                                                        infowindow.setOptions({maxWidth: 200});
                                                        infowindow.open(map, marker);
                                                    }
                                                }) (marker, i));
                                                Markers[datos[i][7]] = marker;
                                            }
                                        }else{
                                            var position = new google.maps.LatLng(datos[i][8], datos[i][9]);                        
                                            var marker = new google.maps.Marker({
                                                position: position,
                                                map: map,
                                                icon: 'static/iconos/IconoGoogle.png',
                                            });
                                            google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                                return function() {
                                                    infowindow.setContent(
                                                        '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                                            '<TR>'+
                                                                 '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                                 +'<div align="center">'
                                                                    +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'ASIENTO'+'</span>'+'</strong>'+'<br>'
                                                                    +'<span style="color: #B82202; font-size: 10px;">'+'Nombre.:'+'</span>'+'<span>'+datos[i][7]+'</span>'+'<br>'
                                                                    +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][8]+', '+datos[i][9]+'</span>'+'<br>'
                                                                    +'<span style="color: #B82202; font-size: 10px;">'+'Tipo Circunscripción.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                                    +'<span style="color: #B82202; font-size: 10px;">'+'Fecha Registro.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                                 +'</div>'
                                                                 +'</td>'+
                                                            '</TR>'+
                                                        '</TABLE>'
                                                    );
                                                    infowindow.setOptions({maxWidth: 200});
                                                    infowindow.open(map, marker);
                                                }
                                            }) (marker, i));
                                            Markers[datos[i][7]] = marker;
                                        }
                                    }
                                }
                            } 
                        }
                    }
                    locate(0);
                }
                function locate(marker_id) {
                    var myMarker = Markers[marker_id];
                    var markerPosition = myMarker.getPosition();
                    map.setCenter(markerPosition);
                    google.maps.event.trigger(myMarker, 'click');
                }
                google.maps.event.addDomListener(window, 'load', initialize(datos)); //buildMap
            });
    };
    funcion();
} 

function funcion(){
    return('4');
}



