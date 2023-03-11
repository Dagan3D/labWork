from Lab_4.Product import Product
from Lab_4.Phone import Phone

product1 = Product("Тряпочка", 1000, "Самая надёжная тряпочка для протирки вашего телефона", 1)
print(product1.name)
print(product1.apply_discount(20))  # выводит 800.0
print(product1.get_quantity_in_box(20, 10, 5), "\n")  # выводит 1000

print(product1, "\n")

phone1 = Phone("SE", 20, "Sony Ericsson", "Xperia X8", 3.0)
phone1.description = "Бессмертная классика"
phone1.volume = 10
print(phone1)

set1 = product1 + phone1
print(set1)
