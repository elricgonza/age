// Para visor en asientos/recintos a partir de coordenadas
// -ric
function gethomjurisdall(event) {
    var map;
    var Markers = {};
    var infowindow;
    var x = event.keyCode;
    var idhom;
    var j=1;
    if (x == 27 || x == 9 || 'undefined') {
            $.getJSON("/get_homjurisd_all", { idhom: $('input[name="idhom"]').val() }, function(datos){
                var origin = new google.maps.LatLng(datos[0][6], datos[0][7]);
                function initialize(datos) {
                    var mapOptions = {
                      zoom: 15,
                      center: origin,
                      mapTypeId: google.maps.MapTypeId.SATELLITE
                    };
                    map = new google.maps.Map(document.getElementById('map'), mapOptions);
                    infowindow = new google.maps.InfoWindow();
                    for(i=0; i<datos.length; i++) {
                        if(i == 0){
                            var position = new google.maps.LatLng(datos[i][6], datos[i][7]);                        
                            var marker = new google.maps.Marker({
                                position: position,
                                map: map,
                                icon: '/static/iconos/IconoGoogle.png',
                            });
                            google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                return function() {
                                    infowindow.setContent(
                                        '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                            '<TR>'+
                                                 '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                 +'<div align="center">'
                                                    +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'RECINTO'+'</span>'+'</strong>'+'<br>'
                                                    +'<span style="color: #B82202; font-size: 10px;">'+'IdLoc.:'+'</span>'+'<span>'+datos[i][1]+'</span>'+'<br>'
                                                    +'<span style="color: #B82202; font-size: 10px;">'+'Reci.:'+'</span>'+'<span>'+datos[i][2]+'</span>'+'<br>'
                                                    +'<span style="color: #B82202; font-size: 10px;">'+'Asiento.:'+'</span>'+'<span>'+datos[i][4]+'</span>'+'<br>'
                                                    +'<span style="color: #B82202; font-size: 10px;">'+'Recinto.:'+'</span>'+'<span>'+datos[i][5]+'</span>'+'<br>'
                                                    +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][6]+', '+datos[i][7]+'</span>'+'<br>'
                                                 +'</div>'
                                                 +'</td>'+
                                            '</TR>'+
                                        '</TABLE>'
                                    );
                                    infowindow.setOptions({maxWidth: 200});
                                    infowindow.open(map, marker);
                                }
                            }) (marker, i));
                            Markers[datos[i][4]] = marker;
                        }else{
                            var position = new google.maps.LatLng(datos[i][13], datos[i][14]);                        
                            var marker = new google.maps.Marker({
                                position: position,
                                map: map,
                                icon: '/static/iconos/IconoGoogle.png',
                            });
                            google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                return function() {
                                    infowindow.setContent(
                                        '<TABLE BORDER="4" BORDERCOLOR="#006666" CELLSPACING="0">'+
                                            '<TR>'+
                                                 '<td width="50%" height="50%" bgcolor="#CCCCCC">'
                                                 +'<div align="center">'
                                                    +'<strong>'+'<span style="color: #B82202; font-size: 12px;">'+'RECINTO'+'</span>'+'</strong>'+'<br>'
                                                    +'<span style="color: #B82202; font-size: 10px;">'+'IdLoc.:'+'</span>'+'<span>'+datos[i][8]+'</span>'+'<br>'
                                                    +'<span style="color: #B82202; font-size: 10px;">'+'Reci.:'+'</span>'+'<span>'+datos[i][9]+'</span>'+'<br>'
                                                    +'<span style="color: #B82202; font-size: 10px;">'+'Asiento.:'+'</span>'+'<span>'+datos[i][11]+'</span>'+'<br>'
                                                    +'<span style="color: #B82202; font-size: 10px;">'+'Recinto.:'+'</span>'+'<span>'+datos[i][12]+'</span>'+'<br>'
                                                    +'<span style="color: #B82202; font-size: 10px;">'+'Coord.(X,Y).:'+'</span>'+'<span>'+datos[i][13]+', '+datos[i][14]+'</span>'+'<br>'
                                                 +'</div>'
                                                 +'</td>'+
                                            '</TR>'+
                                        '</TABLE>'
                                    );
                                    infowindow.setOptions({maxWidth: 200});
                                    infowindow.open(map, marker);
                                }
                            }) (marker, i));
                            Markers[datos[i][4]] = marker;
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



