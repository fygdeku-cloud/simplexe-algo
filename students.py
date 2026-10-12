eleves={"Paul":{
            'note':12,
            'appreciation':'assez bien'},
        "Camille":{
           'note':10,
           'appreciation':'passables'},
        "Theo":{
            'note':17,
            'appreciation':'tres bien'},
        }

# for prenom,values in eleves.items():
#     print(prenom, values)
    
# print("La moyenne est",round(sum(eleves.values()) / len(eleves)))

eleves['Lea']={
    'note':14,
    'appreciation':'bien'
}
for prenom in eleves:
    print(eleves[prenom]['appreciation'],eleves[prenom]['note'])