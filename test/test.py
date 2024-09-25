import pytest
from unittest.mock import patch, MagicMock
from main import *

@pytest.fixture
def main_instance():
    with patch('menu.menu.Menu') as MockMenu:
        mock_menu = MockMenu.return_value
        main = Main()
        main.menu = mock_menu
        return main

def test_iniciar_continuar(main_instance):
    with patch('builtins.input', side_effect=['1', 'S', '2', 'N']), \
         patch.object(main_instance.menu, 'exibir_menu'), \
         patch.object(main_instance.menu, 'executar_operacao', side_effect=[True, False]):
        main_instance.iniciar()
        assert main_instance.menu.exibir_menu.call_count == 2
        assert main_instance.menu.executar_operacao.call_count == 2

def test_iniciar_invalid_option(main_instance):
    with patch('builtins.input', side_effect=['invalid', '1', 'N']), \
         patch.object(main_instance.menu, 'exibir_menu'), \
         patch.object(main_instance.menu, 'executar_operacao', return_value=False):
        main_instance.iniciar()
        assert main_instance.menu.exibir_menu.call_count == 2
        assert main_instance.menu.executar_operacao.call_count == 1

def test_perguntar_continuar_yes(main_instance):
    with patch('builtins.input', side_effect=['S']):
        assert main_instance.perguntar_continuar() == True

def test_perguntar_continuar_no(main_instance):
    with patch('builtins.input', side_effect=['N']):
        assert main_instance.perguntar_continuar() == False

def test_perguntar_continuar_invalid_then_yes(main_instance):
    with patch('builtins.input', side_effect=['invalid', 'S']):
        assert main_instance.perguntar_continuar() == True

def test_perguntar_continuar_invalid_then_no(main_instance):
    with patch('builtins.input', side_effect=['invalid', 'N']):
        assert main_instance.perguntar_continuar() == False