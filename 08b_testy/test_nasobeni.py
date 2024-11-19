
import nasobeni    # nelze importovat celý modul nasobeni, protože pak by kód za assert musel vypadat: 
                                # assert nasobeni.vynasob(2, 4) == 8
def test_vynasob():
    """Otestuje funkci vynasob."""
    assert nasobeni.vynasob(2, 4) == 8      # my ale chceme testovat: assert vynasob(2, 4) == 8

"""
from nasobeni import vynasob
-> def test_vynasob():
    \"""Otestuje funkci vynasob.\"""
    assert vynasob(2, 4) == 8
"""
