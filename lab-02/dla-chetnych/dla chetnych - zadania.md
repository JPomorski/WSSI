## Zad. 1

```
czlowiek(markus).
pompejanczyk(markus).
rzymianin(X) :-
    pompejanczyk(X).

wladca(cezar).

lojalny(X, Y) :-
    rzymianin(X).

probuje_dokonac_zamachu(X, Y) :-
    wladca(Y),
    \+lojalny(X, Y).
```
