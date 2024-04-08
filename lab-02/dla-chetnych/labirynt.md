## Dane:
```
pokoj(start).
pokoj(korytarz).
pokoj(pokoj1).
pokoj(pokoj2).

drzwi(start, korytarz).
drzwi(korytarz, start).
drzwi(korytarz, pokoj1).
drzwi(korytarz, pokoj2).
drzwi(pokoj1, korytarz).
drzwi(pokoj2, korytarz).

klucz(pokoj1, klucz_do_p3).
otwiera(p3, klucz_do_p3).

:- dynamic zebrany/2.
zebrany(klucz_do_p3, false).

:- dynamic odwiedzony/1.

zamkniete(p3).
```

```
wyjdz(A) :-
    findall(B, drzwi(A, B), Drzwi),
    length(Drzwi, Ilosc),
    Ilosc =:= 1,
    write('[wychodze_z '), write(A), write(']'), nl.

przejdz(A, B) :-
    \+odwiedzony(B),
    drzwi(A, B),
    (\+zamkniete(B); (zamkniete(B), otworz(B))),
    assertz(odwiedzony(A)),
    write('[przechodze_z '), write(A), write(' do '), write(B), write(']'), nl.

zbierz_klucz(A) :-
    klucz(A, B),
    retract(zebrany(klucz_do_p3, _)),
    assertz(zebrany(klucz_do_p3, true)),
    write('[znalazlem_klucz '), write(B), write(']'), nl.

otworz(A) :-
    zebrany(B, true),
    otwiera(A, B).

szukaj_wyjscia(POKOJ_POCZATKOWY, POKOJ_Z_KLUCZEM, KLUCZ, POKOJ_Z_WYJSCIEM) :-
    przejdz(POKOJ_POCZATKOWY, B),
    /*wyjdz(B), */
    
    szukaj_wyjscia(B, POKOJ_Z_KLUCZEM, KLUCZ, POKOJ_Z_WYJSCIEM).

```
