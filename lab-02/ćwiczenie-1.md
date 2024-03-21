# **Ćwiczenie 1**

## **Zad. 1**

### Zad. 1.1)

**A)**  
```
rodzic(X, A).
rodzic(Y, A).
rodzic(X, B).
rodzic(Y, B).
```

rodzeństwo

**B)**
```
rodzic(X, A).
rodzic(A, B).
rodzic(C, B).
rodzic(Y, C).
```

kuzyni

**C)**
```
rodzic(A, X).
rodzic(C, A).
rodzic(C, B).
rodzic(B, Y).
```

teściowie

**D)**
```
rodzic(X, A).
rodzic(B, A).
rodzic(B, Y).
```

dziacko - rodzic przyrodni

**E)**
```
rodzic(X, A).
rodzic(X, B).
rodzic(Y, B).
rodzic(Y, C).
```

rodzeństwo przyrodnie

**F)** 
```
rodzic(A, X).
rodzic(A, B).
rodzic(B, C).
rodzic(Y, C).
```

szwagrowie 

**G)** 
```
rodzic(X, A).
rodzic(X, B).
rodzic(C, A).
rodzic(Y, C).
rodzic(Y, B).
```

??? kazirodztwo ??? 💀

### Zad 1.2)
```
dziadek(X, Y) :-
    rodzic(X, Z),
    rodzic(Z, Y).

rodzenstwo(X, Y) :-
    rodzic(X, Z),
    rodzic(Y, Z).

kuzyni(X, Y) :-
    rodzic(X, A),
    rodzic(A, B),
    rodzic(C, B),
    rodzic(Y, C).
```