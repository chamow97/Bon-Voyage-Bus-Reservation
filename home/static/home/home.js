$(window).scroll( function() {
    var x = parseInt($("#logo").css("margin-right"));
    $("#logo").css("margin-right", function(i) { return i + ($(window).scrollTop() * 2)});
});	