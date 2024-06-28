# Importation de la bibliotheque pour afficher l'histogramme

library(ggplot2)

# Importation de la base de Donnée

data <- read.csv("Housing.csv") 
head(data)

#Afficher le nom de tout les colonnes

#Analyse des données
summary(data)

#Verification des valeurs manquante dans la colonne bedrooms

sum(is.na(data$bedrooms))

#Histogramme baser sur la colonne bedrooms

hist(data$bedrooms, breaks = 10 , col = "blue",main = "Histogramme des chambres", xlab = "nbre de chambre", ylab = "Frequence" )

#En analysant ce histograme, on constate que les maisons ont un nombre de chambre qui sont comprise entre 1 et 6
#et la majorité des maisons ont entre 2 et 3 chambres ce qui es indiquer par les pics de l'histogramme.
#Néanmoins, il y a certains chambre qui on un nombre de chambre qui es egal à 6.