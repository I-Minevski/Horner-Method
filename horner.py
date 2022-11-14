def horner_method(coef, n):
    result = int(coef[0])
    new_poly_coef = [coef[0]]
    for i in range(1, len(coef)):
        result = n*result + int(coef[i])
        new_poly_coef.append(result)
    return new_poly_coef


equation_coefficients = []
while True:
    coefficient = input("Enter a valid coefficient. If done type [end]. ")
    if coefficient == "end":
        break
    equation_coefficients.append(int(coefficient))

power = len(equation_coefficients)-1
solutions = []
