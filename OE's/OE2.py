class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def __str__(self):
        return f"Brand: {self.brand}\nModel: {self.model}\nPrice: {self.price}"

    def modify_price(self, new_price):
        self.price = new_price

def create_phone():
    brand = input("Enter brand: ")
    model = input("Enter model: ")
    price = float(input("Enter price: "))
    return Phone(brand, model, price)

def modify_phone(phones):
    index = int(input("Enter phone index to modify: "))
    new_price = float(input("Enter new price: "))
    phones[index].modify_price(new_price)

def delete_phone(phones):
    index = int(input("Enter phone index to delete: "))
    del phones[index]

def main():
    phones = []
    while True:
        print("\n1. Create Phone")
        print("2. Modify Phone")
        print("3. Delete Phone")
        print("4. Display Phones")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            phone = create_phone()
            phones.append(phone)
        elif choice == 2:
            modify_phone(phones)
        elif choice == 3:
            delete_phone(phones)
        elif choice == 4:
            for i, phone in enumerate(phones):
                print(f"Phone {i+1}:")
                print(phone)
        elif choice == 5:
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()