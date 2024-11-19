
# side efekt může být vypsání něčeho na obrazovku nebo do souboru,
# vykreslení okýnka na obrazovku, otázka na uživatele pomocí input, atp.

print("První import: ")     # side efekt je zde výpis na obrazovku v importovaném modulu
import louka_side_efekt     # při prvním importu se provede funkce print() obsažená v modulu louka_side_efekt

print("Druhý import: ")     # importujeme-li modul podruhé (?k čemu by to ale bylo?), side efekt už se neprovede
import louka_side_efekt     # side efektu se obecně snažíme vyhnout

# side efektu se obecně snažíme vyhnout!