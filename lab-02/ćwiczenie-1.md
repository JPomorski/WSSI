# Ćwiczenie 1

## Zad. 1
### Zad. 1.1)
A) <br>
rodzic(X, A). <br>
rodzic(Y, A). <br>
rodzic(X, B). <br>
rodzic(Y, B). <br>

B) <br>
rodzic(X, A). <br>
rodzic(A, B). <br>
rodzic(C, B). <br>
rodzic(Y, C). <br>

C) <br>
rodzic(A, X). <br>
rodzic(C, A). <br>
rodzic(C, B). <br>
rodzic(B, Y). <br>

D) <br>
rodzic(X, A). <br>
rodzic(B, A).
rodzic(B, Y).

E) <br>
rodzic(X, A). <br>
rodzic(X, B). <br>
rodzic(Y, B). <br>
rodzic(Y, C). <br>

F) <br>
rodzic(A, X). <br>
rodzic(A, B). <br>
rodzic(B, C). <br>
rodzic(Y, C). <br>

G) <br>
rodzic(X, A). <br>
rodzic(X, B). <br>
rodzic(C, A). <br>
rodzic(Y, C). <br>
rodzic(Y, B). <br>

### Zad 1.2)
dziadek(X, Y) :- <br>
    rodzic(X, Z), <br>
    rodzic(Z, Y). <br>

rodzenstwo(X, Y) :- <br>
    rodzic(X, Z), <br>
    rodzic(Y, Z). <br>

kuzyni(X, Y) :- <br>
    rodzic(X, A), <br>
    rodzic(A, B), <br>
    rodzic(C, B), <br>
    rodzic(Y, C). <br>