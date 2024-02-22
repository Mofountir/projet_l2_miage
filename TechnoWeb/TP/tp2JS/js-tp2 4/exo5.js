
window.onload = function () {

	// le "handler" du setTimeout
	let chrono = null;

	// si 'ok' est 'true', alors l'utilisateur
	// a choisi la bonne réponse
	//let ok = false;

	// affiche le message 'm' avec la couleur 'c'
	// dans l'élément prévu à cet effet
	function msg(m, c) {
		const element = document.getElementById("message");
		element.textContent = m;
		element.style.color = c;

	}

	// cette fonction est appelée à l'issue
	// du setTimeout
	function stop() {
		clearTimeout(chrono);
		verifier();
	}

	// traite le "clic" sur un bouton radio
	function verifier() {
        const choix = document.querySelector('input[name="reponse"]:checked').value;
        ok = choix === document.querySelector("input[name='reponse'][data-ok]").value;

        if (ok) {
            msg("Bravo, vous avez trouvé la bonne réponse !", "green");
        } 
		else {
            msg("Mauvaise réponse. Veuillez réessayer.", "red");
        }
    }

	// ici, on lance le setTimeout et stocke
	// le "handler" dans la variable 'chrono'
	chrono = setTimeout(stop, 5000); // 10 secondes
	setInterval(chrono, 1000);

	

};
