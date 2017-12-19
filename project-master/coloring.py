for i in db_foods['food_group'].unique():
    list_food = set(db_foods[db_foods['food_group']==i]['name'].tolist())
    db_recipes[i] = db_recipes['ingredients'].apply(lambda x: len(list_food.intersection(x)))
	
###

db_recipes[db_foods['food_group'].unique()].describe()

###

for i in ['cocoa and cocoa products']:
    nodes = set(db_foods[db_foods["food_group"] == i]['name'].tolist())
    edges = dict()
    def add_edges(x):
        for i in x:
            if(i in nodes):
                if(i in edges):
                    edges[i].update(nodes.intersection(x))
                else:
                    edges[i] = nodes.intersection(x)

    db_recipes['ingredients'].apply(add_edges)
    
for i in edges:
    edges[i].remove(i)

###

for i in edges:
    for j in edges[i]:
        if(i not in edges[j]):
            print(i,j)
			
###

s = edges['cocoa butter'].union({'cocoa butter'})
print(s)
for i in s:
    print(edges[i].union({i}).intersection(s))