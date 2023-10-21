from lib.animal import Animal
from lib.zoo import Zoo

# code here


# e.g.  

z1 = Zoo( 'Micke Grove Zoo', 'Lodi, CA' )
z2 = Zoo('Philly Zoo', 'Philadelphia, Pa')
z3 = Zoo('Family Zoo', 'New York, Ny')
a1 = Animal( 'Lion', 75, 'Luke', z1 )
a2 = Animal( 'Tiger', 28, 'Tigger', z1)
a3 = Animal( 'Orangutan', 35, 'Frank', z2)
a4 = Animal( 'Elephant', 500, 'Dumbo', z3)
a5 = Animal( 'Giraffe', 110, 'Mr. Ed', z3 )
a6 = Animal( 'Camel', 83, 'Lumpy', z3 )
a7 = Animal( 'Tiger', 250, 'Fats Domino', z1)






# ipdb allows us to stop our code & test stuff
import ipdb; ipdb.set_trace()
print( 'Thanks for visiting the zoo!' )