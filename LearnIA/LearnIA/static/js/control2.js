window.addEventListener("load",init);
window.addEventListener("load",load);

function init(){
    document.getElementById("error").style.display="none";
}

function cerrar(){
    document.getElementById("error").style.display="none";
}

function load() { 
	
	var botonSubmitDemo = document.getElementById("button-demo"); 
	botonSubmitDemo.addEventListener("click", function(event){
		if (document.formDemo.inputDemo.value.length <= 1){ 
			event.preventDefault();
	      	document.getElementById("error").style.display="block";
	      	document.formDemo.inputDemo.focus();
		}else{
			$('#modal2').hide();
			document.getElementById("error").style.display="none";
		}
		
		
        
	}, false); 
} 
