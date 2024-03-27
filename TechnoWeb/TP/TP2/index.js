
let nbActionsAjoutBatons = 3;

function genererBatons() {
    const nbBatons = parseInt(document.querySelector('.choix-batons #nb_batons_commencer').value);
    const containerElement = document.querySelector('.container');
    
    // Décrémenter le nombre d'actions disponibles
    nbActionsAjoutBatons--;

    // Mettre à jour l'affichage du nombre d'actions restantes
    document.getElementById('nb_actions_restantes').textContent = nbActionsAjoutBatons;


    for (let i = 0; i < nbBatons; i++) {
        const batonElement = document.createElement('div');
        batonElement.style.opacity = 0;

        batonElement.classList.add('batons');
        setTimeout(() => {
            batonElement.style.opacity = 1; // Animer l'opacité à 1
        }, i * 100);

        containerElement.appendChild(batonElement);
    }   

    if (nbActionsAjoutBatons === 0) {
        document.getElementById('btn_ajouter_batons').disabled = true;
    }
} 


    





function supprimerBatons() {
    const nbBatonsASupprimer = parseInt(document.getElementById('nb_batons_supprimer').value);
    var nbBatonsRestants = parseInt(document.querySelector('.choix-batons #nb_batons_commencer').value); // nb batons sur le terrain de jeux
    // Vérifier la validité du nombre saisi
    if (nbBatonsASupprimer <= 0 || nbBatonsASupprimer > 3) {
        alert( "Nombre invalide. Veuillez choisir un nombre entre 1 et 3, et inférieur au nombre de batons restants.");
    } 
    
    
    const batonsElementsArray = Array.from(document.querySelectorAll('.batons'));
    // Récupérer les éléments à supprimer
    if (batonsElementsArray.length >= nbBatonsASupprimer){
        const elementsASupprimer = batonsElementsArray.slice(batonsElementsArray.length - nbBatonsASupprimer);
        // Définir l'opacité à 0 pour les éléments à supprimer
        for (let i = 0; i < elementsASupprimer.length; i++) {
            elementsASupprimer[i].style.opacity = 0;
        }
        setTimeout(() => {
            // Supprimer les éléments en une seule fois
            for (let i = 0; i < elementsASupprimer.length; i++) {
                    elementsASupprimer[i].parentNode.removeChild(elementsASupprimer[i]);
            }
            

        }, 500);
    
        nbBatonsRestants = batonsElementsArray.length - nbBatonsASupprimer;
        if(nbBatonsRestants === 1){
            alert("Félicitations, vous avez gagné !");
            rejouer()
        }if(nbBatonsRestants === 0){
            alert("Dommage, vous avez perdu !");
            rejouer()
        }
        console.log(nbBatonsRestants)
    }

    
    else if(batonsElementsArray.length < nbBatonsASupprimer){
        alert("Vous ne pouvez pas supprimer plus de batons qu'il n'en reste.");
    }
 
}



function rejouer(){
    location.reload();
}








