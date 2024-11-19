

def zamen(slovo, pozice, novy_znak):
    """Zamění písmeno na indexu 'pozice' ve zvoleném slově ('slovo') za 'novy znak'."""

    prvni_cast_slova = slovo[:pozice]
    druha_cast_slova = slovo[pozice+1:]
    nove_slovo = prvni_cast_slova + novy_znak + druha_cast_slova
    return nove_slovo


print(zamen("Hřebík", 0, "K"))
