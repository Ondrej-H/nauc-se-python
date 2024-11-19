
import knp

def test_vyhry():
    """Otestuje funkci urci_vyteze(tah_hrace, tah_pocitace)."""
    volby = ["kámen", "nůžky", "papír"]
    for a in volby:
        for b in volby:
            if a == b:
                assert knp.urci_vyteze(a,b) == "Remíza!"
    assert knp.urci_vyteze("kámen", "nůžky") == "Vyhrál hráč!"
    assert knp.urci_vyteze("nůžky", "papír") == "Vyhrál hráč!"
    assert knp.urci_vyteze("papír", "kámen") == "Vyhrál hráč!"
    assert knp.urci_vyteze("kámen", "papír") == "Vyhrál počítač!"
    assert knp.urci_vyteze("nůžky", "kámen") == "Vyhrál počítač!"
    assert knp.urci_vyteze("papír", "nůžky") == "Vyhrál počítač!"


