
# 
def neco_udelej_1(odpoved):     # pro ozkoušení zadej jako argument string, např.: "Toto není celé číslo."
    return int(odpoved)                # -> ValueError


def neco_udelej_2():
    print(neexistujici_promenna)    # -> NameError


def neco_udelej_3(odpoved):      # jako argument nic nezadávej a zakomentuj blok 'except Exception'
    return int(odpoved)                 # -> TypeError


try:
    neco_udelej_3()
except ValueError:
    print('Tohle se provede, pokud nastane ValueError')
except NameError:
    print('Tohle se provede, pokud nastane NameError')
#except Exception:
#    print('Tohle se provede, pokud nastane jiná chyba')
    # (kromě SystemExit a KeyboardInterrupt, ty chytat nechceme)
except TypeError:
    print('Tohle se provede pouze v případě, že zakomentujeme blok "except Exception" a nastane TypeError.')
    # ("except Exception" výše ošetřuje i TypeError; není-li zakomentován, sem se Python nedostane)
else:
    print('Tohle se provede, pokud chyba nenastane')
finally:
    print('Tohle se provede vždycky; i pokud v `try` bloku byl např. `return`')