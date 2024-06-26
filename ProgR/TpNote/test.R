# Nombre d'�chantillons Monte-Carlo
B <- 1000
# Taille de chaque �chantillon
N <- 1000

# Simulation de l'�chantillon initial
XX <- rnorm(100, mean = 0, sd = 1)
# Calcul de s^2 � partir de XX
s2 <- sum((XX - mean(XX))^2) / length(XX)

# Initialisation des vecteurs pour stocker les valeurs de s^2
s2_monte_carlo <- numeric(B)
biais_monte_carlo <- numeric(B)
s2_bootstrap <- numeric(B)
biais_bootstrap <- numeric(B)

# Boucle sur les �chantillons Monte-Carlo simul�s
for (l in 1:B) {
  # G�n�ration d'un �chantillon de taille N suivant une loi normale N(0, 1)
  sample <- rnorm(N, mean = 0, sd = 1) 
  
  # Calcul de s^2 pour la m�thode Monte-Carlo
  s2_monte_carlo[l] <- sum((sample - mean(sample))^2) / N
  
  # Calcul du biais pour la m�thode Monte-Carlo
  biais_monte_carlo[l] <- mean(s2_monte_carlo[1:l]) - 1
  
  # Simulation d'un �chantillon Bootstrap de taille 100 avec remise
  bootstrap_sample <- sample(XX, size = 100, replace = TRUE)
  
  # Calcul de s^2 pour la m�thode Bootstrap
  s2_bootstrap[l] <- sum((bootstrap_sample - mean(bootstrap_sample))^2) / length(bootstrap_sample)
  
  # Calcul du biais pour la m�thode Bootstrap
  biais_bootstrap[l] <- mean(s2_bootstrap[1:l]) - s2
}

# Affichage des graphiques

par(mfrow = c(2, 2))

# Graphique 1 : Estimation de la variance en fonction du nombre d'it�rations
plot(1:B, s2_monte_carlo, type = "l", xlab = "Nombre d'it�rations", ylab = "Estimation de la variance (Monte-Carlo)", 
     main = "Estimation de la variance (Monte-Carlo)")
lines(1:B, rep(1, B), col = "red") # Vraie valeur de la variance

# Graphique 2 : Biais en fonction du nombre d'it�rations (Monte-Carlo)
plot(1:B, biais_monte_carlo, type = "l", xlab = "Nombre d'it�rations", ylab = "Biais (Monte-Carlo)", 
     main = "Biais en fonction du nombre d'it�rations (Monte-Carlo)")
abline(h = 0, col = "red") # Ligne pour montrer la convergence vers z�ro


# Graphique 3 : Estimation de la variance en fonction du nombre d'it�rations (Bootstrap)
plot(1:B, s2_bootstrap, type = "l", xlab = "Nombre d'it�rations", ylab = "Estimation de la variance (Bootstrap)", 
     main = "Estimation de la variance (Bootstrap)")
lines(1:B, rep(1, B), col = "red") # Vraie valeur de la variance

# Graphique 4 : Biais en fonction du nombre d'it�rations (Bootstrap)
plot(1:B, biais_bootstrap, type = "l", xlab = "Nombre d'it�rations", ylab = "Biais (Bootstrap)", 
     main = "Biais en fonction du nombre d'it�rations (Bootstrap)")
abline(h = 0, col = "red") # Ligne pour montrer la convergence vers z�ro

par(mfrow = c(1, 1)) # R�initialiser la disposition par d�faut
