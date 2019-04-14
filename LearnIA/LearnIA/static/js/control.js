window.addEventListener("load",init);
window.addEventListener("load",load);
window.addEventListener("load",loadSubmit);

function init(){
    document.getElementById("selectAlgorit").addEventListener("change",revisar);
    document.getElementById("button-submit").style.display="none";
    document.getElementById("button-gen").style.display="block";
}

function loadSubmit(){
    document.getElementById("selectIteracSVC").addEventListener("change",loadSubmitRevisar);
    document.getElementById("selectPolarSVC").addEventListener("change",loadSubmitRevisar);
    
    document.getElementById("selectPolarNB").addEventListener("change",loadSubmitRevisar);
    
    document.getElementById("selectPolarRF").addEventListener("change",loadSubmitRevisar);
    document.getElementById("selectTreeRF").addEventListener("change",loadSubmitRevisar);
    document.getElementById("selectMaxDepthRF").addEventListener("change",loadSubmitRevisar);
    document.getElementById("selectFeatureRF").addEventListener("change",loadSubmitRevisar);
    document.getElementById("selectSamSplitRF").addEventListener("change",loadSubmitRevisar);
    document.getElementById("selectSamLeafRF").addEventListener("change",loadSubmitRevisar);
    
    document.getElementById("selectPolarLG").addEventListener("change",loadSubmitRevisar);
    document.getElementById("selectParamCLG").addEventListener("change",loadSubmitRevisar);
}

function load(){
    document.getElementById("selectIteracSVC").addEventListener("change",loadSubmitRevisar);
    document.getElementById("selectPolarSVC").addEventListener("change",loadSubmitRevisar);
    
    document.getElementById("selectPolarNB").addEventListener("change",loadSubmitRevisar);
    
    document.getElementById("selectPolarRF").addEventListener("change",loadSubmitRevisar);
    document.getElementById("selectTreeRF").addEventListener("change",loadSubmitRevisar);
    document.getElementById("selectMaxDepthRF").addEventListener("change",loadSubmitRevisar);
    document.getElementById("selectFeatureRF").addEventListener("change",loadSubmitRevisar);
    document.getElementById("selectSamSplitRF").addEventListener("change",loadSubmitRevisar);
    document.getElementById("selectSamLeafRF").addEventListener("change",loadSubmitRevisar);
    
    document.getElementById("selectPolarLG").addEventListener("change",loadSubmitRevisar);
    document.getElementById("selectParamCLG").addEventListener("change",loadSubmitRevisar);
}

function revisar(){
    if(document.getElementById("selectAlgorit").value == "Modelo Linear SVC"){
        document.getElementById("groupSVC").style.display="block";
        document.getElementById("groupRF").style.display="none";
        document.getElementById("groupNB").style.display="none";
        document.getElementById("groupLG").style.display="none";
        
        document.getElementById("button-submit").style.display="none";
        document.getElementById("button-gen").style.display="none";
        
        document.getElementById("selectIteracSVC").value = "title";
        document.getElementById("selectPolarSVC").value = "title";
        
        document.getElementById("selectPolarNB").value = "title";
        
        document.getElementById("selectPolarRF").value = 'title';
        document.getElementById("selectTreeRF").value = 'title';
        document.getElementById("selectMaxDepthRF").value = "title";
        document.getElementById("selectFeatureRF").value = "title";
        document.getElementById("selectSamSplitRF").value = "title";
        document.getElementById("selectSamLeafRF").value = "title";
        
        document.getElementById("selectPolarLG").value = "title";
        document.getElementById("selectParamCLG").value = "title";
        
    }else if(document.getElementById("selectAlgorit").value == "Random Forest"){
    	document.getElementById("groupRF").style.display="block";
    	document.getElementById("groupSVC").style.display="none";
        document.getElementById("groupNB").style.display="none";
        document.getElementById("groupLG").style.display="none";
        
        document.getElementById("button-submit").style.display="none";
        document.getElementById("button-gen").style.display="none";
        
        document.getElementById("selectIteracSVC").value = "title";
        document.getElementById("selectPolarSVC").value = "title";
        
        document.getElementById("selectPolarNB").value = "title";
        
        document.getElementById("selectPolarRF").value = 'title';
        document.getElementById("selectTreeRF").value = "title";
        document.getElementById("selectMaxDepthRF").value = "title";
        document.getElementById("selectFeatureRF").value = "title";
        document.getElementById("selectSamSplitRF").value = "title";
        document.getElementById("selectSamLeafRF").value = "title";
        
        document.getElementById("selectPolarLG").value = "title";
        document.getElementById("selectParamCLG").value = "title";
        
        
    }else if(document.getElementById("selectAlgorit").value=="Naives Bayes"){
    	document.getElementById("groupNB").style.display="block";
    	document.getElementById("groupSVC").style.display="none";
        document.getElementById("groupRF").style.display="none";  
        document.getElementById("groupLG").style.display="none";
    	
        document.getElementById("button-submit").style.display="none";
        document.getElementById("button-gen").style.display="none";
        
        document.getElementById("selectIteracSVC").value = "title";
        document.getElementById("selectPolarSVC").value = "title";
        
        document.getElementById("selectPolarNB").value = "title";
        
        document.getElementById("selectPolarRF").value = 'title';
        document.getElementById("selectTreeRF").value = "title";
        document.getElementById("selectMaxDepthRF").value = "title";
        document.getElementById("selectFeatureRF").value = "title";
        document.getElementById("selectSamSplitRF").value = "title";
        document.getElementById("selectSamLeafRF").value = "title";
        
        document.getElementById("selectPolarLG").value = "title";
        document.getElementById("selectParamCLG").value = "title";
        
    }else if(document.getElementById("selectAlgorit").value=="Logistic Regression"){
    	document.getElementById("groupLG").style.display="block";
    	document.getElementById("groupNB").style.display="none";
    	document.getElementById("groupSVC").style.display="none";
        document.getElementById("groupRF").style.display="none";    
    	
        document.getElementById("button-submit").style.display="none";
        document.getElementById("button-gen").style.display="none";
        
        document.getElementById("selectIteracSVC").value = "title";
        document.getElementById("selectPolarSVC").value = "title";
        
        document.getElementById("selectPolarNB").value = "title";
        
        document.getElementById("selectPolarRF").value = 'title';
        document.getElementById("selectTreeRF").value = "title";
        document.getElementById("selectMaxDepthRF").value = "title";
        document.getElementById("selectFeatureRF").value = "title";
        document.getElementById("selectSamSplitRF").value = "title";
        document.getElementById("selectSamLeafRF").value = "title";
        
        document.getElementById("selectPolarLG").value = "title";
        document.getElementById("selectParamCLG").value = "title";
        
    }else{
         document.getElementById("groupSVC").style.display="none";
         document.getElementById("groupRF").style.display="none"; 
         document.getElementById("groupNB").style.display="none";
         document.getElementById("groupLG").style.display="none";
         
         document.getElementById("button-submit").style.display="none";
         document.getElementById("button-gen").style.display="block";
         
         document.getElementById("selectIteracSVC").value = "title";
         document.getElementById("selectPolarSVC").value = "title";
         
         document.getElementById("selectPolarNB").value = "title";
         
         document.getElementById("selectPolarRF").value = 'title';
         document.getElementById("selectTreeRF").value = "title";
         document.getElementById("selectMaxDepthRF").value = "title";
         document.getElementById("selectFeatureRF").value = "title";
         document.getElementById("selectSamSplitRF").value = "title";
         document.getElementById("selectSamLeafRF").value = "title";
         
         document.getElementById("selectPolarLG").value = "title";
         document.getElementById("selectParamCLG").value = "title";
    }
}

function load() { 
	var botonText = document.getElementById("text"); 
	botonText.addEventListener("click", function(){
        document.getElementById("groupSVC").style.display="none";
		document.getElementById("groupNB").style.display="none";
		document.getElementById("groupRF").style.display="none";
		document.getElementById("groupLG").style.display="none";
		
        document.getElementById("button-submit").style.display="none";
        
        document.getElementById("selectAlgorit").value = "none";
        
        document.getElementById("selectIteracSVC").value = "title";
        document.getElementById("selectPolarSVC").value = "title";
        
        document.getElementById("selectPolarNB").value = "title";
        
        document.getElementById("selectPolarRF").value = 'title';
        document.getElementById("selectTreeRF").value = "title";
        document.getElementById("selectMaxDepthRF").value = "title";
        document.getElementById("selectFeatureRF").value = "title";
        document.getElementById("selectSamSplitRF").value = "title";
        document.getElementById("selectSamLeafRF").value = "title";
        
        document.getElementById("selectPolarLG").value = "title";
        document.getElementById("selectParamCLG").value = "title";
        
	}, false); 
} 

function loadSubmitRevisar(){
	
	
    if(document.getElementById("selectIteracSVC").value != "title" && 
    		document.getElementById("selectPolarSVC").value != "title" &&
    		document.getElementById("selectAlgorit").value == "Modelo Linear SVC"){
    	
    	document.getElementById("button-submit").style.display="block";
    	document.getElementById("button-gen").style.display="none";
    	
    }else if(document.getElementById("selectPolarNB").value != "title" &&
    		document.getElementById("selectAlgorit").value == "Naives Bayes"){
    	
    	document.getElementById("button-submit").style.display="block";
    	document.getElementById("button-gen").style.display="none";
    	
    }else if(document.getElementById("selectPolarRF").value != 'title' &&
    		document.getElementById("selectTreeRF").value != "title" &&
    		document.getElementById("selectMaxDepthRF").value != "title" &&
    		document.getElementById("selectFeatureRF").value != "title" &&
    		document.getElementById("selectSamSplitRF").value != "title" &&
    		document.getElementById("selectSamLeafRF").value != "title" &&
    		document.getElementById("selectAlgorit").value == "Random Forest"){
    	
    	document.getElementById("button-submit").style.display="block";
    	document.getElementById("button-gen").style.display="none";
    	
    }else if(document.getElementById("selectPolarLG").value != "title" &&
    		document.getElementById("selectParamCLG").value != "title" &&
    		document.getElementById("selectAlgorit").value == "Logistic Regression"){
    	
    	document.getElementById("button-submit").style.display="block";
    	document.getElementById("button-gen").style.display="none";
    	
    }else if(document.getElementById("selectAlgorit").value == "none"){
    	
    	document.getElementById("button-gen").style.display="block";
    	document.getElementById("button-submit").style.display="none";
    	
    }else{
    	 document.getElementById("button-submit").style.display="none";
    	 document.getElementById("button-gen").style.display="none";
    	 
    }
}

    


