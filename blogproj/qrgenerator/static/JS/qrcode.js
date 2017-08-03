var data = document.createElement("input");
data.placeholder = "Put Data/URL here";

var size = document.createElement("input");
size.type = "range";
size.setAttribute("value", 300);
size.min = 50;
size.max = Math.floor(Math.sqrt(3e5));

var chart = document.createElement("img");

var label = document.createElement("label");
label.setAttribute("for", "auto");
label.innerHTML = "Auto update/run";

var generate = document.createElement("button");
generate.innerHTML = "Generate!";
generate.style.display = "none";

var checkbox = document.createElement("input");
checkbox.type = "checkbox";
checkbox.checked = "checked";
checkbox.id = "auto";

var checkboxHandler = function() {

  if(checkbox.checked == false) {

    generate.style.display = "block";
    data.onkeydown = data.onkeyup = size.onchange = false;

  }

  else {

    generate.style.display = "none";
    data.onkeydown = data.onkeyup = size.onchange = formHandler;

  }

};

var formHandler = function() {

  chart.src = "https://chart.googleapis.com/chart?cht=qr&chs="+size.value+"x"+size.value+"&choe=UTF-8&chl="+data.value;

};

checkbox.onchange = checkboxHandler;
checkboxHandler();
formHandler();

generate.onclick = formHandler;

document.body.appendChild(data);
document.body.appendChild(size);
document.body.appendChild(checkbox);
document.body.appendChild(label);
document.body.appendChild(generate);
document.body.appendChild(chart);
