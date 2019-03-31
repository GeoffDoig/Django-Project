$(document).ready(function() {
    $("#update-profile").click(function() {
        $("#update-form").show();
    });
    setTimeout(function(){
        $("#messages").hide(1000);
    }, 5000);
});