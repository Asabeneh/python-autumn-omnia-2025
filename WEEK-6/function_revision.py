def calcaulate_bmi(mass, height):
    """
    This function takes two parameters:mass and height.
    It returns the BMI
    """
    bmi = mass / height ** 2
    print('I calculate your BMI', round(bmi, 2))
    
calcaulate_bmi(75, 1.73)
print(calcaulate_bmi.__doc__)