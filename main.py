goods = [["Apples", 50], ["Oranges", 190], ["Peaches", 100], ["Blueberries", 200], ["Bananas", 77]]
new_product = ["", 0]

product_name = input("Enter a new product name: ")
price = int(input("Enter a price for a new product: "))

new_product[0] = product_name
new_product[1] = int(price)

goods.append(new_product)

print(goods)
box = len(goods)
for i in range(box):
    goods[i][1] += goods[i][1] * 0.08

print(goods)