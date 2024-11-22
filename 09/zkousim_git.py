
def vypis_ucel_tohoto_souboru():
    """
    Tato funkce vrací jen výpis.
    Existuje pouze proto, abych viděl změny v Gitu.
    """
    return "Tento soubor slouží k procvičování Gitu."


def popis_krok_1():
    """
    Popíše, jak proběhl můj první krok.
    """
    return """
V prvním kroku jsem vytvořil modul zkousim_git.py
a jeho spouštěcí program zkousim_git_spoustec.py.
Modul zkousim_git.py obsahoval pouze jedinou funkci
vypis_ucel_tohoto_souboru().
Nyní přidávám funkci druhou, která tímto popisuje,
co jsem udělal v prvním kroku.
Pokračování: commitnu tyto změny a vyzkouším git diff.
"""


def popis_krok_2():
    """
    Popíše jak proběhl můj druhý krok.
    """
    return """
Zjistil jsem, že git diff ukáže rozdíl jen když jsem provedl změny,
ale ještě jsem je necommitnul. Takže teď sem jen připíšu toto,
nebudu commitovat a zadám git diff, ať to konečně ozkouším.
"""


def popis_krok_3():
    """
    Popíše můj třetí krok.
    """
    return """
git diff už jsem vyzkoušel a jdu "větvit". Pomocí git branch uceni_vetveni
jsem vytvořil novou větev uceni_vetveni a pomocí git checkout uceni_vetveni
jsem na ni přepnul. Teď comitnu tuto změnu (vytvoření této funkce) a také
funkci přidám do spouštěče a comitnu.
"""