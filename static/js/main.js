// navbar
function myFunction() {
    document.getElementById("nav-h").classList.toggle("open");
    nav-h.classList.remove('close');
  }
  
  // Closing the dropdown if the user clicks outside of it
  window.onclick = function(e) {
    if (!e.target.matches('.dropbtn')) {
    var sider  = document.getElementById("nav-h");
      if (nav-h.classList.contains('open')) {
        nav-h.classList.remove('open');
      }
    }
  }
  // smooth scroll
  var navMenuAnchorTags = document.querySelectorAll('.nav-social-h a');
  console.log(navMenuAnchorTags);