#========================================================================================
# Nom : FOUNTIR 
# Pénom : Mohamed
# Groupe: Licence 2 Miage
#                                    DEVOIR MAISON
#=========================================================================================

# EXERCICE 1 =============================================================================
#ici on aura Xn une v.a ~ N(m = 2, ??² = 3) avec n de 1 -> 50
#  on admet que la moyenne de Xn suit la même loi normal
# on cherche l'intervalle de confiance IC = [a,b] de niveau 100.(1 ??? ??)% pour m

m <- 2 #moyenne
alphas <- c(0.01, 0.05, 0.1) # Différents niveaux de confiance
ns <- c(50, 100, 200) # Différentes tailles d'échantillon
sigma2s <- c(3, 5, 10) # Différentes valeurs de variance
B <- 100 #taille de l'echontillons

# Fonction pour calculer l'intervalle de confiance pour m
IC <- function(x, alpha) {
  ecart <- sqrt(sigma2 / length(x)) # Ecart type de la moyenne de Xn 
  Z <- qnorm(1 - alpha / 2) # Fractil d'ordre 1-??/2 
  A <- Z * ecart # Marge d'estimation 
  a <- mean(x) - A 
  b <- mean(x) + A
  return(c(a, b))
}

# Boucle sur les différents paramètres
for (alpha in alphas) {
  for (n in ns) {
    for (sigma2 in sigma2s) {
      # Simulation des échantillons
      set.seed(12) # Pour la reproductibilité des résultats
      echantillons <- matrix(rnorm(n * B, mean = m, sd = sqrt(sigma2)), ncol = B)
      
      # Calcul des intervalles de confiance
      IC_95 <- apply(echantillons, 2, IC, alpha = alpha)
      
      # Graphique des intervalles de confiance
      plot(1:B, IC_95[1, ], ylim = c(0, 4), type = "n", xlab = "Numéro de l'échantillon", ylab = "Intervalle de confiance pour m", main = paste("Intervalle de confiance pour m avec alpha =", alpha, ", n =", n, ", sigma2 =", sigma2))
      abline(h = m, lty = 2, col = 'blue') # Ligne horizontale à y = m en pointillés
      segments(1:B, IC_95[1, ], 1:B, IC_95[2, ]) # Tracer des intervalles de confiance
      
      # Calcul de la proportion d'intervalles de confiance qui ne contiennent pas la vraie valeur de m
      proportion <- mean(m < IC_95[1, ] | m > IC_95[2, ])
      cat("Proportion d'intervalles de confiance qui ne contiennent pas la vraie valeur de m :", proportion, "\n")
      
      # Pause entre les graphiques
      Sys.sleep(2)
    }
  }
}


# EXERCICE 2 ============================================================================
#-------------------------------------MONTE-CARLO ---------------------------------------


# Ici on considère les Xi iid ~ N(m = 0 et ??² = 1) avec i de 1 -> 1000

# Simuler B échantillions de taille N = 1000:
B <- 1000
N <- 1000

iterations <- 1:B

s2n_monte_carlo <- numeric(B) # Vecteur pour stocker les valeurs de s2
biais_monte_carlo <- numeric(B) # Vecteur pour stocker les valeurs des biais 

for (l in iterations) {
  # génerer les échontillons
  sample <- rnorm(N, mean = 0, sd = 1) 
  
  # calculer s2n pour chaque valeur de l de {1,..,B}
  s2n_monte_carlo[l] <- (1/N) * sum((sample - mean(sample))^2)
  
  # Calcul de l'estimation de la variation de biais en finction de B (biais = -??²/B ~ 0.001)
  biais_monte_carlo[l] <- (1/l)* sum(s2n_monte_carlo[1:l])-1
}


par(mfrow = c(2, 2))

# Affichage des graphiques
# Graphique 1 : Estimation de la variance en fonction du nombre d'itérations
plot(1:B, s2n_monte_carlo, type = "l", xlab = "Nombre d'itérations", ylab = "Estimation de la variance (Monte-Carlo)", 
     main = "Estimation de la variance (Monte-Carlo)")
lines(1:B, rep(1, B), col = "red") # Vraie valeur de la varianc- 1e

# Graphique 2 : Biais en fonction du nombre d'itérations (Monte-Carlo)
plot(1:B, biais_monte_carlo, type = "l", xlab = "Nombre d'itérations", ylab = "Biais (Monte-Carlo)", 
     main = "Biais en fonction du nombre d'itérations (Monte-Carlo)")
abline(h = -1/B, col = "blue") # Ligne pour montrer la convergence vers zéro




#-------------------------------------BOOTSTRAP----------------------------------------


# Simulation de l'échantillon initial
XX <- rnorm(100, mean = 0, sd = 1)

# Nombre d'itérations Bootstrap
B <- 100
s2n <- sum((XX - mean(XX))^2) / length(XX)
cat('??²(XX) = ', s2n)

s2n_bootstrap <- numeric(B) # Vecteur pour stocker les valeurs de s2
biais_bootstrap <- numeric(B) # Vecteur pour stocker les valeurs des biais 

# Boucle sur les échantillons Bootstrap simulés
for (l in 1:B) {
  # Simulation d'un échantillon Bootstrap de taille 100 avec remise
  bootstrap_sample <- sample(XX, size = 100, replace = TRUE)
  
  # Calcul de s2n(l) Bootstrap
  s2n_bootstrap[l] <- sum((bootstrap_sample - mean(bootstrap_sample))^2) / length(bootstrap_sample)
  # Calcul de l'estimation du biais Bootstrap (biais = -??²/B ~ 0.01)
  biais_bootstrap[l] <- (1/l)* sum(s2n_bootstrap[1:l])- 1
}



# Affichage des graphiques

# Graphique 3 : Estimation de la variance en fonction du nombre d'itérations (Bootstrap)
plot(1:B, s2n_bootstrap, type = "l", xlab = "Nombre d'itérations", ylab = "Estimation de la variance (Bootstrap)", 
     main = "Estimation de la variance (Bootstrap)")
lines(1:B, rep(1, B), col = "red") # Vraie valeur de la variance

# Graphique 4 : Biais en fonction du nombre d'itérations (Bootstrap)
plot(1:B, biais_bootstrap, type = "l", xlab = "Nombre d'itérations", ylab = "Biais (Bootstrap)", 
     main = "Biais en fonction du nombre d'itérations (Bootstrap)")
abline(h = -1/B, col = "blue") # Ligne pour montrer la convergence vers zéro



# EXERCICE 3 ============================================================================
# On veut regarder s'il existe une liaison éventuelle entre le taux de fibre oxydative (X) et la
# teneur en lipides dans la chair de lapins (Y).
# On a pour cela effectuer des mesures sur 9 chairs de lapin.

# Nuages de points de ces observation:-------------------------------------------------------------
# Données
X <- c(3, 4, 4, 17, 24, 45, 55, 68, 73)
Y <- c(0.9, 1.3, 1.0, 2.4, 2.8, 4.4, 5.2, 6.3, 6.6)

plot(X, Y, main = "Nuage de points X,Y", xlab = "Taux de fibre oxydative (X)", ylab = "Teneur en lipides (Y)")

# 2. Régression linéaire:----------------------------------------------------------------------------
modele <- lm(Y ~ X) # droite de regression 
abline(modele, col='red')
modele$coefficients
modele$residuals
confint.default(modele)
# 3. Prédiction pour X = 28:-------------------------------------------------------------------------
X_new <- 28
Y_pred <- predict(modele, data.frame(X = X_new))
cat("La valeur prédite de Y pour X =", X_new, "est", Y_pred, "\n")

# 4. Écarts entre les observations et les prédictions:-----------------------------------------------
ecarts <- resid(modele)
residues <- modele$residuals
identical(ecarts, residues) # Comparaison avec lm$residuals

# 5. approximation de la loi de distribution des résidues:-------------------------------------------
# Histogramme des résidus
# Calcul de la moyenne et de la médiane des résidus
mean_residues <- mean(residues)
variance_residues <- var(residues)
cat(mean_residues)
cat(variance_residues)

# Histogramme des résidus
hist(residues, main = "Histogramme des résidus", xlab = "Résidus", ylab = "Fréquence")

# Ajout de la courbe de densité en rouge
lines(density(residues), col = "red", lwd = 2)

# Ajout de la moyenne et de la médiane
abline(v = mean_residues, col = "green", lwd = 2, lty = 2, label = "Moyenne")

# test Shapiro-Wilk si p-value > 0.05 donc on peut dire que la distribution suit approximativement N(0,1)
shapiro.test(residues)


# 6. Calcul de b------------------------------------------------------------------------------------------
XX <- cbind(rep(1, length(X)), X)
YY <- matrix(Y, ncol = 1)
b <- solve(t(XX) %*% XX) %*% t(XX) %*% YY
cat(b)
summary(modele) # Comparaison avec les coefficients de lm







