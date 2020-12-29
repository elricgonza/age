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
    if (x == 27 || x == 9 || 'undefined') {
            $.getJSON('/get_geo_esp', {
                latitud: $('input[name="latitud"]').val(),
                longitud: $('input[name="longitud"]').val()
            }, function(data) {
                console.log(data);
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
