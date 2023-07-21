class Meal:
    def __init__(self, name, price, is_special=False):
        self.name = name
        self.price = price
        self.is_special = is_special


class DiningExperienceManager:
    def __init__(self):
        self.menu = [
            Meal("Chicken Chow Mein", 8, is_special=True),
            Meal("Spaghetti Carbonara", 10),
            Meal("Croissant", 4),
            # Add more meals to the menu as needed
        ]

    def display_menu(self):
        print("Menu:")
        for idx, meal in enumerate(self.menu):
            print(f"{idx + 1}. {meal.name} - ${meal.price}")

    def validate_quantity(self, quantity):
        try:
            quantity = int(quantity)
            if quantity > 0 and quantity <= 100:
                return quantity
            else:
                raise ValueError("Invalid quantity. Please enter a positive integer between 1 and 100.")
        except ValueError as e:
            print(e)
        return None

    def calculate_total_cost(self, selections):
        total_cost = 0
        for meal_id, quantity in selections.items():
            if 0 <= meal_id < len(self.menu) and quantity > 0:
                meal = self.menu[meal_id]
                total_cost += meal.price * quantity  # Arreglamos el cálculo aquí, eliminamos "meal.calculate_cost(quantity)"

        total_discount = self.calculate_discount(selections)
        total_cost -= total_discount

        if self.check_special_meal_in_selections(selections):
            total_cost += total_cost * 0.05

        return total_cost
    
    def calculate_discount(self, selections):
        total_quantity = sum(selections.values())
        if total_quantity > 10:  # Cambiamos el valor a 10, ya que el descuento del 20% se aplica a partir de 10 unidades
            return 0.2 * total_quantity * 8
        elif total_quantity > 5:  # Cambiamos el valor a 5, ya que el descuento del 10% se aplica a partir de 5 unidades
            return 0.1 * total_quantity * 8
        return 0

    def check_special_meal_in_selections(self, selections):
        for meal_id, quantity in selections.items():
            if 0 <= meal_id < len(self.menu) and quantity > 0:
                if self.menu[meal_id].is_special:
                    return True
        return False

    def start_dining_experience(self):
        print("Welcome to the Dining Experience Manager!")

        selections = {}

        while True:
            self.display_menu()

            meal_idx = input("Enter the number of the meal you want to order (or 'q' to quit): ")
            if meal_idx.lower() == 'q':
                break

            try:
                meal_idx = int(meal_idx) - 1
                if meal_idx < 0 or meal_idx >= len(self.menu):
                    raise ValueError("Invalid meal number. Please select a valid meal from the menu.")
            except ValueError as e:
                print(e)
                continue

            quantity = input("Enter the quantity for this meal: ")
            quantity = self.validate_quantity(quantity)
            if quantity is None:
                continue

            selections[meal_idx] = quantity

        if not selections:
            print("No meals were ordered.")
            return -1

        print("\nOrder Summary:")
        total_before_discount = 0
        for idx, meal in enumerate(self.menu):
            quantity = selections.get(idx, 0)
            if quantity > 0:
                total_before_discount += meal.price * quantity
                print(f"{meal.name} - {quantity} x ${meal.price}")

        total_cost = self.calculate_total_cost(selections)
        total_discount = total_before_discount - total_cost

        print(f"\nTotal Cost: ${total_cost}")
        print(f"Total Discount: ${total_discount}")

        confirmation = input("Confirm the order (y/n): ")
        if confirmation.lower() == 'y':
            print("Order confirmed. Enjoy your dining experience!")
            return total_cost
        else:
            print("Order canceled.")
            return -1


if __name__ == "__main__":
    manager = DiningExperienceManager()
    total_cost = manager.start_dining_experience()
    if total_cost != -1:
        print(f"Total Cost of Dining Experience: ${total_cost}")
