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

klucz(pokoj1, klucz_do_p3).
otwiera(p3, klucz_do_p3).
```

```
wyjdz(A) :-
    findall(B, drzwi(A, B), Drzwi),
    length(Drzwi, Ilosc),
    Ilosc =:= 1,
    write('[wychodze_z '), write(A), write(']'), nl.

przejdz(A, B) :-
    drzwi(A, B),
    write('[przechodze_z '), write(A), write(' do '), write(B), write(']'), nl,
    zbierz_klucz(B),
    wyjdz(B).

zbierz_klucz(A) :-
    klucz(A, B),
    write('[znalazlem_klucz '), write(B), write(']'), nl.
```
