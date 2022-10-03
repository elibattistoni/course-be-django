- jQuery is a JavaScript library
- it is just a large single .js file that has many pre-built methods and objects that simplofy your workflow, especially when interacting with the DOM and making HTTP requests (AJAX)
- when jQuery was created, the more robust and convenient methods such as .querySelector() did not exist
- jQuery was created as a way to help aomplify interactions with the DOM
- one of its main features is the use of $
- how do we get jQuery? there are two options:
  - Link a CDN hosted file (like we did for Bootstrap)
  - Download the .js file from jQuery's official website
- once you've connected jQuery with the <script> tags in the HTML, then you can start to interact with the DOM through jQuery calls


## jQuery vs. vanilla JavaScript: variable assignment

**jQuery**
`var divs = $('div')`

**vanilla JavaScript**
`var divs = document.querySelectorAll('div')`

## jQuery vs. vanilla JavaScript: change style

**jQuery**
`$(el).css('border-width', '20px')`

**vanilla JavaScript**
`el.style.borderWidth = '20px'`

## jQuery vs. vanilla JavaScript: functions

**jQuery**
`$(document).ready(function(){ // code })`

**vanilla JavaScript**
```
function ready(fn){
    if (document.readyState != 'loading'){
        fn();
    } else {
        document.addEventListener('DOMContentLoaded', fn);
    }
}
```

Some situations are helped tremendously by jQuery while others may not necessitate it

https://api.jquery.com/category/events/
https://api.jquery.com/category/effects/