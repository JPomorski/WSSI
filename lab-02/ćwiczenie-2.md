## Ćw. 2

rodzic(marek).
rodzic(grazyna).
mezczyzna(marek).
mezczyzna(brajan).
osoba(marek).
osoba(grazyna).
osoba(brajan).
osoba(dzesika).

kobieta(X) :-
    \+mezczyzna(X).

ojciec(X, Y) :-
    osoba(Y),
    rodzic(X), mezczyzna(X).

matka(X, Y) :-
    osoba(Y),
    rodzic(X), kobieta(X).

corka(X, Y) :-
    kobieta(X), rodzic(Y).

brat_rodzony(X, Y) :-
    mezczyzna(X),
    (ojciec(A, X), ojciec(A, Y)),
    (matka(B, X), matka(B, Y)).

brat_przyrodni(X, Y) :-
    mezczyzna(X),
    ((ojciec(A, X), ojciec(A, Y)),
    \+(matka(B, X), matka(B, Y)));
    (matka(A, X), matka(A, Y)),
    \+(ojciec(B, X), ojciec(B, Y)).
