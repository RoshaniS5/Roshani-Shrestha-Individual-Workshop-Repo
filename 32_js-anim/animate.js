// Team Splendid Slugs :: Jonathan Wu, Roshani Shrestha
// SoftDev pd2
// K31 -- canvas based JS animation
// 2022-02-15t
// time spent: 45 minutes

// model for HTML5 canvas-based animation

// SKEELTON


//access canvas and buttons via DOM
var c = document.getElementById("playground"); // GET CANVAS
var dotButton = document.getElementById("buttonCircle"); // GET DOT BUTTON
var stopButton = document.getElementById("buttonStop"); // GET STOP BUTTON
var movieButton = document.getElementById("buttonMovie"); // GET MOVIE BUTTON

//prepare to interact with canvas in 2D
var ctx = c.getContext("2d"); 

//set fill color to team color
ctx.fillStyle = 'purple'; 

var requestID;  //init global var for use with animation frames


//var clear = function(e) {
var clear = (e) => {
  console.log("clear invoked...")
  ctx.clearRect(0, 0, c.clientWidth, c.clientHeight); //clears canvas
};


var radius = 0;
var growing = true;


//var drawDot = function() {
var drawDot = () => {
  console.log("drawDot invoked...")
  clear();
  window.cancelAnimationFrame(requestID);
  ctx.beginPath();
  ctx.arc(c.clientWidth/2, c.clientHeight/2, radius, 0, 2 * Math.PI);
  ctx.stroke();
  ctx.fill();
  if (radius === (Math.min(c.clientWidth,c.clientHeight) / 2)) {
    growing = false;
  }
  if (radius === 0) {
    growing = true;
   }
  if (growing) {
    radius++;
  }
  else {
    radius--;
  }
  requestID = window.requestAnimationFrame(drawDot);
};

var movie = () => {
  console.log("movie");
  var dvdImage = new Image(100);
  dvdImage.src = 'logo_dvd.jpg';
  // var dvdImage = document.getElementById('source');
  void ctx.drawImage(dvdImage, 0, 0, 100, 50);
};

//var stopIt = function() {
var stopIt = () => {
  console.log("stopIt invoked...")
  console.log( requestID );
  window.cancelAnimationFrame(requestID);
};


dotButton.addEventListener( "click", drawDot );
stopButton.addEventListener( "click",  stopIt );
movieButton.addEventListener( "click", movie );
