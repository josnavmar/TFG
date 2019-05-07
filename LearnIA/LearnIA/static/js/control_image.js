window.addEventListener("load", init2);
window.addEventListener("load", load2);
window.addEventListener("load", loadSubmit2);

function init2() {
	document.getElementById("selectSentGen")
			.addEventListener("change", revisar2);
	document.getElementById("button-submit").style.display = "none";
	document.getElementById("simpleCNNSent").style.display = "none";
	document.getElementById("miniXCNNSent").style.display = "none";
	document.getElementById("bigXCNNSent").style.display = "none";
	document.getElementById("simpleCNNGen").style.display = "none";
	document.getElementById("miniXCNNGen").style.display = "none";
	document.getElementById("bigXCNNGen").style.display = "none";
	
	document.getElementById("sgdSent").style.display = "none";
	document.getElementById("rmsPropSent").style.display = "none";
	document.getElementById("adamSent").style.display = "none";
	document.getElementById("sgdGen").style.display = "none";
	document.getElementById("rmsPropGen").style.display = "none";
	document.getElementById("adamGen").style.display = "none";
}

function loadSubmit2() {
	document.getElementById("selectIterSent").addEventListener("change", loadSubmitRevisar2);
	document.getElementById("selectOptimSent").addEventListener("change", loadSubmitRevisar2);
	document.getElementById("selectRedSent").addEventListener("change", loadSubmitRevisar2);

	document.getElementById("selectIterGen").addEventListener("change", loadSubmitRevisar2);
	document.getElementById("selectOptimGen").addEventListener("change", loadSubmitRevisar2);
	document.getElementById("selectRedGen").addEventListener("change", loadSubmitRevisar2);

}
function load2() {
	document.getElementById("selectIterSent").addEventListener("change",
			loadSubmitRevisar2);
	document.getElementById("selectOptimSent").addEventListener("change",
			loadSubmitRevisar2);
	document.getElementById("selectRedSent").addEventListener("change",
			loadSubmitRevisar2);

	document.getElementById("selectIterGen").addEventListener("change",
			loadSubmitRevisar2);
	document.getElementById("selectOptimGen").addEventListener("change",
			loadSubmitRevisar2);
	document.getElementById("selectRedGen").addEventListener("change",
			loadSubmitRevisar2);

}

function revisar2() {
	if (document.getElementById("selectSentGen").value == "Sentimiento") {

		document.getElementById("groupSent").style.display = "block";
		document.getElementById("groupGen").style.display = "none";

		document.getElementById("button-submit").style.display = "none";

		document.getElementById("selectIterSent").value = "title";
		document.getElementById("selectOptimSent").value = "title";
		document.getElementById("selectRedSent").value = "title";

		document.getElementById("selectIterGen").value = "title";
		document.getElementById("selectOptimGen").value = "title";
		document.getElementById("selectRedGen").value = "title";
		
		document.getElementById("simpleCNNSent").style.display = "none";
		document.getElementById("miniXCNNSent").style.display = "none";
		document.getElementById("bigXCNNSent").style.display = "none";
		document.getElementById("sgdSent").style.display = "none";
		document.getElementById("rmsPropSent").style.display = "none";
		document.getElementById("adamSent").style.display = "none";


	} else if (document.getElementById("selectSentGen").value == "Genero") {
		document.getElementById("groupSent").style.display = "none";
		document.getElementById("groupGen").style.display = "block";

		document.getElementById("button-submit-2").style.display = "none";

		document.getElementById("selectIterSent").value = "title";
		document.getElementById("selectOptimSent").value = "title";
		document.getElementById("selectRedSent").value = "title";

		document.getElementById("selectIterGen").value = "title";
		document.getElementById("selectOptimGen").value = "title";
		document.getElementById("selectRedGen").value = "title";
		
		document.getElementById("simpleCNNGen").style.display = "none";
		document.getElementById("miniXCNNGen").style.display = "none";
		document.getElementById("bigXCNNGen").style.display = "none";
		document.getElementById("sgdGen").style.display = "none";
		document.getElementById("rmsPropGen").style.display = "none";
		document.getElementById("adamGen").style.display = "none";

	} else {
		document.getElementById("groupSent").style.display = "none";
		document.getElementById("groupGen").style.display = "none";

		document.getElementById("button-submit-2").style.display = "none";

		document.getElementById("selectIterSent").value = "title";
		document.getElementById("selectOptimSent").value = "title";
		document.getElementById("selectRedSent").value = "title";

		document.getElementById("selectIterGen").value = "title";
		document.getElementById("selectOptimGen").value = "title";
		document.getElementById("selectRedGen").value = "title";
		
		document.getElementById("simpleCNNSent").style.display = "none";
		document.getElementById("miniXCNNSent").style.display = "none";
		document.getElementById("bigXCNNSent").style.display = "none";
		
		document.getElementById("simpleCNNGen").style.display = "none";
		document.getElementById("miniXCNNGen").style.display = "none";
		document.getElementById("bigXCNNGen").style.display = "none";
		
		document.getElementById("sgdSent").style.display = "none";
		document.getElementById("rmsPropSent").style.display = "none";
		document.getElementById("adamSent").style.display = "none";
		
		document.getElementById("sgdGen").style.display = "none";
		document.getElementById("rmsPropGen").style.display = "none";
		document.getElementById("adamGen").style.display = "none";
	}
}

function load2() {
	var botonText = document.getElementById("image");
	botonText.addEventListener("click", function() {
		document.getElementById("groupSent").style.display = "none";
		document.getElementById("groupGen").style.display = "none";

		document.getElementById("button-submit-2").style.display = "none";

		document.getElementById("selectSentGen").value = "none";

		document.getElementById("selectIterSent").value = "title";
		document.getElementById("selectOptimSent").value = "title";
		document.getElementById("selectRedSent").value = "title";

		document.getElementById("selectIterGen").value = "title";
		document.getElementById("selectOptimGen").value = "title";
		document.getElementById("selectRedGen").value = "title";


	}, false);
}

function loadSubmitRevisar2() {

	if (document.getElementById("selectIterSent").value != "title"
			&& document.getElementById("selectOptimSent").value != "title"
			&& document.getElementById("selectRedSent").value != "title"
			&& document.getElementById("selectSentGen").value == "Sentimiento") {

		document.getElementById("button-submit-2").style.display = "block";

	} else if (document.getElementById("selectIterGen").value != "title"
			&& document.getElementById("selectOptimGen").value != "title"
			&& document.getElementById("selectRedGen").value != "title"
			&& document.getElementById("selectSentGen").value == "Genero") {

		document.getElementById("button-submit-2").style.display = "block";

	} else {
		document.getElementById("button-submit-2").style.display = "none";

	}
	
	//Definicion de red neuronal
	//Sentimiento
	
	if (document.getElementById("selectRedSent").value == "Simple CNN"){
		document.getElementById("simpleCNNSent").style.display = "block";
		document.getElementById("miniXCNNSent").style.display = "none";
		document.getElementById("bigXCNNSent").style.display = "none";
	}else if (document.getElementById("selectRedSent").value == "Mini XCEPTION CNN"){
		document.getElementById("miniXCNNSent").style.display = "block";
		document.getElementById("simpleCNNSent").style.display = "none";
		document.getElementById("bigXCNNSent").style.display = "none";
	}else if (document.getElementById("selectRedSent").value == "Big XCEPTION CNN"){
		document.getElementById("bigXCNNSent").style.display = "block";
		document.getElementById("simpleCNNSent").style.display = "none";
		document.getElementById("miniXCNNSent").style.display = "none";
	}else{
		document.getElementById("simpleCNNSent").style.display = "none";
		document.getElementById("miniXCNNSent").style.display = "none";
		document.getElementById("bigXCNNSent").style.display = "none";
	}
	
	// Genero
	
	if (document.getElementById("selectRedGen").value == "Simple CNN"){
		document.getElementById("simpleCNNGen").style.display = "block";
		document.getElementById("miniXCNNGen").style.display = "none";
		document.getElementById("bigXCNNGen").style.display = "none";
	}else if (document.getElementById("selectRedGen").value == "Mini XCEPTION CNN"){
		document.getElementById("miniXCNNGen").style.display = "block";
		document.getElementById("simpleCNNGen").style.display = "none";
		document.getElementById("bigXCNNGen").style.display = "none";
	}else if (document.getElementById("selectRedGen").value == "Big XCEPTION CNN"){
		document.getElementById("bigXCNNGen").style.display = "block";
		document.getElementById("simpleCNNGen").style.display = "none";
		document.getElementById("miniXCNNGen").style.display = "none";
	}else{
		document.getElementById("simpleCNNGen").style.display = "none";
		document.getElementById("miniXCNNGen").style.display = "none";
		document.getElementById("bigXCNNGen").style.display = "none";
	}
	
	//Definicion de optimizadores
	//Sentimiento
	
	if (document.getElementById("selectOptimSent").value == "SGD"){
		document.getElementById("sgdSent").style.display = "block";
		document.getElementById("rmsPropSent").style.display = "none";
		document.getElementById("adamSent").style.display = "none";
	}else if (document.getElementById("selectOptimSent").value == "RMSprop"){
		document.getElementById("sgdSent").style.display = "none";
		document.getElementById("rmsPropSent").style.display = "block";
		document.getElementById("adamSent").style.display = "none";
	}else if (document.getElementById("selectOptimSent").value == "Adam"){
		document.getElementById("sgdSent").style.display = "none";
		document.getElementById("rmsPropSent").style.display = "none";
		document.getElementById("adamSent").style.display = "block";
	}else{
		document.getElementById("sgdSent").style.display = "none";
		document.getElementById("rmsPropSent").style.display = "none";
		document.getElementById("adamSent").style.display = "none";
	}
	
	//Genero
	
	if (document.getElementById("selectOptimGen").value == "SGD"){
		document.getElementById("sgdGen").style.display = "block";
		document.getElementById("rmsPropGen").style.display = "none";
		document.getElementById("adamGen").style.display = "none";
	}else if (document.getElementById("selectOptimGen").value == "RMSprop"){
		document.getElementById("sgdGen").style.display = "none";
		document.getElementById("rmsPropGen").style.display = "block";
		document.getElementById("adamGen").style.display = "none";
	}else if (document.getElementById("selectOptimGen").value == "Adam"){
		document.getElementById("sgdGen").style.display = "none";
		document.getElementById("rmsPropGen").style.display = "none";
		document.getElementById("adamGen").style.display = "block";
	}else{
		document.getElementById("sgdGen").style.display = "none";
		document.getElementById("rmsPropGen").style.display = "none";
		document.getElementById("adamGen").style.display = "none";
	}
	
	
}
