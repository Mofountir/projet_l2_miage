function redirectToGame(nbBatons) {
    const url = `reste${nbBatons}.html`;
    window.location.href = url;
}

function redirectHome() {
    window.location.href = 'index.html';
}
  
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
        batonElement.classList.add('batons');
        containerElement.appendChild(batonElement);
    }   

    if (nbActionsAjoutBatons === 0) {
        document.getElementById('btn_ajouter_batons').disabled = true;
    }
} 


    





function supprimerBatons() {
    const nbBatonsASupprimer = parseInt(document.getElementById('nb_batons_supprimer').value);
    const nbBatonsRestants = parseInt(document.querySelector('.choix-batons #nb_batons_commencer').value); // nb batons sur le terrain de jeux
  
    // Vérifier la validité du nombre saisi
    if (nbBatonsASupprimer <= 0 || nbBatonsASupprimer > 3 || nbBatonsASupprimer > nbBatonsRestants) {
      alert("Nombre invalide. Veuillez choisir un nombre entre 1 et 3, et inférieur au nombre de batons restants.");
      return;
    }
  
    // **Convertir NodeList en tableau**
    const batonsElementsArray = Array.from(document.querySelectorAll('.batons'));
  
    // **Récupérer les éléments à supprimer**
    const elementsASupprimer = batonsElementsArray.slice(batonsElementsArray.length - nbBatonsASupprimer);
  
    // **Supprimer les éléments en une seule fois**
    for (const element of elementsASupprimer) {
      element.parentNode.removeChild(element);
    }
  
    // Mettre à jour le nombre de batons restants
    nbBatonsRestants = nbBatonsRestants - nbBatonsASupprimer;
  }
  


