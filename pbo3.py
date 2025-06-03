class Cashier:
    def __init__(self, items, prices):
        self.items = items
        self.prices = prices
    def calculate_total(self, selected_items): #modifikasi fungsi ini
        try:
            total = 0
            for item in selected_items:
                index = self.items.index(item)
                price = self.prices[index]
                total += price
            return total
        except: 
            print("barang tidak tersedia")

items = ["apel", "pisang", "jeruk"]
prices = [2500, 1500, 3000]

cashier = Cashier(items, prices)

selected_items = input("Masukkan item yang dibeli (pisahkan dengan koma): ").lower().split(",")

selected_items = [item.strip() for item in selected_items]

total_price = cashier.calculate_total(selected_items)
print("Total belanja:", total_price)