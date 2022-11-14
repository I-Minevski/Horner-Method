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
for step in range(power):
    equation = ""
    j = 0
    for i in range(len(equation_coefficients)-1, -1, -1):
        equation += f"({equation_coefficients[j]}x^{i}) + "
        j += 1
    equation = equation.rstrip(" + ")
    print(equation)
    known_solution = int(input("Enter a known solution. "))
    solutions.append(known_solution)
    equation_coefficients = horner_method(equation_coefficients, known_solution)
    equation_coefficients.pop(-1)
    print(equation_coefficients)
    
simplified = ""
for solution in solutions:
    if solution > 0:
        simplified += f"(x - {solution}) * "
    elif solution < 0:
        simplified += f"(x + {-solution}) * "
    else:
        simplified += "x * "
print("The simplified equation is:")
print(simplified.rstrip(" * "))