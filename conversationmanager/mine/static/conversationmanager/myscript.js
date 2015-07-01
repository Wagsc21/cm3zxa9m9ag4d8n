 var removerows = function  (tablebody) {
      var rows = tablebody.getElementsByTagName("tr");
      var len=rows.length
      if(len > 0)
        rows[len-1].parentNode.removeChild(rows[len-1]);
    }

    var addrows = function  (tablebody) {
     
        var rows = tablebody.getElementsByTagName("tr");
        var len=rows.length
        var row = document.createElement("tr");
        var titlecell = document.createElement("td");
        titlecell.appendChild(document.createTextNode("Row " + len));
        row.appendChild(titlecell);
        for (var j=0;j<3;j++)
        {
          var cell = document.createElement("td");
          var input = document.createElement("input");
          input.setAttribute("type", "text");
          input.setAttribute("name", "row["+len+"],col["+j+"]");
          cell.appendChild(input);
          row.appendChild(cell);
        }
        tablebody.appendChild(row);
    }

    var adder = function  () {
      var tablebody = document.getElementById("maintablebody");
      console.log("head");
      addrows(tablebody);
    }
    var remover=function () {
      var tablebody=document.getElementById("maintablebody")
      removerows(tablebody)
      // body...
    }