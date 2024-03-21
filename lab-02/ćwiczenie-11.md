# Ćwiczenie 11
```
lubi(jan, pawel).
lubi(pawel, krzysztof).
lubi(pawel, jan).
lubi(jan, bartek).
lubi(bartek, jan).

mezczyzna(jan).
mezczyzna(pawel).
kobieta(kasia).
kobieta(zosia).

kocha(jan, kasia).
kocha(kasia, jan).
kocha(pawel, zosia).
kocha(krzysztof, linux).

przyjazn(X, Y) :-
    lubi(X, Y),
    lubi(Y, X).

niby_przyjazn(X, Y) :-
    lubi(X, Y);
    lubi(Y, X).
```

### 1.
```
nieprzyjazn(X, Y) :-
    \+lubi(X, Y),
    \+lubi(X, Y).
```

### 2. 
zrobione wyżej

### 3.
```
loves(X, Y) :-
    (kocha(X, Y); kocha(Y, X)),
    (mezczyzna(X), kobieta(Y); kobieta(X), mezczyzna(Y)).
```

### 4.
```
true_love(X, Y) :-
    (kocha(X, Y), kocha(Y, X)),
    (mezczyzna(X), kobieta(Y); kobieta(X), mezczyzna(Y)).
```
