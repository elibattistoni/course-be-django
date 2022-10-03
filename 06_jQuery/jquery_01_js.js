// open html in browser, and open console; type $ and press enter; if a function is returned than you know that jquery is loaded
// commands
$('h1')
$('li')

var x = $('h1')
x.css('color','red')

// change css style all at once
var newCSS = {
    color:"white",
    background:"blue",
    border:"5px solid red"
}
x.css(newCSS)

/////////
var listItems = $('li')
// this is a node list or a list, not an array
listItems.css('color','blue')
// in order to grab only one of them
listItems.eq(0).css('color','orange') // first item
listItems.eq(-1).css('background','orange') // last item

// get the text
$('h1').text()
// change the text
$('h1').text("BRAND NEW TEXT")
// change the html
$('h1').html("<em>new</em>")

// get all input tags
$('input')
// change submit input button to checkbox
$('input').eq(1).attr('type','checkbox')
// change value of textbox
$('input').eq(0).val('new value!')

//! add css classes with jquery
$('h1').addClass('turnRed')
$('h1').removeClass('turnRed')

//! toggle classes
$('h1').toggleClass('turnBlue') // on
$('h1').toggleClass('turnBlue') // off