from io import StringIO
from unittest.mock import patch
import pytest
from taller import Meal, DiningExperienceManager


class TestDiningExperienceManager:

    @pytest.fixture
    def manager(self):
        return DiningExperienceManager()

    def test_validate_quantity_valid_input(self, manager):
        quantity = "5"
        result = manager.validate_quantity(quantity)
        assert result == 5

    def test_validate_quantity_invalid_input(self, manager):
        quantity = "-1"
        result = manager.validate_quantity(quantity)
        assert result is None

    def test_calculate_total_cost_with_discounts(self, manager):
        selections = {0: 5, 1: 6, 2: 7}
        result = manager.calculate_total_cost(selections)
        assert result == 104.16

    def test_calculate_discount(self, manager):
        selections = {0: 5, 1: 6, 2: 7}
        result = manager.calculate_discount(selections)
        assert result == 28.8

    def test_calculate_total_cost_special_offer_discount_10(self, manager):
        selections = {0: 5}
        result = manager.calculate_total_cost(selections)
        assert result == 42.0

    def test_calculate_total_cost_no_special(self, manager):
        selections = {1: 3, 2: 2}
        result = manager.calculate_total_cost(selections)
        assert result == 38

    def test_calculate_total_cost_discount_5_percent(self, manager):
        selections = {0: 6}
        result = manager.calculate_total_cost(selections)
        assert result == 45.36

    def test_calculate_total_cost_discount_10_percent(self, manager):
        selections = {0: 11}
        result = manager.calculate_total_cost(selections)
        assert result == 73.92

    def test_calculate_total_cost_discount_20_percent(self, manager):
        selections = {0: 15}
        result = manager.calculate_total_cost(selections)
        assert result == 100.8
        
    ##------ case additional to coverage 100%----------------
    def test_display_menu(self, manager):
            # Creamos un objeto StringIO para capturar la salida impresa
            output = StringIO()
            
            # Usamos el decorador patch para redirigir la salida impresa al objeto StringIO
            with patch('sys.stdout', new=output):
                manager.display_menu()

            # Obtenemos la salida capturada
            output_text = output.getvalue()

            # Comparamos la salida capturada con la salida esperada
            expected_output = "Menu:\n1. Chicken Chow Mein - $8\n2. Spaghetti Carbonara - $10\n3. Croissant - $4\n"
            assert output_text == expected_output   

    def test_start_dining_experience_order_cancel(self, manager):
        # Simulamos el caso en el que el usuario cancela el pedido
        with patch('builtins.input', side_effect=['q']):  # Agregamos 'q' para simular la cancelación
            with patch('sys.stdout', new=StringIO()) as output:
                result = manager.start_dining_experience()

        expected_output = "Welcome to the Dining Experience Manager!\nMenu:\n1. Chicken Chow Mein - $8\n2. Spaghetti Carbonara - $10\n3. Croissant - $4\nNo meals were ordered.\n"
        
        
        assert output.getvalue() == expected_output

   
    def test_start_dining_experience_invalid_meal_number(self, manager):
        # Simulamos el caso en el que el usuario ingresa un número de comida inválido (5)
        with patch('builtins.input', side_effect=['5', 'q']):
            with patch('sys.stdout', new=StringIO()) as output:
                result = manager.start_dining_experience()
        print(output.getvalue().strip())
        expected_output = """
Welcome to the Dining Experience Manager!
Menu:
1. Chicken Chow Mein - $8
2. Spaghetti Carbonara - $10
3. Croissant - $4
Invalid meal number. Please select a valid meal from the menu.

Menu:
1. Chicken Chow Mein - $8
2. Spaghetti Carbonara - $10
3. Croissant - $4
No meals were ordered.
    """
        print(expected_output.strip())
        assert output.getvalue().strip() == expected_output.strip()

    def test_start_dining_experience_order_confirm(self, manager):
        # Simulamos el caso en el que el usuario realiza un pedido y lo confirma
        with patch('builtins.input', side_effect=['1', '2', 'q', 'y']):
            with patch('sys.stdout', new=StringIO()) as output:
                result = manager.start_dining_experience()

        print(output.getvalue())  # Imprime el contenido real del output

        expected_output = """
Welcome to the Dining Experience Manager!
Menu:
1. Chicken Chow Mein - $8
2. Spaghetti Carbonara - $10
3. Croissant - $4
Menu:
1. Chicken Chow Mein - $8
2. Spaghetti Carbonara - $10
3. Croissant - $4

Order Summary:
Chicken Chow Mein - 2 x $8

Total Cost: $16.8
Total Discount: $-0.8000000000000007
Order confirmed. Enjoy your dining experience!
"""

        assert output.getvalue().strip() == expected_output.strip()
        
  
    def test_start_dining_experience_quantity_none(self, manager):
        with patch('builtins.input', side_effect=['1','2','3', '', 'q', 'n']):
            with patch('sys.stdout', new=StringIO()) as output:
                result = manager.start_dining_experience()

        print(output.getvalue())  # Imprime el contenido real del output

        expected_output = """
Welcome to the Dining Experience Manager!
Menu:
1. Chicken Chow Mein - $8
2. Spaghetti Carbonara - $10
3. Croissant - $4
Menu:
1. Chicken Chow Mein - $8
2. Spaghetti Carbonara - $10
3. Croissant - $4
invalid literal for int() with base 10: ''
Menu:
1. Chicken Chow Mein - $8
2. Spaghetti Carbonara - $10
3. Croissant - $4

Order Summary:
Chicken Chow Mein - 2 x $8

Total Cost: $16.8
Total Discount: $-0.8000000000000007
Order canceled.
        """

        assert output.getvalue().strip() == expected_output.strip()