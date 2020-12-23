// Operaciones tabla-dinamica para indicadores en asientos y recintos

// ARRAY FOR HEADER.
var arrHead = new Array();
arrHead = ['Categoria', 'Subcategoria', 'Observaciones', 'Eliminar']; // SIMPLY ADD OR REMOVE VALUES IN THE ARRAY FOR TABLE HEADERS.

// FIRST CREATE A TABLE STRUCTURE BY ADDING A FEW HEADERS AND
// ADD THE TABLE TO YOUR WEB PAGE.
function createTable() {
    var empTable = document.createElement('table');
    empTable.setAttribute('id', 'empTable'); // SET THE TABLE ID.

    var tr = empTable.insertRow(-1);

    for (var h = 0; h < arrHead.length; h++) {
        var th = document.createElement('th'); // TABLE HEADER.
        th.innerHTML = arrHead[h];
        tr.appendChild(th);
    }

    var div = document.getElementById('cont'); // id  div en html  
    div.appendChild(empTable); // ADD THE TABLE TO YOUR WEB PAGE.
}

// PARA  DOS COMBOS
// ADD A NEW ROW TO THE TABLE.s
function addRow2(objOpt, codImg = 0, rutaImg = '', objOpt2, codImg2 = 0) {
    //alert('PARA 2 CBX INICIA de add la fila');
    var empTab = document.getElementById('empTable');

    //var rowCnt = empTab.rows.length; // GET TABLE ROW COUNT.

    var rowCnt = 1; // GET TABLE ROW COUNT.
    var tr = empTab.insertRow(rowCnt); // TABLE ROW.
    tr = empTab.insertRow(rowCnt);

    for (var c = 0; c < arrHead.length; c++) {
        var td = document.createElement('td'); // TABLE DEFINITION.
        td = tr.insertCell(c);

        if (c == 0) {
            var td = document.createElement('td'); // TABLE DEFINITION.
            td = tr.insertCell(c);

            //Create and append select list
            var selectList = document.createElement("select");
            selectList.id = "idSelect" + rowCnt;
            selectList.name = "mySelect" + rowCnt;
            selectList.onchange = function() { cambia(this.id) };

            // objOpt ->  toda la tabla defin de imag [frontal, panoramica plaza,...]             
            for (var prop in objOpt) {
                var option = document.createElement("option");
                if (objOpt.hasOwnProperty(prop)) {
                    option.value = prop;
                    option.text = objOpt[prop];
                    //  opcion seleccionada ->  bajado de la base de datos
                    if (prop == codImg) {
                        option.selected = true;
                    }
                    selectList.appendChild(option);
                }
                td.appendChild(selectList);
            }
        }

        if (c == 1) {
            //alert('segundo combo');
            var td = document.createElement('td'); // TABLE DEFINITION.
            td = tr.insertCell(c);

            //Create and append select list
            var selectList2 = document.createElement("select");
            selectList2.id = "idSelectSub" + rowCnt;
            selectList2.name = "mySelectSub" + rowCnt;

            // objOpt ->  toda la tabla defin de imag [frontal, panoramica plaza,...]             
            for (var prop in objOpt2) {
                var option = document.createElement("option");
                if (objOpt2.hasOwnProperty(prop)) {
                    option.value = prop;
                    option.text = objOpt2[prop];
                    //  opcion seleccionada ->  bajado de la base de datos
                    if (prop == codImg2) {
                        option.selected = true;
                    }
                    selectList2.appendChild(option);
                }
                td.appendChild(selectList2);
            }
        }

        if (c == 2) {
            var td = document.createElement('td'); // TABLE DEFINITION.
            td = tr.insertCell(c);

            // ADD A INPUT. 
            var nuevoInput = document.createElement('input');
            nuevoInput.id = "idTxtObs" + rowCnt;
            nuevoInput.name = "myTxtObs" + rowCnt;
            nuevoInput.value = rutaImg;

            td.appendChild(nuevoInput);
        }

        if (c == 3) {

            // ADD A BUTTON.
            var button = document.createElement('input');

            // SET INPUT ATTRIBUTE.
            button.setAttribute('type', 'button');
            button.setAttribute('value', 'Eliminar');

            // ADD THE BUTTON's 'onclick' EVENT.
            button.setAttribute('onclick', 'removeRow(this)');

            td.appendChild(button);
        }
    }
} //FIN  ADD A NEW ROW TO THE TABLE

// ADD A NEW ROW  VACIA A LA TABLA ->  A LACER CLICK EN EL BOTON 'Adicionar Indice'
function pAddRow(objOpt, objSubcat) {
    //addRow2(objOpt);
    addRow2(objOpt, 0, '', objSubcat, 0)
}

// DELETE TABLE ROW.
function removeRow(oButton) {
    if (confirm("Confirmar la Eliminacion!.   Esta seguro de Eliminar?")) {
        txt = "You pressed OK!";
        var empTab = document.getElementById('empTable');
        empTab.deleteRow(oButton.parentNode.parentNode.rowIndex); // BUTTON -> TD -> TR.
    } else {
        txt = "You pressed Cancel!";
    }
}

// EXTRACT AND SUBMIT TABLE DATA.
function pSubmit() {
    submit();
}

function submit() {
    var arrs = [];
    var arrf = [];
    var arrv = [];

    var myform = document.getElementById('imgform');
    for (var i = 0; i < myform.elements.length; i++) { //loop through all form elements
        // Primer select  se obtiene los id  seleccionados
        for (var j = 0; j < myform.elements.length; j++) {
            var n1 = 'idSelect' + j;
            if (myform.elements[i].id == n1) {
                arrs.push(myform.elements[i].value);
            }
        }
        // Segundo select  se obtiene los id  seleccionados
        for (var j = 0; j < myform.elements.length; j++) {
            var n2 = 'idSelectSub' + j;
            if (myform.elements[i].id == n2) {
                arrf.push(myform.elements[i].value);
            }
        }
        // InputText para las observaciones
        for (var j = 0; j < myform.elements.length; j++) {
            var n3 = 'idTxtObs' + j;
            if (myform.elements[i].id == n3) {
                arrv.push(myform.elements[i].value);
            }
        }
    }
    document.getElementById('id_imgsa').value = arrs;
    document.getElementById('id_filesa').value = arrf;
    document.getElementById('id_filesv').value = arrv;
}