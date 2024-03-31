## Zad. 1

### a)
```
czlowiek(markus).
czlowiek(aureliusz).

czlowiek(X) :-
    lojalny(X, _).

pompejanczyk(markus).

rzymianin(X) :-
    pompejanczyk(X).
rzymianin(X) :-
    lojalny(X, Y), wladca(Y).

wladca(cezar).

lojalny(markus, aureliusz).
lojalny(aureliusz, cezar).
        
probuje_dokonac_zamachu(X, Y) :-
    wladca(Y),
    \+lojalny(X, Y).
```

### b)

Według mnie tak, ponieważ wiemy, że Markus próbował dokonać zamachu na Cezara, a dokonać zamachu mogą tylko ludzie nielojalni wobec Cezara. Zapytanie w Prologu potwierdza te podejrzenia:

```
lojalny(markus, cezar)
false
```

## Zad. 2

### a)
```
lubi(jan, X) :-
    pozywienie(X).

pozywienie(jablka).
pozywienie(kurczak).

pozywienie(Y) :-
    zjada(X, Y), \+zabija(Y, X).

zjada(adam, orzeszki).
zjada(basia, X) :-
    zjada(adam, X).

zabija(adam, trucizna).
```

## Zad. 3

### a)
```
urodzony(markus, 40).
zniszczone(pompeje, 79).

martwy(X, Y) :-
    urodzony(X, Z), Y - Z > 150.

martwy(X, Y) :-
    urodzony(X, Z), Z < 79, Y > 79.

zywy(X, Y) :-
    \+martwy(X, Y).
```
```
zywy(markus, 2021)
false
```

Można to wykazać na 2 sposoby:  

Po pierwsze, w 2021 roku Markus miałby 1981 lat, czyli znacznie więcej niż 150, co czyni go martwym.  

Po drugie, Markus urodził się przed rokiem 79 n.e., zatem został zabity przez wybuch Wezuwiusza.
