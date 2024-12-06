function redirectToDoska() {
    window.location.href = 'doska.html';
}
function sendMessage() {
    alert("Товар временно отсутствует!");
}
  
var modal = document.getElementById('id01');
var modal2 = document.getElementById('id02');

window.onclick = function(event) {
  if (event.target == modal && event.target == modal2) {
    modal.style.display = "none";
    modal2.style.display = "none";
  }
}

/* Toggle between showing and hiding the navigation menu links when the user clicks on the hamburger menu / bar icon */
function myFunction() {
  var x = document.getElementById("myLinks");
  if (x.style.display === "block") {
    x.style.display = "none";
  } else {
    x.style.display = "block";
  }
}