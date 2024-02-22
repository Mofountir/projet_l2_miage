
window.onload = function () {
	
	// les noms des fichiers images
	var sources = ["paysage-1.jpg", "paysage-2.jpg", "paysage-3.jpg",
		"paysage-4.jpg", "paysage-5.jpg", "paysage-6.jpg",
		"paysage-7.jpg", "paysage-8.jpg", "paysage-9.jpg"];

	sources = sources.map(function(image){
		return "images/" + image;
	});

	// l'indice de l'image actuellement visible
	var indices = 0;

	// délai d'affichage de chaque image
	var delai = 2000;

	// affiche l'image suivante
	function next() {
		indices = (indices + 1) % sources.length;
		document.getElementById("show").src = sources[indices];

	}
	// lancement auto du diapo

	var interval = setInterval(next, delai);

	// arreter le diapo
	function stop() {
		clearInterval(interval);
	}

	// boutton pour démarer et arreter le diapo
	document.getElementById("start").onclick = function() {
		interval = setInterval(next, delai);
	}

	document.getElementById("stop").onclick = stop;

	// arret en cliquant sur l'image
	document.getElementById("show").onclick = stop;

	//affichage le l'image initial
	next();

	// affiche l'image précédente
	function previous() {
		indices = (indices - 1 + sources.length) % sources.length;
		document.getElementById("show").src = sources[indices];
	}

	// ici, il faut relier le JS à l'évènement "onclick" sur
	// les deux "flèches" (les images)
	document.getElementById("arrow-right").onclick = next;
	document.getElementById("arrow-left").onclick = previous;



};
