peso=[77, 80, 117, 78, 102, 95, 65, 79, 74, 70, 114, 69, 87, 43, 65, 98, 71, 92, 95, 94, 67, 75, 102, 119, 99, 87, 74, 110, 64]
altura=[1.63, 1.53, 2.26, 1.97, 2.52, 1.60, 1.72, 2.04, 1.52, 1.83, 2.96, 2.08, 2.09, 1.50, 1.50, 1.78, 2.11, 2.14, 2.60, 2.02, 1.83, 1.64, 1.71, 2.73, 2.22, 1.76, 1.43, 3.16, 1.35]
for p, a in zip(peso, altura):
        bmi = p/(a)**2
        if bmi < 18.5:
            print("under")
        elif bmi >= 18.5 and bmi < 25:
            print("normal")
        elif bmi >= 25 and bmi < 30:
            print("over")
        elif bmi >= 30:
            print("obese")
