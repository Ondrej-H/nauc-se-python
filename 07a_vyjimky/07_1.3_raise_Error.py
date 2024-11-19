
# obsah čtverce, kde zvedáme ValueError 
def vypocti_obsah_ctverce(strana):
    """Vrátí obsah čtverce s danou délkou strany.
    Pokud strana není kladná, vyvolá ValueError."""
    if strana > 0:
        obsah = strana ** 2
        return obsah
    else:
        raise ValueError(f"Délka strany musí být kladná! Číslo {strana} kladné není.")
        # raise ukončí funkci a není-li ošetrřeno jjinak, tak ukončí i celý program

print(vypocti_obsah_ctverce(-5))