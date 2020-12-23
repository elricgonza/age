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
                        if(dpto.options[dpto.selectedIndex].innerText != ""){ 
                            console.log(1);
                            if(provincia.options[provincia.selectedIndex].innerText != ""){
                                if(municipio.options[municipio.selectedIndex].innerText != ""){
                                    if(document.getElementById("icir1").checked){
                                        if(estado.options[estado.selectedIndex].innerText != ""){
                                            if(fi != "" && ff != ""){
                                                if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && ci1 && es==datos[i][10] && (datos[i][11]>=fi && datos[i][11]<=ff)){
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
                                                if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && ci1 && es==datos[i][10]){
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
                                                if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && ci1 && (datos[i][11]>=fi && datos[i][11]<=ff)){
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
                                                if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && ci1){
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
                                    if(document.getElementById("icir2").checked){
                                        if(estado.options[estado.selectedIndex].innerText != ""){
                                            if(fi != "" && ff != ""){
                                                if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && ci2 && es==datos[i][10] && (datos[i][11]>=fi && datos[i][11]<=ff)){
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
                                                if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && ci2 && es==datos[i][10]){
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
                                                if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && ci2 && (datos[i][11]>=fi && datos[i][11]<=ff)){
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
                                                if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && ci2){
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
                                    if(document.getElementById("icir3").checked){
                                        if(estado.options[estado.selectedIndex].innerText != ""){
                                            if(fi != "" && ff != ""){
                                                if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && ci3 && es==datos[i][10] && (datos[i][11]>=fi && datos[i][11]<=ff)){
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
                                                if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && ci3 && es==datos[i][10]){
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
                                                if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && ci3 && (datos[i][11]>=fi && datos[i][11]<=ff)){
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
                                                if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && ci3){
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
                                }else{//no municipio
                                    if(document.getElementById("icir1").checked){
                                        if(estado.options[estado.selectedIndex].innerText != ""){
                                            if(fi != "" && ff != ""){
                                                if(dp==datos[i][1] && pr==datos[i][3] && ci1 && es==datos[i][10] && (datos[i][11]>=fi && datos[i][11]<=ff)){
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
                                                if(dp==datos[i][1] && pr==datos[i][3] && ci1 && es==datos[i][10]){
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
                                        }else{//no estado
                                            if(fi != "" && ff != ""){
                                                if(dp==datos[i][1] && pr==datos[i][3] && ci1 && (datos[i][11]>=fi && datos[i][11]<=ff)){
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
                                            }else{//no fecha
                                                if(dp==datos[i][1] && pr==datos[i][3] && ci1){
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
                                    if(document.getElementById("icir2").checked){
                                        if(estado.options[estado.selectedIndex].innerText != ""){
                                            if(fi != "" && ff != ""){
                                                if(dp==datos[i][1] && pr==datos[i][3] && ci2 && es==datos[i][10] && (datos[i][11]>=fi && datos[i][11]<=ff)){
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
                                                if(dp==datos[i][1] && pr==datos[i][3] && ci2 && es==datos[i][10]){
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
                                        }else{//no estado
                                            if(fi != "" && ff != ""){
                                                if(dp==datos[i][1] && pr==datos[i][3] && ci2 && (datos[i][11]>=fi && datos[i][11]<=ff)){
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
                                            }else{//no fecha
                                                if(dp==datos[i][1] && pr==datos[i][3] && ci2){
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
                                    if(document.getElementById("icir3").checked){
                                        if(estado.options[estado.selectedIndex].innerText != ""){
                                            if(fi != "" && ff != ""){
                                                if(dp==datos[i][1] && pr==datos[i][3] && ci3 && es==datos[i][10] && (datos[i][11]>=fi && datos[i][11]<=ff)){
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
                                                if(dp==datos[i][1] && pr==datos[i][3] && ci3 && es==datos[i][10]){
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
                                        }else{//no estado
                                            if(fi != "" && ff != ""){
                                                if(dp==datos[i][1] && pr==datos[i][3] && ci3 && (datos[i][11]>=fi && datos[i][11]<=ff)){
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
                                            }else{//no fecha
                                                if(dp==datos[i][1] && pr==datos[i][3] && ci3){
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
                            }else{//no provincia
                                console.log(2);
                                if(municipio.options[municipio.selectedIndex].innerText != ""){
                                    console.log(3);
                                    if(document.getElementById("icir1").checked){
                                        if(estado.options[estado.selectedIndex].innerText != ""){
                                            if(fi != "" && ff != ""){
                                                if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && ci1 && es==datos[i][10] && (datos[i][11]>=fi && datos[i][11]<=ff)){
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
                                                if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && ci1 && es==datos[i][10]){
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
                                                if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && ci1 && (datos[i][11]>=fi && datos[i][11]<=ff)){
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
                                                if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && ci1){
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
                                    if(document.getElementById("icir2").checked){
                                        if(estado.options[estado.selectedIndex].innerText != ""){
                                            if(fi != "" && ff != ""){
                                                if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && ci2 && es==datos[i][10] && (datos[i][11]>=fi && datos[i][11]<=ff)){
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
                                                if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && ci2 && es==datos[i][10]){
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
                                                if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && ci2 && (datos[i][11]>=fi && datos[i][11]<=ff)){
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
                                                if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && ci2){
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
                                    if(document.getElementById("icir3").checked){
                                        if(estado.options[estado.selectedIndex].innerText != ""){
                                            if(fi != "" && ff != ""){
                                                if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && ci3 && es==datos[i][10] && (datos[i][11]>=fi && datos[i][11]<=ff)){
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
                                                if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && ci3 && es==datos[i][10]){
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
                                                if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && ci3 && (datos[i][11]>=fi && datos[i][11]<=ff)){
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
                                                if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && ci3){
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
                                }else{//no municipio
                                    console.log(3);
                                    if(document.getElementById("icir1").checked){
                                        if(estado.options[estado.selectedIndex].innerText != ""){
                                            if(fi != "" && ff != ""){
                                                if(dp==datos[i][1] && ci1 && es==datos[i][10] && (datos[i][11]>=fi && datos[i][11]<=ff)){
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
                                                if(dp==datos[i][1] && ci1 && es==datos[i][10]){
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
                                        }else{//no estado
                                            if(fi != "" && ff != ""){
                                                if(dp==datos[i][1] && ci1 && (datos[i][11]>=fi && datos[i][11]<=ff)){
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
                                            }else{//no fecha
                                                if(dp==datos[i][1] && ci1){
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
                                    if(document.getElementById("icir2").checked){
                                        if(estado.options[estado.selectedIndex].innerText != ""){
                                            if(fi != "" && ff != ""){
                                                if(dp==datos[i][1] && ci2 && es==datos[i][10] && (datos[i][11]>=fi && datos[i][11]<=ff)){
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
                                                if(dp==datos[i][1] && ci2 && es==datos[i][10]){
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
                                        }else{//no estado
                                            if(fi != "" && ff != ""){
                                                if(dp==datos[i][1] && ci2 && (datos[i][11]>=fi && datos[i][11]<=ff)){
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
                                            }else{//no fecha
                                                if(dp==datos[i][1] && ci2){
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
                                    if(document.getElementById("icir3").checked){
                                        if(estado.options[estado.selectedIndex].innerText != ""){
                                            if(fi != "" && ff != ""){
                                                if(dp==datos[i][1] && ci3 && es==datos[i][10] && (datos[i][11]>=fi && datos[i][11]<=ff)){
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
                                                if(dp==datos[i][1] && ci3 && es==datos[i][10]){
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
                                        }else{//no estado
                                            if(fi != "" && ff != ""){
                                                if(dp==datos[i][1] && ci3 && (datos[i][11]>=fi && datos[i][11]<=ff)){
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
                                            }else{//no fecha
                                                if(dp==datos[i][1] && ci3){
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
                        }else{//no departamento
                            if(provincia.options[provincia.selectedIndex].innerText != ""){
                                if(municipio.options[municipio.selectedIndex].innerText != ""){
                                    if(document.getElementById("icir1").checked){
                                        if(estado.options[estado.selectedIndex].innerText != ""){
                                            if(fi != "" && ff != ""){
                                                if(ci1 && es==datos[i][10] && (datos[i][11]>=fi && datos[i][11]<=ff)){
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
                                                if(ci1 && es==datos[i][10]){
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
                                                if(ci1 && (datos[i][11]>=fi && datos[i][11]<=ff)){
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
                                                if(ci1){
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
                                    if(document.getElementById("icir2").checked){
                                        if(estado.options[estado.selectedIndex].innerText != ""){
                                            if(fi != "" && ff != ""){
                                                if(ci2 && es==datos[i][10] && (datos[i][11]>=fi && datos[i][11]<=ff)){
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
                                                if(ci2 && es==datos[i][10]){
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
                                                if(ci2 && (datos[i][11]>=fi && datos[i][11]<=ff)){
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
                                                if(ci2){
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
                                    if(document.getElementById("icir3").checked){
                                        if(estado.options[estado.selectedIndex].innerText != ""){
                                            if(fi != "" && ff != ""){
                                                if(ci3 && es==datos[i][10] && (datos[i][11]>=fi && datos[i][11]<=ff)){
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
                                                if(ci3 && es==datos[i][10]){
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
                                                if(ci3 && (datos[i][11]>=fi && datos[i][11]<=ff)){
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
                                                if(ci3){
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
                                }else{//no municipio
                                    if(document.getElementById("icir1").checked){
                                        if(estado.options[estado.selectedIndex].innerText != ""){
                                            if(fi != "" && ff != ""){
                                                if(dp==datos[i][1] && pr==datos[i][3] && ci1 && es==datos[i][10] && (datos[i][11]>=fi && datos[i][11]<=ff)){
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
                                                if(dp==datos[i][1] && pr==datos[i][3] && ci1 && es==datos[i][10]){
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
                                        }else{//no estado
                                            if(fi != "" && ff != ""){
                                                if(dp==datos[i][1] && pr==datos[i][3] && ci1 && (datos[i][11]>=fi && datos[i][11]<=ff)){
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
                                            }else{//no fecha
                                                if(dp==datos[i][1] && pr==datos[i][3] && ci1){
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
                                    if(document.getElementById("icir2").checked){
                                        if(estado.options[estado.selectedIndex].innerText != ""){
                                            if(fi != "" && ff != ""){
                                                if(dp==datos[i][1] && pr==datos[i][3] && ci2 && es==datos[i][10] && (datos[i][11]>=fi && datos[i][11]<=ff)){
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
                                                if(dp==datos[i][1] && pr==datos[i][3] && ci2 && es==datos[i][10]){
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
                                        }else{//no estado
                                            if(fi != "" && ff != ""){
                                                if(dp==datos[i][1] && pr==datos[i][3] && ci2 && (datos[i][11]>=fi && datos[i][11]<=ff)){
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
                                            }else{//no fecha
                                                if(dp==datos[i][1] && pr==datos[i][3] && ci2){
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
                                    if(document.getElementById("icir3").checked){
                                        if(estado.options[estado.selectedIndex].innerText != ""){
                                            if(fi != "" && ff != ""){
                                                if(dp==datos[i][1] && pr==datos[i][3] && ci3 && es==datos[i][10] && (datos[i][11]>=fi && datos[i][11]<=ff)){
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
                                                if(dp==datos[i][1] && pr==datos[i][3] && ci3 && es==datos[i][10]){
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
                                        }else{//no estado
                                            if(fi != "" && ff != ""){
                                                if(dp==datos[i][1] && pr==datos[i][3] && ci3 && (datos[i][11]>=fi && datos[i][11]<=ff)){
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
                                            }else{//no fecha
                                                if(dp==datos[i][1] && pr==datos[i][3] && ci3){
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
                            }else{//no provincia
                                if(municipio.options[municipio.selectedIndex].innerText != ""){
                                    if(document.getElementById("icir1").checked){
                                        if(estado.options[estado.selectedIndex].innerText != ""){
                                            if(fi != "" && ff != ""){
                                                if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && ci1 && es==datos[i][10] && (datos[i][11]>=fi && datos[i][11]<=ff)){
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
                                                if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && ci1 && es==datos[i][10]){
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
                                                if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && ci1 && (datos[i][11]>=fi && datos[i][11]<=ff)){
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
                                                if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && ci1){
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
                                    if(document.getElementById("icir2").checked){
                                        if(estado.options[estado.selectedIndex].innerText != ""){
                                            if(fi != "" && ff != ""){
                                                if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && ci2 && es==datos[i][10] && (datos[i][11]>=fi && datos[i][11]<=ff)){
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
                                                if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && ci2 && es==datos[i][10]){
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
                                                if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && ci2 && (datos[i][11]>=fi && datos[i][11]<=ff)){
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
                                                if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && ci2){
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
                                    if(document.getElementById("icir3").checked){
                                        if(estado.options[estado.selectedIndex].innerText != ""){
                                            if(fi != "" && ff != ""){
                                                if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && ci3 && es==datos[i][10] && (datos[i][11]>=fi && datos[i][11]<=ff)){
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
                                                if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && ci3 && es==datos[i][10]){
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
                                                if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && ci3 && (datos[i][11]>=fi && datos[i][11]<=ff)){
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
                                                if(dp==datos[i][1] && pr==datos[i][3] && mu==datos[i][5] && ci3){
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
                                }else{//no municipio
                                    if(document.getElementById("icir1").checked){
                                        if(estado.options[estado.selectedIndex].innerText != ""){
                                            if(fi != "" && ff != ""){
                                                if(ci1 && es==datos[i][10] && (datos[i][11]>=fi && datos[i][11]<=ff)){
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
                                                if(ci1 && es==datos[i][10]){
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
                                        }else{//no estado
                                            if(fi != "" && ff != ""){
                                                if(ci1 && (datos[i][11]>=fi && datos[i][11]<=ff)){
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
                                            }else{//no fecha
                                                if(ci1){
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
                                    if(document.getElementById("icir2").checked){
                                        if(estado.options[estado.selectedIndex].innerText != ""){
                                            if(fi != "" && ff != ""){
                                                if(ci2 && es==datos[i][10] && (datos[i][11]>=fi && datos[i][11]<=ff)){
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
                                                if(ci2 && es==datos[i][10]){
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
                                        }else{//no estado
                                            if(fi != "" && ff != ""){
                                                if(ci2 && (datos[i][11]>=fi && datos[i][11]<=ff)){
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
                                            }else{//no fecha
                                                if(ci2){
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
                                    if(document.getElementById("icir3").checked){
                                        if(estado.options[estado.selectedIndex].innerText != ""){
                                            if(fi != "" && ff != ""){
                                                if(ci3 && es==datos[i][10] && (datos[i][11]>=fi && datos[i][11]<=ff)){
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
                                                if(ci3 && es==datos[i][10]){
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
                                        }else{//no estado
                                            if(fi != "" && ff != ""){
                                                if(ci3 && (datos[i][11]>=fi && datos[i][11]<=ff)){
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
                                            }else{//no fecha
                                                if(ci3){
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



