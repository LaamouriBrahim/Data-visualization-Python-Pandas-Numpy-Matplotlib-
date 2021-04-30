from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import odf
from pandas_ods_reader import read_ods
import matplotlib
import numpy as np



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

data=data.replace('-',0) #remplacer toutes les occurences du str "-" par 0
data = pd.DataFrame.transpose(data)

idcomp =["1.1","1.2","1.3","2.1","2.2","2.3","2.4","3.1","3.2","3.3","3.4","4.1","4.2","4.3","5.1","5.2"]

x = np.arange(len(idcomp))
fig, ax = plt.subplots()
ax.set_xticklabels(idcomp)
plt.xlabel("Compétence")


#fonction qui trace les boites à moustaches directement à partir de la dataframe
#elle fait tout le boulot HiHi
plt.boxplot(data)
plt.grid(True, color = "white", linewidth = 2)
plt.gca().patch.set_facecolor('0.9')

plt.title("Boite à moustaches de toutes les compétences PIX de la promotion "+annee)
plt.show()