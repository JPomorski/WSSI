# **Ćwiczenie 1**

## **Zad. 1**

### Zad. 1.1)

**A)**  
```
rodzic(x, a).
rodzic(y, a).
rodzic(x, b).
rodzic(y, b).
```

rodzeństwo: X jest bratem Y, mają wspólnych rodziców

**B)**
```
rodzic(x, a).
rodzic(a, b).
rodzic(c, b).
rodzic(y, c).
```

kuzyni: rodzic X i rodzic Y mają wspólnego rodzica

**C)**
```
rodzic(a, x).
rodzic(b, a).
rodzic(b, c).
rodzic(c, y).
```

teściowie: dziecko X i dziecko Y mają wspólne dziecko

**D)**
```
rodzic(x, a).
rodzic(b, a).
rodzic(b, y).
```

dziecko - rodzic przyrodni: X jest dzieckiem przyrodnim Y, ma tylko jednego wspólnego rodzica z dzieckiem Y

**E)**
```
rodzic(x, a).
rodzic(x, b).
rodzic(y, b).
rodzic(y, c).
```

rodzeństwo przyrodnie: X i Y mają tylko jednego wspólnego rodzica

**F)** 
```
rodzic(a, x).
rodzic(a, b).
rodzic(b, c).
rodzic(y, c).
```

szwagrowie: rodzic dziecka X jest dzieckiem rodzica Y

**G)** 
```
rodzic(x, a).
rodzic(x, c).
rodzic(b, a).
rodzic(y, b).
rodzic(y, c).
```

??? kazirodztwo ??? 💀  
wujek - bratanek: dziecko rodzica X jest rodzicem Y

### Zad 1.2)
```
dziadek(X, Y) :-
    rodzic(X, Z),
    rodzic(Z, Y).

rodzenstwo(X, Y) :-
    rodzic(X, A),
    rodzic(Y, A),
    rodzic(X, B),
    rodzic(Y, B),
    X \= Y,
    A \= B.

kuzyni(X, Y) :-
    rodzic(X, A),
    rodzic(A, B),
    rodzic(C, B),
    rodzic(Y, C).

tesciowie(X, Y) :-
    rodzic(A, X),
    rodzic(B, A),
    rodzic(B, C),
    rodzic(C, Y).

rodzic_przyrodni(X, Y) :-
    rodzic(X, A),
    rodzic(B, A),
    rodzic(B, Y),
    \+rodzic(X, Y).

rodzenstwo_przyrodnie(X, Y) :-
    rodzic(X, A),
    rodzic(Y, A),
    rodzic(Y, B),
    \+rodzic(X, B).

szwagrowie(X, Y) :-
    rodzic(A, X),
	rodzic(A, B),
	rodzic(B, C),
	rodzic(Y, C).

bratanek(X, Y) :-
    rodzic(X, A),
    rodzic(B, A),
    rodzic(Y, B).
```
