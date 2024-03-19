## Ćwiczenie 11

lubi(jan, pawel). <br>
lubi(pawel, krzysztof). <br>
lubi(pawel, jan). <br>
lubi(jan, bartek). <br>
lubi(bartek, jan). <br>

mezczyzna(jan). <br>
mezczyzna(pawel). <br>
kobieta(kasia). <br>
kobieta(zosia). <br>

kocha(jan, kasia). <br>
kocha(kasia, jan). <br>
kocha(pawel, zosia). <br>
kocha(krzysztof, linux). <br>

przyjazn(X, Y) :- <br>
    lubi(X, Y), <br>
    lubi(Y, X).

niby_przyjazn(X, Y) :- <br>
    lubi(X, Y); <br>
    lubi(Y, X).

### 1. 
nieprzyjazn(X, Y) :- <br>
    \\+lubi(X, Y), <br>
    \\+lubi(X, Y).


### 2. 
zrobione wyżej

### 3. 
loves(X, Y) :- <br>
    (kocha(X, Y); kocha(Y, X)), <br>
    (mezczyzna(X), kobieta(Y); kobieta(X), mezczyzna(Y)).

### 4. 
true_love(X, Y) :- <br>
    (kocha(X, Y), kocha(Y, X)), <br>
    (mezczyzna(X), kobieta(Y); kobieta(X), mezczyzna(Y)).
