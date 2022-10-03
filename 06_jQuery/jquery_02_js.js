
// $("h1").click(function(){
//     console.log("There was a click!")
// })

////////////////////////////////////////////////////////

$("h4").click(function(){
    $(this).text("I was changed!")
})

////////////////////////////////////////////////////////
//# grab multiple elements
$("li").click(function(){
    console.log("any li was clicked")
})

////////////////////////////////////////////////////////

//# key press
// basic
// $("input").eq(0).keypress(function(){
//     $("h3").toggleClass("turnBlue");
// })

$("input").eq(0).keypress(function(event){
    // console.log(event);
    // the keycode 13 is the Enter Key
    if (event.which === 13) {
        $("h3").toggleClass("turnBlue");
    }
})

//# on()
$("h1").on("dblclick",function(){
    $(this).toggleClass("turnBlue");
})

$("h4").on("mouseenter",function(){
    $(this).toggleClass("turnRed");
})

//# ANIMATIONS
$("input").eq(1).on("click",function(event){
    // $(".container").fadeOut(3000)
    $(".container").slideUp(3000)
})

