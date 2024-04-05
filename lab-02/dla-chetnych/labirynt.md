## Dane:
```
pokoj(start).
pokoj(korytarz).
pokoj(pokoj1).
pokoj(pokoj2).

drzwi(start, korytarz).
drzwi(korytarz, start).
drzwi(korytarz, pokoj1).
drzwi(pokoj1, korytarz).
drzwi(korytarz, pokoj2).
drzwi(pokoj2, korytarz).
```

```
wyjdz(A) :-
    findall(B, drzwi(A, B), Drzwi),
    length(Drzwi, Ilosc),
    Ilosc =:= 1,
    write('[wychodze_z '), write(A), write(']').

przejdz(A, B) :-
    drzwi(A, B),
    write('[przechodze_z '), write(A), write(' do '), write(B), write(']'),
    wyjdz(B).
```
