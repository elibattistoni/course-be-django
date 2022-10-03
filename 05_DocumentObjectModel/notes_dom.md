DOM = Document Object Model

the DOM allows us to interface our Javascript code to interact with HTML and CSS

Browsers will construct the DOM, which means storing all the HTML tags as Javascript objects

you can see the DOM of any website:
- go to a website and in the console type: document
- that will return the HTML text of the page. to see the actual objects use: console.dir(document)

this DOM will allow us to use Javascript to interact with the web page

the DOM is enormous, most developers won't use all the properties

we will cover the common objects used

### Important Document attributes:

`document.URL`

`document.body`

`document.head`

`document.links`

### Methods for grabbing elements from the DOM:

`document.getElementById()`

`document.getElementByClassName()`

`document.getElementsByTagName()`

`document.querySelector()` returns the first object matching the css style selector

`document.querySelectorAll()` returns all the objects matching the css style selector