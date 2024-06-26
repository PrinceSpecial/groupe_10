#Importer le fichier csv
data <- read.csv("Housing.csv")

#Prendre connaissance avec le dataset
head(data)
dim(data)

#Graphique de dispersion
library(ggplot2)

ggplot(data, aes(x=area, y=price)) + geom_point() + labs(title="area vs price", x="area", y="price")
#Le graphique de dispersion nous montre une relation positive entre area et price.
#Ce qui signifie qu'en général, les maisons plus grandes sont plus chères que les maisons plus petites.
#Cependant, cette relation n'est pas parfaite car il y a quelques points qui se situent loin de la ligne de tendance.
