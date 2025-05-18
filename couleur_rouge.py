import IA

p_init = [1,0.9,0.9] # état initial du neurone
seuil = 0.0001 # écart minimum entre deux états


# remarque : les valeurs des composantes [r,g,b] des couleurs sont ici
# normalisées entre 0 et 1. Généralement, ces valeurs se situent 
# dans l'intervalle [0,255] lorsque les couleurs sont codées sur 8 bits.

# le jeu d'apprentissage ( [r,g,b], objectif )
liste_entrees_objectifs = [ ([1,0,0],1), ([0,1,1],0), ([1,1,0],0),           \
                           ([1,0,0.2],1), ([0,1,0],0), ([0,0,0],0),          \
                           ([1,0,1],0), ([0.7,0,0],1), ([0.5,0.5,0.5],0),    \
                           ([0.9,0.2,0],1), ([0.9,0,0],1), ([1,1,1],0),      \
                           ([0.2,1,0],0), ([0.8,0.2,0],1), ([0.7,0.1,0.1],1) \
                          ]

# Récupération des données d'entrainement dans le fichier CSV
# Ces données ont été générées par x_interface_rgb.py
#df = pd.read_csv('data.csv')
#liste_entrees_objectifs = [ ( [ df['rouge'][i], df['vert'][i], df['bleu'][i] ], df['label'][i] ) for i in range(len(df))]

# le jeu de test ( [r,g,b] )
jeu_test_couleurs = [ (0.9,0,0), (1,0.2,0.2), (0,0,1), \
                     (1,0,1), (1,0.5,0), (0.7,0.5,0.4) \
                    ]

#######################################################################
# phase d'apprentissage
#######################################################################
def apprentissage():  
    p = list(p_init)
    cpt = 0
    
    while True:           
        new_p = IA.epoque_apprentissage(p, liste_entrees_objectifs)
        e = IA.ecart(p,new_p)
        
        if e < seuil:
            break
        
        p = list(new_p)
        cpt = cpt + 1
    
    print("Convergence obtenue après", cpt, "iterations :", p, sep=" ")
    print("")
    return p

#######################################################################
# phase de prédiction
#######################################################################
def prediction(p):
    print("Jeu de test :")
    
    for couleur in jeu_test_couleurs:
        
        if IA.activation(p,couleur)==True:
            print("la couleur",couleur,"est rouge")
        else:
            print("la couleur",couleur,"n'est pas rouge")

#######################################################################
# programme principal  
#######################################################################  
if __name__ == '__main__':
    
    coeffs = apprentissage()
    prediction(coeffs)