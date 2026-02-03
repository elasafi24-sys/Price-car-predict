import numpy as np

def predict_car_price(features):
    age = features[0]
    
    if age < 7:
        weights = np.array([-1200, -0.05, 2000, 65])
        bias = 14000
    else:
        weights = np.array([-400, -0.001, 1200, 45])
        bias = 6000
    
    return np.dot(features, weights) + bias

print("--- مرحباً بك في نظام وليد الذكي لتسعير السيارات ---")

try:
    # استقبال المدخلات من المستخدم
    age = float(input("أدخل عمر السيارة (بالسنوات): "))
    mileage = float(input("أدخل المسافة المقطوعة (بالكيلومتر): "))
    engine = float(input("أدخل سعة المحرك (باللتر - مثلاً 1.8): "))
    hp = float(input("أدخل عدد الأحصنة (HP): "))

    # وضعها في مصفوفة NumPy
    user_car = np.array([age, mileage, engine, hp])

    # حساب السعر
    final_price = predict_car_price(user_car)

    # عرض النتيجة
    if final_price < 500: # حد أدنى للسعر (سعر الخردة)
        final_price = 500
        
    print("\n" + "="*30)
    print(f"السعر المتوقع لسيارتك هو: ${final_price:,.2f}")
    print("="*30)

except ValueError:
    print("خطأ: يرجى إدخال أرقام صحيحة فقط!")
