
window.addEventListener("load",init);
window.addEventListener("load",load);

function init(){
    document.getElementById("error1").style.display="none";
    document.getElementById("error2").style.display="none";
    document.getElementById("error3").style.display="none";
}

function cerrar(){
    document.getElementById("error1").style.display="none";
    document.getElementById("error2").style.display="none";
    document.getElementById("error3").style.display="none";
}

function load() { 
	
	var botonSubmitDemo = document.getElementById("button-submit"); 
	botonSubmitDemo.addEventListener("click", function(event){
		validate = true;
		var _validFileExtensions = [".jpg", ".jpeg", ".png"];
		var oInput =document.getElementById("inputDemo"); 
		if (oInput.type == "file") {
	        var sFileName = oInput.value;
	         if (sFileName.length > 0) {
	            var blnValid = false;
	         
	            if(sFileName.indexOf('%') != -1){
	            	
	                 document.getElementById("error1").style.display="block";
	            	 var blnValid = false;
	            	 document.getElementById("inputDemo").value = null;
	            	 document.getElementById('submit').disabled=false;
	            	 event.preventDefault();
	            	 validate = false;
	            	 
	            }
	            
	            for (var j = 0; j < _validFileExtensions.length; j++) {
	                var sCurExtension = _validFileExtensions[j];
	                if (sFileName.substr(sFileName.length - sCurExtension.length, sCurExtension.length).toLowerCase() == sCurExtension.toLowerCase()) {
	                    blnValid = true;
	                    break;
	                }
	            }
	             
	            if (!blnValid) {
	            	event.preventDefault();
	            	document.getElementById("error2").style.display="block";
	                oInput.value = "";
	                document.getElementById("inputDemo").value = null;
	                document.getElementById('submit').disabled=false;
	                validate = false;
	            }
	        }else{
	        	event.preventDefault();
	        	document.getElementById("error3").style.display="block";
	        	validate = false;
	        }
	    }
		
		if(validate == true){
			$('#modal4').hide();
		}
		
        
	}, false); 
} 