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

rodzeństwo

**B)**
```
rodzic(x, a).
rodzic(a, b).
rodzic(c, b).
rodzic(y, c).
```

kuzyni

**C)**
```
rodzic(a, x).
rodzic(b, a).
rodzic(b, c).
rodzic(c, y).
```

teściowie

**D)**
```
rodzic(x, a).
rodzic(b, a).
rodzic(b, y).
```

dziacko - rodzic przyrodni

**E)**
```
rodzic(x, a).
rodzic(x, b).
rodzic(y, b).
rodzic(y, c).
```

rodzeństwo przyrodnie

**F)** 
```
rodzic(a, x).
rodzic(a, b).
rodzic(b, c).
rodzic(y, c).
```

szwagrowie 

**G)** 
```
rodzic(x, a).
rodzic(x, b).
rodzic(c, a).
rodzic(y, c).
rodzic(y, b).
```

??? kazirodztwo ??? 💀  
X jest wujkiem Y

### Zad 1.2)
```
dziadek(X, Y) :-
    rodzic(X, Z),
    rodzic(Z, Y).

rodzenstwo(X, Y) :-
    rodzic(X, A),
    rodzic(Y, A),
    rodzic(X, B),
    rodzic(Y, B).

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
    \+rodzic(Y, A),
    rodzic(X, B),
    rodzic(Y, B),
    rodzic(Y, C),
    \+rodzic(X, C).
```