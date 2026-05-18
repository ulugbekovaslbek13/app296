def calculate_bmi():
    print("--- TANA VAZNI INDEKSI (BMI) ---")
    vazn = float(input("Vazningizni kiriting (kg): "))
    boy = float(input("Boyingizni kiriting (metrda, masalan 1.75): "))
    
    bmi = vazn / (boy ** 2)
    
    print(f"\nSizning BMI ko'rsatkichingiz: {bmi:.2f}")
    
    if bmi < 18.5:
        print("Holat: Vazn yetishmovchiligi")
    elif 18.5 <= bmi < 25:
        print("Holat: Me'yor (Sog'lom)")
    else:
        print("Holat: Ortiqcha vazn")

calculate_bmi()
input("\nYopish uchun Enter bosing...")