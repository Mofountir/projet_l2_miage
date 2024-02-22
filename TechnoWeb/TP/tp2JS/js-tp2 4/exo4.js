
window.onload = function () {

	// affiche le nombre "t" dans le span "spanElt"
	// "t" a au plus deux chiffres
	function afficher(t, spanElt) {
		var str = t.toString();
		

		spanElt[0].src = 'images/' + str[0] + '.png'
		spanElt[1].src = 'images/' + str[1] + '.png'
		
		console.log(str[0]);
		console.log(str[1]);

		
	}

	

	// met à jour les images de l'horloge
	// à chaque seconde
	function tictac() {
		var date = new Date();

		var heures = date.getHours();
		var minutes = date.getMinutes();
		var secondes = date.getSeconds();

		images = Array.from(document.querySelectorAll('span img'))
		
		afficher(heures, images.slice(0,2));
		afficher(minutes, images.slice(2,4));
		afficher(secondes, images.slice(4,6));

	}

	// ici, il faut lancer l'horloge
	setInterval(tictac, 1000);

	//tictac();

};
