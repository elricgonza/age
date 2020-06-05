// Operaciones tabla-dinamica para imagenes en asientos y recintos

    // ARRAY FOR HEADER.
    var arrHead = new Array();
    arrHead = ['Imagen', 'Actualizar', 'Actualmente'];      // SIMPLY ADD OR REMOVE VALUES IN THE ARRAY FOR TABLE HEADERS.

    // FIRST CREATE A TABLE STRUCTURE BY ADDING A FEW HEADERS AND
    // ADD THE TABLE TO YOUR WEB PAGE.
    function createTable() {
        var empTable = document.createElement('table');
        empTable.setAttribute('id', 'empTable');            // SET THE TABLE ID.

        var tr = empTable.insertRow(-1);

        for (var h = 0; h < arrHead.length; h++) {
            var th = document.createElement('th');          // TABLE HEADER.
            th.innerHTML = arrHead[h];
            tr.appendChild(th);
        }

        var div = document.getElementById('cont');
        div.appendChild(empTable);    // ADD THE TABLE TO YOUR WEB PAGE.
    }

    // ADD A NEW ROW TO THE TABLE.s
    function addRow(objOpt, codImg = 0, rutaImg = '') {
        var empTab = document.getElementById('empTable');

        var rowCnt = empTab.rows.length;        // GET TABLE ROW COUNT.
        var tr = empTab.insertRow(rowCnt);      // TABLE ROW.
        tr = empTab.insertRow(rowCnt);

        for (var c = 0; c < arrHead.length; c++) {
            var td = document.createElement('td');          // TABLE DEFINITION.
            td = tr.insertCell(c);

            if (c == 0) {
                var td = document.createElement('td');          // TABLE DEFINITION.
                td = tr.insertCell(c);

                //Create and append select list
                var selectList = document.createElement("select");
                selectList.id = "idSelect" + rowCnt;
                selectList.name = "mySelect" + rowCnt;

                for (var prop in objOpt) {
                    var option = document.createElement("option");
                    if (objOpt.hasOwnProperty(prop)) {
                        option.value = prop;
                        option.text = objOpt[prop];
                        if (prop == codImg) {
                            option.selected = true;
                        }
                        selectList.appendChild(option);
                    }

                td.appendChild(selectList);
                }
            }

            if (c == 1) {

                var td = document.createElement('td');          // TABLE DEFINITION.
                td = tr.insertCell(c);

                //Create and append inputFile
                var inputFile = document.createElement("input");
                inputFile.name = 'filelist' //  + rowCnt;
                inputFile.id = 'exa';
                inputFile.type = 'file';
                inputFile.accept = 'image/*';
                //inputFile.accept = 'image/png, image/jpeg, image/jpg, image/tif, image/bmp';
                //inputFile.required = true;
                //inputFile.value = 'archivito.txt';

                td.appendChild(inputFile);
            }

            if (c == 2) {  
                /*
                // ADD A BUTTON.
                var button = document.createElement('input');

                // SET INPUT ATTRIBUTE.
                button.setAttribute('type', 'text');
                button.setAttribute('value', rutaImg);

                // ADD THE BUTTON's 'onclick' EVENT.
                button.setAttribute('onclick', 'removeRow(this)');

                td.appendChild(button);

                */


                // ADD img
                var imglink = document.createElement('img');
                //imglink.setAttribute('src', {{ url_for('img/asi', filename='{{rutaImg}}') }} );
                //imglink.setAttribute('src', "/static/img/asi/00098_02.jpg") ;
                //imglink.setAttribute('src', "/static/imgbd/asi/00102_02.jpg") ;
                imglink.setAttribute('src', rutaImg) ;
                imglink.setAttribute('alt', rutaImg);
                imglink.setAttribute('height', "auto");
                imglink.setAttribute('width', "30%");
                td.appendChild(imglink);
            }
        }
    }

    function pAddRow(objOpt) {
        addRow(objOpt);
    }

    // DELETE TABLE ROW.
    function removeRow(oButton) {
        var empTab = document.getElementById('empTable');
        empTab.deleteRow(oButton.parentNode.parentNode.rowIndex);       // BUTTON -> TD -> TR.
    }

    // EXTRACT AND SUBMIT TABLE DATA.
    function pSubmit(){
        submit();
    }

    function submit(){
        var arrs = [];
        var arrf = [];
        var arrv = [];

        var myform = document.getElementById('imgform');
        for (var i=0; i<myform.elements.length; i++){  //loop through all form elements
            if (myform.elements[i].type=="select-one" || myform.elements[i].type=="select-multiple"){
                //var s = myform.elements[i];
                arrs.push(myform.elements[i].value);
                //arrs.push(s.value);
            }
            if (myform.elements[i].type=='file'){
                arrf.push(myform.elements[i].name);
                arrv.push(myform.elements[i].value);
                //alert(myform.elements[i].filename);
                //var f = myform.elements[i];
                //arrf.push(f.name);
            }
        }
        document.getElementById('id_imgsa').value = arrs;
        document.getElementById('id_filesa').value = arrf;
        document.getElementById('id_filesv').value = arrv;
    }
