
$(document).ready(function(){
        $(".toggle-btn").click(function(){
            if(screen.width < 1500 ) {
            $('#sidebar').toggleClass('active');
            $('.sidebar-menu li span').toggleClass('menu-hide'); };
});
});

    