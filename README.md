# 1. Dane Techniczne
## 1.1 Nazwa Gry
Dungeons and pythons

## 1.2 Platformy
- Windows 
- Linux

## 1.3 Widok Kamery
Gracz będzie widoczny w widoku z góry.

## 1.4 Język
Python 3.10.1

## 1.5 Biblioteki
Pygame 2.1.2

# 2. Styl artystyczny
Jest to gra 2D z widokiem z góry w grafice typu PixelArt. Gra nie posida dźwięków.

# 3. Gameplay
Gracz przemierza loch składający się z 5 losowo generowanych poziomów, żeby znaleźć skarb ukryty na końcu. Po drodze napotyka różne potwory próbujące go zatrzymać. Po śmierci gracz musi zacząć swoją podróż od początku. Po drodze znajduje przedmioty dzięki którym może zwiększyć swoje statystyki.

# 4. Mechaniki
## 4.1 Sterowanie
- a/w/s/d -> chodzenie i interakcja
- esc -> wyjście z gry
- r -> reset

## 4.2 Walka
Gracz i potwory atakują gdy jedno z nich spróbuje wejść na to samo miejsce gdzie znajduję się inna istota. Zadawane obrażenia są dzielone przez obronnę danej istoty 

## 4.3 Ruch
Istoty w lochu poruszają się po siatcę.

## 4.4 Przedmioty
Gracz po wejściu na to samo miejsce gdzie znajduję się przemiot automatycznie go podnosi. List przedmiotów:
- miecz -> podnosi siłe o 1
- tarcza -> podnosi obronnę o 1
- mikstura zdrowia -> leczy 5 punktów zdrowia