## Ćw. 2

```
osoba(jan).		/*rodzice*/
osoba(kasia).
osoba(bartek).	/*dzieci*/
osoba(julia).

osoba(krystian).
osoba(krzysztof).
osoba(romuald).

osoba(aneta).
osoba(jurek).

rodzic(jan, bartek).
rodzic(jan, julia).
rodzic(kasia, bartek).
rodzic(kasia, julia).
rodzic(kasia, krystian).

rodzic(krzysztof, jan).
rodzic(romuald, kasia).
rodzic(romuald, aneta).
rodzic(aneta, jurek).

mezczyzna(jan).
mezczyzna(bartek).
mezczyzna(krystian).
mezczyzna(krzysztof).
mezczyzna(romuald).
mezczyzna(jurek).


kobieta(X) :-
    \+mezczyzna(X).

ojciec(X, Y) :-
    mezczyzna(X),
    rodzic(X, Y).

matka(X, Y) :-
    kobieta(X),
    rodzic(X, Y).

corka(X, Y) :-
    kobieta(X),
    rodzic(Y, X).

brat_rodzony(X, Y) :-
    mezczyzna(X),
    rodzic(A, X),
    rodzic(A, Y),
    rodzic(B, X),
    rodzic(B, Y),
	X \= Y,
    A \= B.

brat_przyrodni(X, Y) :-
    mezczyzna(X),
    rodzic(A, X),
    rodzic(A, Y),
    rodzic(B, X),
    \+rodzic(B, Y).

kuzyn(X, Y) :-
    rodzic(A, X),
    rodzic(B, A),
    rodzic(B, C),
    rodzic(C, Y).
    
dziadek_od_strony_ojca(X, Y) :-
    ojciec(A, Y),
    rodzic(X, A).

dziadek_od_strony_matki(X, Y) :-
    matka(A, Y),
    rodzic(X, A).
```
