$(document).ready(function() {
    // function to display profile update form
    $("#update-profile").click(function() {
        $("#update-form").show();
    });

    // Timer function to display messages
    setTimeout(function(){
        $("#messages").hide(1000);
    }, 5000);
});
