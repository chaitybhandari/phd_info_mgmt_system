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
function validate_phd_course_form(){
    var phd_course_form  = document.forms["phd_course_form"];
    var course_id = phd_course_form["course_id"].value;
    var reg = /^[A-Z]{2,5}-(F|G)\d\d\d/g;
    var match_arr = course_id.match(reg);
    if (!match_arr){
        alert("Please enter a valid Course ID.");
        return false;
    }

}
function validate_phd_scholar_form(){
    var phd_form = document.forms["phd_scholar_form"];
    var id_number = phd_form["id_number"].value;
    var reg = /20\d\dPH[A-Z][A-Z]\d\d\d\dH/g;
    var match_arr = id_number.match(reg);
    if (!match_arr){
        alert("Please enter a valid ID Number.");
        //document.getElementById("id_error").style.display = "inline"
        return false;
    }

    var email_address = phd_form["email"].value;
    if (email_address != ""){
        var regular_email_reg = /^[A-Za-z][\w]+\@[\w]+(\.com|\.co\.in)/g;
        var bits_email_reg = /^f20\d\d\d\d\d\d\@bits.hyderabad.ac.in/g;
        var regular_email_address = email_address.match(regular_email_reg);
        var bits_email_address = email_address.match(bits_email_reg);
        if (!regular_email_address && !bits_email_address){
            alert("Please enter a valid email address.");
            return false;
        }
    }


}

