feet = eval(input('enter the height'))
inches = eval(input('enter the inches'))
weight = eval(input('enter the weight'))
weight = weight * 2.208
feeti = feet * 12
height = feeti + inches
bmi = (weight / height ** 2) * 703
print(bmi)

