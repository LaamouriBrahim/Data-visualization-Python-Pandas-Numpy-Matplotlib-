import pandas as pd
import numpy as np
from matplotlib import colorbar, pyplot as plt
import matplotlib
from pandas_ods_reader import read_ods
import odf



#saisir des années

'''

#list des années dont les données sont dispo
annee_fichiers_dispo = ["2018_2019","2019_2020","2020_2021"]

#faciliter la visualisation d'histogramme des differents fichiers/il faut qu'ils soient dans le meme dossier
annee1= input("saisissez les deux années correspondant à l'année scolaire : \n")
annee2= input("")
annee = str(min(int(annee1),int(annee2)))+"_"+str(max(int(annee1),int(annee2)))

#vérifier si on a bien les données de l'année inséré
if(annee not in annee_fichiers_dispo):
	print("les données de l'année "+annee+" sont indisponible")
	exit()

'''



#choix d'années

print("Choisissez l'année scolaire dont vous souhaitez voir l'histogramme (insérez 1, 2 ou 3):")
print("1 - 2018/2019\n2 - 2019/2020\n3 - 2020/2021")
ans = input("")

if ans == '1':
	annee="2018_2019"
elif ans == '2' :
	annee="2019_2020"
elif ans == '3' :
	annee="2020_2021"
else :
	print("Veuillez choisir l'un des numéros proposés !")
	exit()


#pathway du fichier ods dont on souhaite visualiser l'histogramme
path = "/home/blaamouri/cmi/certification_pix_"+annee+".ods"      
#print(path, type(path)) /juste pour vérifier que path est bien saisi
#récupérer les données du fichier et les stocker dans un dataframe appellé qu'on va nommer data

data = read_ods(path, 1)
#print(data) / ptit test

data = data.replace('-',0)
#avg stands for average/moyenne
avg = data.mean()
#std stands for standard deviation/écart type
std = data.std()

idcomp =["1.1","1.2","1.3","2.1","2.2","2.3","2.4","3.1","3.2","3.3","3.4","4.1","4.2","4.3","5.1","5.2"]
#tableau contenant la moyenne de chaque compétence
avgs = [avg[0],avg[1],avg[2],avg[3],avg[4],avg[5],avg[6],avg[7],avg[8],avg[9],avg[10],avg[11],avg[12],avg[13],avg[14],avg[15]]
#tableau contenant l'écart type' de chaque compétence
stds = [std[0],std[1],std[2],std[3],std[4],std[5],std[6],std[7],std[8],std[9],std[10],std[11],std[12],std[13],std[14],std[15]]
#lol


#on crée un tableau contenant les int de 0 jusqu'à 15
x = np.arange(len(idcomp))
#largeur de chaque bar
width = 0.80

fig, ax = plt.subplots()

#tracer les barres reprensentant les moyennes
avg_bar = ax.bar( x ,avgs ,width, label='moyenne', color = "turquoise")

#tracer écart type sous forme de barre d'erreur/segements sur les barres de moyennes de centre = la moyenne....
#on supprime la ligne de code juste en bas si on souhaite visualiser que les moyennes
plt.errorbar(idcomp, avgs, color="dimgray" ,label = "écart type", fmt = '.',yerr=stds,capsize = 5)


#afficher la légende
plt.legend()

#titre de l'histogramme
ax.set_title("Moyennes et écarts types des differents compétences de la certification PIX de la promotion "+annee)
ax.set_xticks(x)
ax.set_xticklabels(idcomp)
#fig.tight_layout()

#label de chaque axe
plt.xlabel("Compétence")
plt.ylabel("Niveau")

#afficher l'histogramme
plt.show()






