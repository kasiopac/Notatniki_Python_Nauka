import types
from imp import reload

def status(modul):
    print('przeladowanie ' + modul.__name__)

def zagniezdzony_reload(modul, visited):
    if not modul in visited:             # przechwycenie cykli i powtarzajacych sie modulow
        status(modul)                    # wyprintowanie 'przeladowanie modulu'
        reload(modul)                    # przejscie do jego modulow podrzednych (?)
        visited[modul] = None          
        for attrobj in modul.__dict__.values():  # dla wszystkich atrybutow
            if type(attrobj) == types.ModuleType:  # rekurencja - jesli to nadal modul
                zagniezdzony_reload(attrobj, visited)
                
def reload_all(*args):
    visited = {}
    for arg in args:
        if type(arg) == types.ModuleType:
            zagniezdzony_reload(arg,visited)

if __name__ == '__main__':
    import reloadall
    reload_all(reloadall)