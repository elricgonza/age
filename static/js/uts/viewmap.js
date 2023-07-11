function viewMap(gj_mun, gj_prov, gj_cir) {
    document.getElementById('dmap').innerHTML = "<div id='map' style='width: 100%; height: 100%;'></div>";

    var munLayer = L.geoJson( gj_mun , {onEachFeature: forEachFeatureMun, style: style});
    var provLayer = L.geoJson( gj_prov , {onEachFeature: forEachFeatureProv, style: styleProv});
    var cirLayer = L.geoJson(  gj_cir , {onEachFeature: forEachFeatureCir, style: styleCir});


    // baseMaps - overlayMaps

    var osmUrl = 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
        osmAttrib = 'Map data &copy; OpenStreetMap contributors',
        landUrl = 'http://{s}.tile.thunderforest.com/landscape/{z}/{x}/{y}.png',
        thunAttrib = 'only Attrib',
        googleSatUrl = 'https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
        googleMapUrl = 'https://mt1.google.com/vt/lyrs=r&x={x}&y={y}&z={z}',
        mbUrl = 'https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWJ1Z2xlMjAyMSIsImEiOiJjbGpyY2NiZTUwZWRzM3BzMHF2MnVybGZoIn0.FFzEizwxsT_0jOxOmcHrCA',
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

    // geoservicios
    // https://github.com/heigeo/leaflet.wms - explicit source spec wms
    var options = {'transparent': true, 'opacity': 0.4};
    var source = L.WMS.source("http://10.100.15.54:8080/geoserver/ows?", options);
    var ueLayer = source.getLayer('uniedu');
    var locLayer = source.getLayer('loc2012');
    var asiLayer = source.getLayer('asientos');
    var reciLayer = source.getLayer('recintos');

    /*
      "Recintos Electorales":reciLayer,
      "Cluster-Recintos Elect.":markersMCG,
      "Asientos Electorales":asiLayer,
      */      
    var overlayMaps = {
      "Circunscripciones":cirLayer,
      "Municipios":munLayer,
      "Provincias":provLayer,
      "Unidades Educativas":ueLayer,
      "Centros Poblados INE-2012":locLayer,
      "Asientos Electorales":asiLayer,
      "Recintos Electorales":reciLayer
    };	
      

    // Set up map

    lat = $('input[name="latitud"]').val();
    long = $('input[name="longitud"]').val();

    var mapCenter = [lat, long];
    var map = L.map('map', {
      defaultExtentControl: true,
      center: mapCenter,
      zoom: 16,
      layers: [mbSat] // only add one!
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
        iconUrl: '../../static/iconos/icons8-street-view-52.png',
        iconSize: [52, 52]
        })
    var marker_gsv = L.marker(map.getCenter(), {icon:iconStreet});
    map.on('move', function() { marker_gsv.setLatLng(map.getCenter()); });


    //----- Add easyButton gsv - StreetView-----
    var sw_marker_gsv = 0;
    var gsvPopup = L.popup().setContent('<u><i>Servicio</i></u>: <b>Google Street View (GSV)</b> \
            y otros Habilitado. Ubique posición y presione click en opciones  \
            (ubicado en la parte inferior/izquierda) ');

    L.easyButton('<img src="../../static/iconos/icons8-street-view-26.png" style="width:23px">', function(btn, map){
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
      },'Habilitar/Inhabilitar Google Street View (GSV)2').addTo(map);
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


/*
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
*/

    //Plugin magic goes here! Note that you cannot use the same layer object again, as that will confuse the two map controls
    var osm2 = new L.TileLayer(osmUrl, {minZoom: 0, maxZoom: 13, attribution: osmAttrib });

    var rect1 = {color: "#ff1100", weight: 3};
    var rect2 = {color: "#0000AA", weight: 1, opacity:0, fillOpacity:0};
    var miniMap = new L.Control.MiniMap(osm2, { toggleDisplay: true, aimingRectOptions : rect1, shadowRectOptions: rect2}).addTo(map);


    // remove - clear
    map.removeLayer(munLayer);


    // add marker & popup with coord
    var marker = L.marker([0,0]);

    function markerOnClick(e)
    {
      var coord = e.latlng.toString().split(',');
      var lat = coord[0].split('(');
      var lng = coord[1].split(')');
      marker.bindPopup('Latitud:: ' + lat[1] + '  Longitud: ' + lng[0]);
    }

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



    // add marker - coordenadas - parametro
    const markerIconParam = L.icon({
        iconSize: [25, 41],
        iconAnchor: [10, 41],
        popupAnchor: [2, -40],
        // specify the path here
        iconUrl:   "../../static/css/leaflet1.5.1/images/marker-icon.png",
        shadowUrl: "../../static/css/leaflet1.5.1/images/marker-shadow.png"
    });

    L.marker([lat, long],
          {
            title: "Lat.: " + lat +  "  Long.: " + long,
              opacity: 0.8,
              icon: markerIconParam
          }
      ).addTo(map);

}


// ---------------------------------------------------------was  viewmap.js
    // Set style function that sets fill color property
    function style(feature) {
        return {
            fillColor: 'green', 
            fillOpacity: 0.2,  
            weight: 2,
            opacity: 1,
            color: '#ffffff',
            dashArray: '3'
        };
    }

    function styleProv(feature) {
        return {
            fillColor: 'orange', 
            fillOpacity: 0.2,  
            weight: 2,
            opacity: 1,
            color: '#ffffff',
            dashArray: '3'
        };
    }

    function styleCir(feature) {
        return {
            fillColor: 'gray', 
            fillOpacity: 0.2,  
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

/*
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
*/
/*
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
*/


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



