// Para visor en asientos/recintos a partir de coordenadas
// -ric
function getgeoext(event) {
    var x = event.keyCode;
    //alert(x)
    if (x == 27 || x == 9 || 'undefined') {          
        buildMap($('input[name="latitud"]').val(),   $('input[name="longitud"]').val());
    };
} //getgeo


function getgeoesp(event) {
    var x = event.keyCode;
    //alert(x)
    var ban=0;
    if (x == 27 || x == 9 || 'undefined') {
            $.getJSON('/get_geo_esp', {
                latitud: $('input[name="latitud"]').val(),
                longitud: $('input[name="longitud"]').val()
            }, function(data) {
                document.getElementById("ideploc").setAttribute("value", data.dep)
                document.getElementById("idepartamento").setAttribute("value", data.departamento)
                document.getElementById("iprovloc").setAttribute("value", data.prov)
                document.getElementById("iprovincia").setAttribute("value", data.provincia)
                document.getElementById("isecloc").setAttribute("value", data.sec)
                document.getElementById("imunicipio").setAttribute("value", data.municipio)
                //document.getElementById("icircun").setAttribute("value", data.dep);
                //document.getElementById("icircun").setAttribute("value", circun(3));
                switch(data.dep){
                    case 2:{
                        document.getElementById("icircun").setAttribute("value", '1');
                        $('#icircun').css('color', 'black');
                    }
                    break;
                    case 3:{
                        document.getElementById("icircun").setAttribute("value", '2');
                        $('#icircun').css('color', 'black');   
                    }
                    break;
                    case 4:{
                        document.getElementById("icircun").setAttribute("value", '3');
                        $('#icircun').css('color', 'black');   
                    }
                    break;
                    case 6:{
                        document.getElementById("icircun").setAttribute("value", '4');
                        $('#icircun').css('color', 'black');   
                    }
                    break;
                    case 7:{
                        document.getElementById("icircun").setAttribute("value", '5');   
                    }
                    break;
                    case 8:{
                        document.getElementById("icircun").setAttribute("value", '6');
                        $('#icircun').css('color', 'black');  
                    }
                    break;
                    case 9:{
                        document.getElementById("icircun").setAttribute("value", '7');
                        $('#icircun').css('color', 'black');  
                    }
                    break;
                    default:{ 
                        document.getElementById("icircun").setAttribute("value", 'No Hay');
                        $('#icircun').css('color', 'red');
                    } 
                    break;
                }
            });
        buildMap($('input[name="latitud"]').val(),   $('input[name="longitud"]').val());
    };
} //getgeo


function getgeo(event) {
    var x = event.keyCode;
    //alert(x)
    if (x == 27 || x == 9 || 'undefined') {
            $.getJSON('/get_geo', {
                latitud: $('input[name="latitud"]').val(),
                longitud: $('input[name="longitud"]').val()
            }, function(data) {
                document.getElementById("ideploc").setAttribute("value", data.dep)
                document.getElementById("idepartamento").setAttribute("value", data.departamento)
                document.getElementById("iprovloc").setAttribute("value", data.prov)
                document.getElementById("iprovincia").setAttribute("value", data.provincia)
                document.getElementById("isecloc").setAttribute("value", data.sec)
                document.getElementById("imunicipio").setAttribute("value", data.municipio)
                document.getElementById("icircun").setAttribute("value", data.nrocircun)
            });
          
        buildMap($('input[name="latitud"]').val(),   $('input[name="longitud"]').val());
    };
} //getgeo

function getgeoespecial(event) {
    var x = event.keyCode;
    //alert(x)
    if (x == 27 || x == 9 || 'undefined') {
            $.getJSON('/get_geo', {
                latitud: $('input[name="latitud"]').val(),
                longitud: $('input[name="longitud"]').val()
            }, function(data) {
                document.getElementById("ideploc").setAttribute("value", data.dep)
                document.getElementById("idepto").setAttribute("value", data.departamento)
                document.getElementById("iprovloc").setAttribute("value", data.prov)
                document.getElementById("iprovi").setAttribute("value", data.provincia)
                document.getElementById("isecloc").setAttribute("value", data.sec)
                document.getElementById("imuni").setAttribute("value", data.municipio)
                document.getElementById("icircun").setAttribute("value", data.nrocircun)
            });
        var select=document.getElementById("idepartamento");
        // obtenemos el valor a buscar
        var buscar=document.getElementById("idepto").value;
        // recorremos todos los valores del select
        for(var i=1;i<select.length;i++)
        {
            if(select.options[i].text.trim() === buscar.trim()){
                select.selectedIndex=i;
            }
        }  
        var dep=document.getElementById("ideploc").value;
        var prov=document.getElementById("iprovloc").value;
        $('#iprovincia').html('');
        $('#imunicipio').html('');
        $.getJSON("/get_provespeciales_all1", {
            dep: dep,
            prov: prov
        }, function(datos){
            $("#iprovincia").append('<option></option>');                
            $.each(datos, function(index, obj){
                if(obj[1]==prov){
                    $("#iprovincia").append('<option value="' + obj[1] + '" selected>' + obj[2] + '</option>');
                }else{
                    $("#iprovincia").append('<option value="' + obj[1] + '">' + obj[2] + '</option>');
                }           
            });
        });

        var muni=document.getElementById("isecloc").value;
        $('#imunicipio').html('');
        $.getJSON("/get_muniespeciales_all1", {
            dep: dep,
            prov: prov,
            muni: muni
        }, function(datos1){
            console.log(datos1);
            $("#imunicipio").append('<option></option>');                
            $.each(datos1, function(index1, obj1){
                if(obj1[2]==muni){
                    $("#imunicipio").append('<option value="' + obj1[2] + '" selected>' + obj1[3] + '</option>');
                }else{
                    $("#imunicipio").append('<option value="' + obj1[2] + '">' + obj1[3] + '</option>');
                }           
            });
        });

        buildMap($('input[name="latitud"]').val(),   $('input[name="longitud"]').val());
    };
} 

function buildMap(lat,lon)  {
    document.getElementById('dmap').innerHTML = "<div id='map' style='width: 100%; height: 100%;'></div>";

        var osmUrl = 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
            osmAttrib = 'only osmAttrib',
            landUrl = 'http://{s}.tile.thunderforest.com/landscape/{z}/{x}/{y}.png',
            thunAttrib = 'only Attrib',
            googleSatUrl = 'https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
            googleMapUrl = 'https://mt1.google.com/vt/lyrs=r&x={x}&y={y}&z={z}',
            mbUrl = 'https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibzJicGlja2luIiwiYSI6ImNpbXUyMzNldTAyNTF1cmtrZXdnbWZycDIifQ.JdYE50MBxDn1fdZtVFYXZw';

        var osmMap = L.tileLayer(osmUrl, {attribution: ''}),
            landMap = L.tileLayer(landUrl, {attribution: ''}),
            googleSat = L.tileLayer(googleSatUrl, {Attribution: 'gsat'}),
            googleMap = L.tileLayer(googleMapUrl, {Attribution: 'gmap'}),
            mbStreet = L.tileLayer(mbUrl, {id: 'mapbox.streets', attribution: 'mbSat'}), 
            mbSat = L.tileLayer(mbUrl, {id: 'mapbox.satellite', attribution: 'mbSat'}) ;

        var map = L.map('map', {
			    layers: [googleSat] // only add one!
		    })
		    .setView([lat, lon], 15);

		var baseLayers = {
			"OSM Mapnik": osmMap,
			"Landscape": landMap,
			"Google Satellite": googleSat,
            "Google Map": googleMap,
            "MapBox Satellite": mbSat,
            "MapBox Streets": mbStreet
		};


		L.control.layers(baseLayers).addTo(map);

    // to marker --
        //iconUrl: "https://unpkg.com/leaflet@1.5.1/dist/images/marker-icon.png",
        //shadowUrl: "https://unpkg.com/leaflet@1.5.1/dist/images/marker-shadow.png"
    const markerIcon = L.icon({
        iconSize: [25, 41],
        iconAnchor: [10, 41],
        popupAnchor: [2, -40],
        // specify the path here
        iconUrl:   "../../static/css/leaflet1.5.1/images/marker-icon.png",
        shadowUrl: "../../static/css/leaflet1.5.1/images/marker-shadow.png"
    });

    L.marker([lat, lon],
        {
            title: "Asiento",
            opacity: 0.8,
            icon: markerIcon
        }
    ).addTo(map);

    L.circle([lat, lon], {
            color: 'red',
            fillColor: '#f03',
            fillOpacity: 0.06,
            radius: 500
        }).addTo(map);
} //buildMap


function buildMapCoordIni(lat,lon)  {

  $.getJSON('/get_json_ptos', {
      latitud: $('input[name="latitud"]').val(),
      longitud: $('input[name="longitud"]').val()
  }, function(data) {
    /*
      document.getElementById("idepartamento").setAttribute("value", data.gj_ptos)
    */
    alert(data.gj_ptos.name);
  });
}

//--------------------------------------------------------------------------------------------

// ---------------------------------------------------------was  viewmap.js
    // Set style function that sets fill color property
    function style(feature) {
        return {
            fillColor: 'green', 
            fillOpacity: 0.5,  
            weight: 2,
            opacity: 1,
            color: '#ffffff',
            dashArray: '3'
        };
    }

    function styleProv(feature) {
        return {
            fillColor: 'orange', 
            fillOpacity: 0.5,  
            weight: 2,
            opacity: 1,
            color: '#ffffff',
            dashArray: '3'
        };
    }

    function styleCir(feature) {
        return {
            fillColor: 'gray', 
            fillOpacity: 0.5,  
            weight: 2,
            opacity: 1,
            color: 'red',
            dashArray: '3'
        };
    }


    var highlight = {
      'fillColor': 'yellow',
      'weight': 2,
      'opacity': 2
    };
    

    var highlightCir = {
      'fillColor': '#a3c2c2',
      'weight': 2,
      'opacity': 2
    };


    function forEachFeature(feature, layer) {
        var popupContent = "<p><b>ID: </b>"+ feature.properties.id +
            "</br>LOCALIDAD: "+ feature.properties.nom_localidad + '</p>';

        layer.bindPopup(popupContent);

        layer.on("click", function (e) { 
            locLayer.setStyle(style); //resets layer colors
            layer.setStyle(highlight);  //highlights selected.
        }); 
    }


    function forEachFeatureReci(feature, layer) {
      var popupContent = "<p><b><span style='color:blue'>Recinto: </b></span>" + '<b><big>' + feature.properties.recinto + '</big></b>' +
            "</br><b><span style='color:blue'>Idloc/Reci: </b></span>"+ feature.properties.idlocreci + 
            "</br><b><span style='color:blue'>Dep/Prov/Municipio: </b></span>"+ feature.properties.dpm + 
            "</br><b><span style='color:blue'>Cod. Dep/Prov/Municipio: </b></span>"+ feature.properties.cod + 
            "</br><b><span style='color:blue'>Circunscripción: </b></span>"+ feature.properties.circun + 
            "</br><b><span style='color:blue'>Zona: </b></span>"+ feature.properties.zona + 
            "</br><b><span style='color:blue'>Dirección:  </b></span>"+ feature.properties.direccion + 
            '</p>';

        layer.bindPopup(popupContent);

        layer.on("click", function (e) { 
            reciLayer.setStyle(style); //resets layer colors
            reciLayer.setStyle(highlight);  //highlights selected.
        }); 
    }


    function forEachFeatureAsi(feature, layer) {
        var popupContent = "<p><b><span style='color:blue'>Asiento: </b></span>" + feature.properties.asiento +
            "</br><b><span style='color:blue'>Idloc: </b></span>"+ feature.properties.idloc + 
            "</br><b><span style='color:blue'>Dep/Prov/Municipio: </b></span>"+ feature.properties.dpm + 
            "</br><b><span style='color:blue'>Cod. Dep/Prov/Municipio: </b></span>"+ feature.properties.cod + 
            "</br><b><span style='color:blue'>Tipo Circunscripción: </b></span>"+ feature.properties.tipo_circun + 
            '</p>';

        layer.bindPopup(popupContent);

        layer.on("click", function (e) { 
            reciLayer.setStyle(style); //resets layer colors
            reciLayer.setStyle(highlight);  //highlights selected.
        }); 
    }


    function forEachFeatureMun(feature, layer) {
        var popupContent = "<p><b><span style='color:blue'>Cod.: </span></b>"+ feature.properties.cod +
          "</br><b><span style='color:blue'>Municipio: </span></b>"+ feature.properties.municipio + '</p>';

        layer.bindPopup(popupContent);

        layer.on("click", function (e) { 
            munLayer.setStyle(style); //resets layer colors
            layer.setStyle(highlight);  //highlights selected.
        }); 
    }
      

    function forEachFeatureProv(feature, layer) {
        var popupContent = "<p><b><span style='color:blue'>Cod.: </span></b>"+ feature.properties.cod +
          "</br><b><span style='color:blue'>Provincia: </span></b>"+ feature.properties.provincia + '</p>';

        layer.bindPopup(popupContent);

        layer.on("click", function (e) { 
            provLayer.setStyle(styleProv); //resets layer colors
            layer.setStyle(highlight);  //highlights selected.
        }); 
    }


    function forEachFeatureCir(feature, layer) {
        var popupContent = "<p><b>Circunscripción: </b>"+ feature.properties.circun + "</p";

        layer.bindPopup(popupContent);

        layer.on("click", function (e) { 
            cirLayer.setStyle(styleCir); //resets layer colors
            layer.setStyle(highlightCir);  //highlights selected.
        }); 
    }


    function markerOnClick(e)
    {
      var coord = e.latlng.toString().split(',');
      var lat = coord[0].split('(');
      var lng = coord[1].split(')');
      marker.bindPopup('Latitud:: ' + lat[1] + '  Longitud: ' + lng[0]);
    }


// invoked ---------------------------------------------cfg/view/coord in  map--------------------------
function viewMap() {
    document.getElementById('dmap').innerHTML = "<div id='map' style='width: 100%; height: 100%;'></div>";

    // add markerClusterGroup
    var markersMCG = L.markerClusterGroup();


    //tmp--var locLayer = L.geoJson( {{ geo_json | safe }}, {onEachFeature: forEachFeature, style: style});

    /*
    // reciLayer
    var iconReci = L.icon({
      iconUrl: '../static/iconos/icons8-map-pin-40.png',
      iconSize: [35, 35]
    });

    var reciLayer = L.geoJson( {{ gj_reci | safe }}, {
      pointToLayer: function (feature, latlng) {
        var lm = L.marker(latlng, {icon: iconReci});
        markersMCG.addLayer(lm);
        return lm;
    },
      onEachFeature: forEachFeatureReci, style: style
    });


    // asiLayer
    var iconAsi = L.icon({
      iconUrl: '../static/iconos/icons8-map-pin-40-red.png',
      iconSize: [35, 35]
    });

    var asiLayer = L.geoJson( {{ gj_asi | safe }}, {
      pointToLayer: function (feature, latlng) {
        var lma = L.marker(latlng, {icon: iconAsi});
        return lma;
    },
      onEachFeature: forEachFeatureAsi, style: style
    });
    */

    var provLayer = L.geoJson( {{ gj_prov | safe }}, {onEachFeature: forEachFeatureProv, style: styleProv});
    var provLayer = L.geoJson( {{ gj_prov | safe }}, {onEachFeature: forEachFeatureProv, style: styleProv});
    var cirLayer = L.geoJson( {{ gj_cir | safe }}, {onEachFeature: forEachFeatureCir, style: styleCir});


    // baseMaps - overlayMaps

    var osmUrl = 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
        osmAttrib = 'Map data &copy; OpenStreetMap contributors',
        landUrl = 'http://{s}.tile.thunderforest.com/landscape/{z}/{x}/{y}.png',
        thunAttrib = 'only Attrib',
        googleSatUrl = 'https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
        googleMapUrl = 'https://mt1.google.com/vt/lyrs=r&x={x}&y={y}&z={z}',
        mbUrl = 'https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibzJicGlja2luIiwiYSI6ImNpbXUyMzNldTAyNTF1cmtrZXdnbWZycDIifQ.JdYE50MBxDn1fdZtVFYXZw',
        topoUrl = 'https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png',
        topoAttrib = 'Kartendaten: &copy; <a href="https://openstreetmap.org/copyright">OpenStreetMap</a>-Mitwirkende, <a href="http://viewfinderpanoramas.org">SRTM</a> | Kartendarstellung: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)';

    var osmMap = L.tileLayer(osmUrl, {attribution: osmAttrib}),
        landMap = L.tileLayer(landUrl, {attribution: ''}),
        googleSat = L.tileLayer(googleSatUrl, {Attribution: 'gsat'}),
        googleMap = L.tileLayer(googleMapUrl, {Attribution: 'gmap'}),
        mbSat = L.tileLayer(mbUrl, {id: 'mapbox.satellite', attribution: 'mbSat'}) ;
        topoMap = new L.TileLayer(topoUrl, {minZoom: 1, maxZoom: 17, detectRetina: false, attribution: topoAttrib});

    var BING_KEY = 'AuhiCJHlGzhg93IqUH_oCpl_-ZUrIE6SPftlyGYUvr9Amx5nzA-WqGcPquyFZl4L';
    var bingSat = L.tileLayer.bing(BING_KEY);
    var esriStreets = L.esri.basemapLayer('Streets');
    var esriImagery = L.esri.basemapLayer('Imagery');

    var tokenMapBox = 'pk.eyJ1IjoibWJ1Z2xlMjAyMSIsImEiOiJja3FpOHd4cjMyYmR0MnpuMHZrajF5c3pxIn0.2gFzBGWekEI59pMl0EflSw';
    var mapboxUrl = 'https://api.mapbox.com/styles/v1/mapbox/streets-v10/tiles/{z}/{x}/{y}@2x?access_token=' + tokenMapBox;
    var mapboxAttrib = 'Map data © <a href="http://osm.org/copyright">OpenStreetMap</a> contributors. Tiles from <a href="https://www.mapbox.com">Mapbox</a>.';
    var mapboxStreets = new L.TileLayer(mapboxUrl, {
      attribution: mapboxAttrib,
      tileSize: 512,
      zoomOffset: -1
    });

    var baseLayers = {
      "Open Street Map": osmMap,
      "Google Satellite": googleSat,
      "Google Streets": googleMap,
      "MapBox Satellite": mbSat,
      "MapBox Streets": mapboxStreets,
      "Esri Streets": esriStreets,
      "Esri Imagery": esriImagery,
      "Bing Satellite": bingSat,
      "Landscape": landMap,
      "Open TopoMap": topoMap
    };
/*
      "Recintos Electorales":reciLayer,
      "Cluster-Recintos Elect.":markersMCG,
      "Asientos Electorales":asiLayer,
      */      
    var overlayMaps = {
      "Circunscripciones":cirLayer,
      "Municipios":munLayer,
      "Provincias":provLayer
    };	
      

    // Set up map

    var mapCenter = [-17.05678, -64.81934];
    var map = L.map('map', {
      defaultExtentControl: true,
      center: mapCenter,
      zoom: 6,
      layers: [mapboxStreets] // only add one!
    });

    //Add layer control
    L.control.layers(baseLayers, overlayMaps).addTo(map);

    // Add defaultExtent
    //L.control.defaultExtent().addTo(map);


    // add others controls 
    map.addControl(new L.Control.Fullscreen());

    map.addControl(new L.Control.LinearMeasurement({
      unitSystem: 'metric',
      color: '#FF6600'
    }))

    L.control.locate({
      strings: {title: "Ver donde estoy.."}
    }).addTo(map);

    //----- Add the Street View buttons in the bottom left corner -----
    // (Please get your own Client ID on https://www.mapillary.com/app/settings/developers)
    var iconStreet = L.icon({
        iconUrl: '../static/iconos/icons8-street-view-52.png',
        iconSize: [52, 52]
        })
    var marker_gsv = L.marker(map.getCenter(), {icon:iconStreet});
    map.on('move', function() { marker_gsv.setLatLng(map.getCenter()); });


    //----- Add easyButton gsv - StreetView-----
    var sw_marker_gsv = 0;
    var gsvPopup = L.popup().setContent('<u><i>Servicio</i></u>: <b>Google Street View (GSV)</b> \
            y otros Habilitado. Ubique posición y presione click en opciones  \
            (ubicado en la parte inferior/izquierda) ');

    L.easyButton('<img src="../static/iconos/icons8-street-view-26.png" style="width:23px">', function(btn, map){
      if (sw_marker_gsv == 0) {
         sv = L.streetView({ position: 'bottomleft', mapillaryId: 'RC1ZRTBfaVlhWmJmUGVqRk5CYnAxQTpmMGE3OTU0MzM0MTljZTA4' }).addTo(map);
         gsvPopup.setLatLng(map.getCenter()).openOn(map);
         marker_gsv.addTo(map);
         sw_marker_gsv = 1;
         }
      else {
         sv.remove();
         map.removeLayer(marker_gsv);
         gsvPopup.removeFrom(map);
         sw_marker_gsv = 0;
         }
      },'Habilitar/Inhabilitar Google Street View (GSV)').addTo(map);
    // end Street View - easyButton


    L.control.coordinates({
      position:"bottomleft",
      decimals:5,
      decimalSeperator:",",
      lngFirst:true,
      labelTemplateLat:"<b>Latitud:</b> {y}",
      labelTemplateLng:"<b>Longitud:</b> {x}",
      useLatLngOrder: true
    }).addTo(map);


    map.addControl( new L.Control.Search({
      url: 'https://nominatim.openstreetmap.org/search?format=json&accept-language=de-DE&q={s}',
      jsonpParam: 'json_callback',
      propertyName: 'display_name',
      propertyLoc: ['lat','lon'],
      markerLocation: true,
      autoType: false,
      autoCollapse: true,
      minLength: 2,
      zoom:16,
      text: 'Buscar dirección ó lat long',
      textCancel: 'Cancelar',
      textErr: 'No encontrado... ',
      position: 'topleft'
    }) );
    //marker: L.circleMarker([0,0],{radius:30}),

  //L.control.locate({showCompass:true,icon:"fa fa-crosshairs"}).addTo(map);


  // to munLayer Search
    var searchControlMun = new L.Control.Search({
      layer: munLayer,
      propertyName: 'municipio',
      zoom:9,
      circleLocation: false,
      text: 'Municipio a buscar',
      textCancel: 'Cancelar',
      textErr: 'Municipio NO encontrado... ',
      position: 'topright'
    });

      searchControlMun.on('search_locationfound', function(e) {
          e.layer.setStyle({fillcolor: 'red', color: '#0f0'});
          e.layer.setStyle(highlight);  //highlights selected.
      })
    map.addControl(searchControlMun);


    // to reciLayer Search
    var searchControlReci = new L.Control.Search({
      layer: reciLayer,
      propertyName: 'recinto',
      zoom:12,
      text: 'Recinto Electoral a buscar',
      textCancel: 'Cancelar',
      textErr: 'Recinto NO encontrado... ',
      position: 'topright'
    });
    map.addControl(searchControlReci);   // add control & checked locLayer


    //Plugin magic goes here! Note that you cannot use the same layer object again, as that will confuse the two map controls
    var osm2 = new L.TileLayer(osmUrl, {minZoom: 0, maxZoom: 13, attribution: osmAttrib });

    var rect1 = {color: "#ff1100", weight: 3};
    var rect2 = {color: "#0000AA", weight: 1, opacity:0, fillOpacity:0};
    var miniMap = new L.Control.MiniMap(osm2, { toggleDisplay: true, aimingRectOptions : rect1, shadowRectOptions: rect2}).addTo(map);


    // add marker & popup with coord
    var marker = L.marker([0,0]);

    map.on('contextmenu',
      function mapContextmenuListen(e) {
        var pos = e.latlng;
        marker = L.marker(
          pos, {
            draggable: true
          }
        );
        marker.on('dragstart', function(e) {
          map.off('contextmenu', mapContextmenuListen);
        });

        marker.on('dragend', function(event) {
          var position = marker.getLatLng();
          marker.setLatLng(position, {
            draggable: 'true'
          }).bindPopup(position).update();

          setTimeout(function() {
            map.on('contextmenu', mapContextmenuListen);
          }, 10);
        });

        //marker.addTo(map);
        map.addLayer(marker);
        marker.on('click', markerOnClick);
      }
    );
}
