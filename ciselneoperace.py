print("Welcome to calculator\n")
for target_list in range(1000):
    n1 = float(input("Write a number: \n"))
    op = input("\nChoose operator: \n")
    n2 = float(input("\nWrite a number: \n"))

if op == "+":
    print("\n Result is\n", n1 + n2)

elif op == "-":
    print("\n Result is\n", n1 - n2)

elif op == "*":
    print("\n Result is\n", n1 * n2)

elif op == "/":
    print("\n Result is\n", n1 / n2)

elif op == "**":
    print("\n After the sum and exponentiation of this numbers comes out \n", (n1 + n2) ** 2)
    print("\n So let's try the compare of numbers \n")
cn1 = float(input("\n Choose a number: \n"))
op = input("\n Choose a comparison: \n")
cn2 = float(input("\n Choose a number: \n"))

if cn1 > cn2:
    print("\n", cn1, "is bigger than", cn2)

elif cn1 < cn2:
    print(cn1, "is smaller than", cn2)

elif cn1 == cn2:
    print(cn1, "is the same as", cn2)

else:
    print("\n", cn1, op, cn2, "is wrong result\n")
