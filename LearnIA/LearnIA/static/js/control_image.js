window.addEventListener("load", init2);
window.addEventListener("load", load2);
window.addEventListener("load", loadSubmit2);

function init2() {
	document.getElementById("selectSentGen")
			.addEventListener("change", revisar2);
	document.getElementById("button-submit-2").style.display = "none";
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

		document.getElementById("button-submit-2").style.display = "none";

		document.getElementById("selectIterSent").value = "title";
		document.getElementById("selectOptimSent").value = "title";
		document.getElementById("selectRedSent").value = "title";

		document.getElementById("selectIterGen").value = "title";
		document.getElementById("selectOptimGen").value = "title";
		document.getElementById("selectRedGen").value = "title";

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
}
