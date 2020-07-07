"""
mydir.py: moduł wymieniający przestrzenie nazw innych modułów
"""
seplen = 60
sepchr = '-'
def listing(module, verbose=True):
    sepline = sepchr * seplen
    if verbose:
        print(sepline)
        print('nazwa:', module.__name__, 'plik:', module.__file__)
        print(sepline)
    count = 0
    for attr in module.__dict__:                # Przeszukanie kluczy przestrzeni nazw
        print('%02d) %s' % (count, attr), end = ' ')
        if attr.startswith('__'):
            print('<zmienna wbudowana>')          # Pominięcie __file__ itd.
        else:
            print(getattr(module, attr))          # To samo co .__dict__[attr]
        count += 1
    if verbose:
        print(sepline)
        print(module.__name__, 'ma %d zmiennych' % count)
        print(sepline)
if __name__ == '__main__':
    import mydir
    listing(mydir)                               # Test samosprawdzający — lista samego siebie