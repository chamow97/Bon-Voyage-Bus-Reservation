
$(window).scroll( function() {
    var x = parseInt($("#logo").css("margin-right"));
    //alert(x);
    $("#logo").css("margin-right", function(i) { return i + ($(window).scrollTop() * 1.2)});   
});	