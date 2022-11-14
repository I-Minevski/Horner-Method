def horner_method(coef, n):
    result = int(coef[0])
    new_poly_coef = [coef[0]]
    for i in range(1, len(coef)):
        result = n * result + int(coef[i])
        new_poly_coef.append(result)
    return new_poly_coef


polynomial_coefficients = []
while True:
    coefficient = input("Enter a valid coefficient. If done type [end]. ")
    if coefficient == "end":
        break
    polynomial_coefficients.append(int(coefficient))

power = len(polynomial_coefficients) - 1
solutions = []
is_expandable = True
horner_matrix = []
for step in range(power):
    polynomial = ""
    j = 0
    for i in range(len(polynomial_coefficients) - 1, -1, -1):
        if polynomial_coefficients[j] == 1:
            monomial = f"(x^{i}) + "
        else:
            monomial = f"({polynomial_coefficients[j]}x^{i}) + "
        polynomial += monomial
        j += 1
    polynomial = polynomial.rstrip(" + ")
    print(polynomial)
    known_solution = int(input("Enter a known solution. "))
    if horner_method(polynomial_coefficients, known_solution)[-1] != 0:
        print("The remaining polynomial has no real solutions.")
        is_expandable = False
        break
    solutions.append(known_solution)
    polynomial_coefficients = horner_method(polynomial_coefficients, known_solution)
    polynomial_coefficients.pop(-1)
    horner_matrix.append(polynomial_coefficients)
    for row in horner_matrix:
        print('|'.join(str(coef) for coef in row))

simplified = ""
for solution in solutions:
    if solution > 0:
        simplified += f"(x - {solution}) * "
    elif solution < 0:
        simplified += f"(x + {-solution}) * "
    else:
        simplified += "x * "
if not is_expandable:
    simplified += f"({polynomial})"
print("The simplified polynomial is:")
print(simplified.rstrip(" * "))