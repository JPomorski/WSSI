# **Ćwiczenie 2**

## **Zad. 2**

Baza predykatów:

```
osoba(jan).         %rodzice
osoba(kasia).
osoba(bartek).      %dzieci
osoba(julia).

osoba(krystian).	%brat przyrodni
osoba(krzysztof).	%dziadkowie
osoba(romuald).
osoba(grazyna).

osoba(edward).		%pradziadkowie
osoba(elzbieta).

osoba(aneta).		%ciotka
osoba(jurek).		%kuzyn

rodzic(jan, bartek).
rodzic(jan, julia).
rodzic(kasia, bartek).
rodzic(kasia, julia).
rodzic(kasia, krystian).

rodzic(krzysztof, jan).
rodzic(romuald, kasia).
rodzic(romuald, aneta).
rodzic(grazyna, kasia).
rodzic(aneta, jurek).

rodzic(edward, krzysztof).
rodzic(elzbieta, krzysztof).

mezczyzna(jan).
mezczyzna(bartek).
mezczyzna(krystian).
mezczyzna(krzysztof).
mezczyzna(romuald).
mezczyzna(jurek).
mezczyzna(edward).
```

Reguły:

**1)**

```
kobieta(X) :-
    \+mezczyzna(X).
```

**2)**

```
ojciec(X, Y) :-
    mezczyzna(X),
    rodzic(X, Y).
```

**3)**

```
matka(X, Y) :-
    kobieta(X),
    rodzic(X, Y).
```

**4)**

```
corka(X, Y) :-
    kobieta(X),
    rodzic(Y, X).
```

**5)**

```
brat_rodzony(X, Y) :-
    mezczyzna(X),
    rodzic(A, X),
    rodzic(A, Y),
    rodzic(B, X),
    rodzic(B, Y),
	X \= Y,
    A \= B.
```

**6)**

```
brat_przyrodni(X, Y) :-
    mezczyzna(X),
    rodzic(A, X),
    rodzic(A, Y),
    rodzic(B, X),
    \+rodzic(B, Y).
```

**7)**

```
kuzyn(X, Y) :-
    rodzic(A, X),
    rodzic(B, A),
    rodzic(B, C),
    rodzic(C, Y).
```

**8)**

```
dziadek_od_strony_ojca(X, Y) :-
    ojciec(X, A),
    ojciec(A, Y).
```

**9)**

```
dziadek_od_strony_matki(X, Y) :-
    ojciec(X, A),
    matka(A, Y).
```

**10)**

```
dziadek(X, Y) :-
    ojciec(X, A),
    rodzic(A, Y).
```

**11)**

```
babcia(X, Y) :-
    matka(X, A),
    rodzic(A, Y).
```

**12)**

```
wnuczka(X, Y) :-
    kobieta(Y),
    (babcia(X, Y); dziadek(X, Y)).
```

**13)**

```
przodek_do2pokolenia_wstecz(X, Y) :-
    rodzic(X, Y);
    (dziadek(X, Y); babcia(X, Y)).
```

**14)**

```
przodek_do3pokolenia_wstecz(X, Y) :-
    rodzic(X, Y);
    (dziadek(X, Y); babcia(X, Y));
    ((rodzic(X, A), dziadek(A, Y)); (rodzic(X, A), babcia(A, Y))).
```
