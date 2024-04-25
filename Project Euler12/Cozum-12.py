from itertools import count


def euler12():
    for i in count(2):
        c=list(carpanlara_ayir(i))
        c.extend(carpanlara_ayir(i+))
        bolen_sayisi=reduce(lambda x,y :(y[1]+1)*x if y[0] !=2 else y[1]*x),c,1)

        if bolen_sayisi >500:
            return i*(i+1)/2
