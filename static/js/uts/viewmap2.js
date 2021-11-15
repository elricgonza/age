function viewMap() {
  alert('rarooo..');
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


    function markerOnClick(e)
    {
      var coord = e.latlng.toString().split(',');
      var lat = coord[0].split('(');
      var lng = coord[1].split(')');
      marker.bindPopup('Latitud:: ' + lat[1] + '  Longitud: ' + lng[0]);
    }

