var main = function() {
    $(".btn").click(function() {
        $("p").toggleClass("isyellow");
    })
};

$(document).ready(main);
