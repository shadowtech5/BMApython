$(document).ready(function(){
    $(window).scroll(function(){
        console.log("ai");
    });
    console.log("test");
    $(".sign_button").click(function(e){
        $(".login-box").toggle("slow");
    });
    $(".celebrity-anchor").click(function(e){
        console.log("hi");
        $(".celebrity-anchor_tab").removeClass("hide");
        $(".real_anchor_tab").addClass("hide");
    });
    $(".real_anchor").click(function(e){
        console.log("hey");
        $(".celebrity-anchor_tab").addClass("hide");
        $(".real_anchor_tab").removeClass("hide");
    });
    $("#booking-info").click(function(){
    	$("#booking-info").addClass("active");
    	$("#biography").removeClass("active");
        $("#photos").removeClass("active");
        $("#videos").removeClass("active");
    	$(".biography-container").addClass("hide");
    	$(".booking-info-container").removeClass("hide");
        $(".photos-container").addClass("hide");
        $(".video-container").addClass("hide");
        $("#clientsandtest").removeClass("active");
        $(".testmonial").addClass("hide");
    });
    $("#biography").click(function(){
    	$("#booking-info").removeClass("active");
    	$("#biography").addClass("active");
        $("#photos").removeClass("active");
        $("#videos").removeClass("active");
    	$(".biography-container").removeClass("hide");
    	$(".booking-info-container").addClass("hide");
        $(".photos-container").addClass("hide");
        $(".video-container").addClass("hide");
        $("#clientsandtest").removeClass("active");
        $(".testmonial").addClass("hide");
    });
    $("#photos").click(function(){
        $("#booking-info").removeClass("active");
        $("#photos").addClass("active");
        $("#biography").removeClass("active");
        $("#videos").removeClass("active");
        $("#clientsandtest").removeClass("active");
        $(".testmonial").addClass("hide");
        $(".biography-container").addClass("hide");
        $(".booking-info-container").addClass("hide");
        $(".photos-container").removeClass("hide");
        $(".video-container").addClass("hide");
    });
    $("#videos").click(function(){
        $("#booking-info").removeClass("active");
        $("#videos").addClass("active");
        $("#biography").removeClass("active");
        $("#photos").removeClass("active");
        $(".biography-container").addClass("hide");
        $(".booking-info-container").addClass("hide");
        $(".video-container").removeClass("hide");
        $(".photos-container").addClass("hide");
        $("#clientsandtest").removeClass("active");
        $(".testmonial").addClass("hide");
    });
    $("#clientsandtest").click(function(){
        $("#booking-info").removeClass("active");
        $("#videos").removeClass("active");
        $("#biography").removeClass("active");
        $("#photos").removeClass("active");
        $(".biography-container").addClass("hide");
        $(".booking-info-container").addClass("hide");
        $(".video-container").addClass("hide");
        $(".photos-container").addClass("hide");
        $("#clientsandtest").addClass("active");
        $(".testmonial").removeClass("hide");
    });
    $("#book_now_buttonss").click(function(e){
        console.log("inside book");
        $(".biography-container").addClass("hide");
        $(".booking-info-container").addClass("hide");
        $(".video-container").addClass("hide");
        $(".photos-container").addClass("hide");
        $(".booking_container").removeClass("hide");
    });
    $("#budget-fix").click(function(e){
        console.log("budget");
        $("#budget-fix_container").slideToggle("slow");
        $("#available_result").empty();
        $('#available_form').show();
        $('#available_result_book').hide();
    });
    $("#book_confirmation").click(function(e){
        console.log("book_confirmation");
        $confirm_var = confirm("Are you sure");
        if($confirm_var)
        {
            
            var frm = $('#contact-form');
            e.preventDefault;
            $.ajax({
                url: 'book.php',
                type: 'POST',
                data: frm.serialize(),
                success: function (data) 
                {
                    alert("Booking Confirmed please check your mail");
                    $("#available_result_book").show(); // appending data response to result-page div
                    setTimeout(function () {
                        $("#result-page").hide(); 
                        $("#link-page").show();
                    }, 5000);
                }
            });
        }
    });
    $("#feedback").click(function(e){
        console.log("feedback");
        var frm = $('#feedback-form');
        e.preventDefault;
        $.ajax({
            url: 'feedback.php',
            type: 'POST',
            data: frm.serialize(),
            success: function (data) 
            {
                alert("Thank you for sending your feedback");
            }
        });
    });
    // $(".budget-fix").click(function (e) {
    //     console.log("inside")
    //     var Id=$(this).attr('data-ids');
    //     var input = "<input type='hidden' value='"+Id+"' name='jishnu'/>"
    //     $('#append').append(input);
    //     $("#available_result").hide(); // appending data response to result-page div
    //     $('#available_form').show();  //hiding form
    //     $("#available_result").empty();
    //     console.log(Id);
    // });
    $(".filter").click(function(){
        console.log("test111");
        $(".filter-options-details").slideToggle("slow");
    });
    $("#test").click(function (e) {
        var frm = $('#form1');
        e.preventDefault;
        $.ajax({
            url: 'check_rate.php',
            type: 'POST',
            data: frm.serialize(),
            success: function (data) 
            {
                $("#available_result").append(data).show(); // appending data response to result-page div
                $('#available_form').hide();  //hiding form
                setTimeout(function () {
                    $("#result-page").hide(); 
                    $("#link-page").show();
                }, 5000);
            }
        });
    });

    $("#price").slider({
        tooltip: 'always'
    });
    $("#performing_members").slider({
        tooltip: 'always'
    });
    $("#check_available_form_button").click(function (e) {
        console.log("fdjg");
        // this.disabled = true;
        $('#check_available_form_button').hide();
        var frm = $('#check_available_form');
        $.ajax({
            url: 'check_available.php',
            type: 'POST',
            data: frm.serialize(),
            success: function (data) {
                $(".price_container").append(data).show(); // appending data response to result-page div
                $('.check_available_form_contents').hide();  //hiding form
                $('#check_available_form_button').hide();
            }
        });
    });
    
});
