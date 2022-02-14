// Team Splendid Slugs :: Jonathan Wu, Roshani Shrestha
// SoftDev pd2
// K30 -- canvas based JS drawing
// 2022-02-14m
// time spent: 45 minutes

// JavaScript canvas work

//retrieve node in DOM via ID
var c = document.getElementById("slate");

//instantiate a CanvasRenderingContext2D Object
var ctx = c.getContext("2d");

//init global state var 
var mode = "rect";

// var toggleMode = function(e) {
var toggleMode = (e) => {
    console.log("toggling...");
    if (e) {
        ctx.strokeStyle = 'red';
    }
    else {
        ctx.strokeStyle = 'red';
    }
}

var drawRect() = function(e) {
    var mouseX = offsetX;
    var mouseY = offsetY;
    console.log("mouseclick registered at ", mouseX, mouseY);
    ctx.beginPath();
}

//var drawCircle = function(e) {
var drawCircle = (e) => {
    ctx.beginPath();
    ctx.arc(mouseX, mouseY, 50, 0, 2 * Math.PI);
    ctx.stroke();
    console.log("mouseclick registered at ", mouseX, mouseY);
    ctx.fill();
}

//var draw = function(e) {
var draw = (e) => {
    console.log("draw");
}

//var wipeCanvas = function() {
var wipeCanvas = () => {
    clearRect();
}

c.addEventListener("click", draw);
var bToggler = document. ;
bToggler. ;
var clearB = ;
clearB. ; 