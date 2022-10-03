//! EVENT LISTENER
// JavaScript will be listening for an event to occur and then execute a function when it happens

// listening for an event looks like this:
// myvar.addEventListener(event,func);
// e.g.
// var head = document.querySelectorAll("h1");
// head.addEventListener("click",changeColor);
// many possible events:
// Clicks
// Hovers
// Double Clicks
// Drags
// https://developer.mozilla.org/en-US/docs/Web/Events

var headOne = document.querySelector("#one")
var headTwo = document.querySelector("#two")
var headThree = document.querySelector("#three")

console.log("Connected!")

// change text and color when hover
headOne.addEventListener("mouseover", function(){
    headOne.textContent = "Mouse currently over";
    headOne.style.color = "red";
})
// change back
headOne.addEventListener("mouseout", function(){
    headOne.textContent = "HOVER OVER ME"
    headOne.style.color = "black"
})
// change on click
headTwo.addEventListener("click", function(){
    headTwo.textContent = "CLICKED ON"
    headTwo.style.color = "blue"
})
// change on double click
headThree.addEventListener("dblclick", function(){
    headThree.textContent = "I WAS DOUBLE CLICKED"
    headThree.style.color = "green"
})