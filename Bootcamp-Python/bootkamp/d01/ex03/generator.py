from numpy.random import shuffle as shfl

def generator(txt, sep=' ', option='default'):
    if type(txt) is not str or option not in ('ordered', 'unique', 'shuffle', 'default'):
        return 'ERRROR'
    liste = txt.split(sep)
    dico = {
        'ordered':lambda liste: liste.sort(),
        'unique':lambda liste: set(liste),
        'shuffle':lambda liste: shfl(liste),
        'default':lambda liste: True }
    liste = (liste, dico[option](liste))[option == 'unique']
    for i in liste:
        yield i

if __name__ == '__main__':
    for elem in generator('jaime les fougere', sep=' '):
        print('default: ' + elem)
    for elem in generator('jaime les fougere', option='shuffle', sep=' '):
        print('shuffle: ' + elem)
    for elem in generator('jaime les fougere Ahh', option='ordered', sep=' '):
        print('orderred: ' + elem)
    for elem in generator('jaime les fougere les jaime fougere les', option='unique', sep=' '):
        print('unique: ' + elem)
    for elem in generator(6, option='unique', sep=' '):
        print('error: ' + elem)
