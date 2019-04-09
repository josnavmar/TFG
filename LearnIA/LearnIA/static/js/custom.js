
 /* jQuery Pre loader
  -----------------------------------------------*/
$(window).load(function(){
    $('.preloader').fadeOut(2000); // set duration in brackets    
});


$(document).ready(function() {

  /* Home Slideshow Vegas
  -----------------------------------------------*/
  $(function() {
    $('body').vegas({
        slides: [
            { src: '/static/images/fondo_1.jpg' },
            { src: '/static/images/fondo_2.jpg' },
            { src: '/static/images/fondo_3.png' },
            { src: '/static/images/fondo_4.jpeg' },
            { src: '/static/images/fondo_5.jpeg' },
            { src: '/static/images/fondo_7.jpg' },
            { src: '/static/images/fondo_8.jpg' }
        ],
        timer: false,
        transition: [ 'zoomOut', ]
    });
  });


   /* Back top
  -----------------------------------------------*/
    $(window).scroll(function() {
        if ($(this).scrollTop() > 200) {
        $('.go-top').fadeIn(200);
        } else {
          $('.go-top').fadeOut(200);
        }
        });   
        // Animate the scroll to top
      $('.go-top').click(function(event) {
        event.preventDefault();
      $('html, body').animate({scrollTop: 0}, 300);
      })
      

  /* wow
  -------------------------------*/
  new WOW({ mobile: false }).init();

  });

window.addEventListener("load",init);

window.addEventListener("load",load);

function init(){
    document.getElementById("selectAlgo").addEventListener("change",revisar);
}

function revisar(){
    if(document.getElementById("selectAlgo").value=="rf"){
        document.getElementById("grupParam1").style.display="block";
        document.getElementById("grupParam2").style.display="none";
    }else if(document.getElementById("selectAlgo").value=="nb"){
    	document.getElementById("grupParam1").style.display="none";
        document.getElementById("grupParam2").style.display="block";
    }else{
    	 document.getElementById("grupParam2").style.display="none";
         document.getElementById("grupParam1").style.display="none";
    }
}

function load() { 
	var el = document.getElementById("text"); 
	el.addEventListener("click", function(){
		document.getElementById("grupParam2").style.display="none";
        document.getElementById("grupParam1").style.display="none";
	}, false); 
} 

