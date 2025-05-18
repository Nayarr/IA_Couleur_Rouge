def activation(neurone,entree):
    q = 0
    for i in range(len(neurone)):
        q += neurone[i] * entree[i]
        
    if(q < 1):
        return 0
    else:
        return 1
    

def apprentissage(neurone,entree,objectif):
    new_neurone = neurone.copy()
    sortie = activation(neurone, entree)
    if objectif == sortie:
        return new_neurone
    elif sortie == 0 and objectif == 1:
        for i in range(len(new_neurone)):
            new_neurone[i] += 0.2 * entree[i]
    elif sortie == 1 and objectif == 0:
        for i in range(len(new_neurone)):
            new_neurone[i] -= 0.2 * entree[i]
    return new_neurone
            
def epoque_apprentissage(neurone_init,liste_entrees_objectifs):
    new_neurone = neurone_init
    for element in liste_entrees_objectifs:
        new_neurone = apprentissage(new_neurone, element[0], element[1])
        print(new_neurone)
    return new_neurone



def ecart(neurone, neurone_base):
    q = 0
    for i in range(len(neurone)):
        q += (neurone[i] - neurone_base[i])**2
    return q