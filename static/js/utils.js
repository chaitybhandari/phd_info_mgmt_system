function get_year_range(start_year){
    var start =  start_year;
    var end = new Date().getFullYear();
    var options = ""
    for(var year=start; year<=end; year++){
        options += "<option value=" + year + ">"+year+"</option>"

    }
    return options

}

function is_number(id, e){
    var specialKeys = new Array();
    specialKeys.push(8); //Backspace
    var keyCode = e.which ? e.which : e.keyCode;
    var ret = ((keyCode >=48 && keyCode <= 57) ||
              (specialKeys.indexOf(keyCode) != -1))
    document.getElementById(id).style.display = ret ? "none" : "inline" ;
    console.log(ret)
    return ret

}

function hide_on_blur(id){
    document.getElementById(id).style.display = "none"
}
