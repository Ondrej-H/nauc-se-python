import knp
import pytest

def test_spatneho_tahu():
    """🤘 vs. 🖖 není správný vstup"""
    with pytest.raises(ValueError):
        knp.urci_vyteze('metal', 'spock')

