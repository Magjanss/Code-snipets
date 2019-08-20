
# Dagbok
    Detta är tänkt som ett dokument som håller reda på det som gjorts och det som ska göras.

## Allmänt:
Saker som är klara:
* VSCODE
    1. Installerade vscode
        * sudo apt purge snapd
        * sudo apt install snapd
        * sudo snap install --classic code
    2.  Fixade exstension
        * Markdown
        * python
        * gitlens
* Python-pip
    1. installerade pip
       * sudo apt install python3-pip
* Selenium
    1. Installerade med:
        * pip3 install -U selenium
          Successfully installed selenium-3.141.0
* geckodriver
    1. https://github.com/mozilla/geckodriver/releases
    2. Installerade genom att lägga geckdriver filen i /user/local/bin




## Krav
-  [x] En användare skall kunna skriva in ett meddelande i ett fält, 
  -  [x] meddelandet får max ha 140 tecken.
-  [x] En användare skall kunna, genom att klicka på en knapp,
        publicera sitt meddelande. Innan meddelandet publiceras
        skall det valideras med JavaScript. Om meddelandet är
        tomt eller mer än 140 tecken skall det inte publiceras
        och ett felmeddelande skall visas för användare (obs,
        använd inte "alert" för felmeddelande).
- [x] Ett meddelande som är publicerat skall visas i kronologiskt
        fallande (senast först) ordning nedanför textfältet.
- [x] Alla meddelanden som visas skall ha en knapp som när man 
        klickar markerar meddelandet som läst.
- [x] Det skall vara tydlig skillnad mellan lästa och olästa meddelanden.
- [x] Alla meddelanden skall försvinna när man laddar om sidan.
- [ ] Alla krav skall testas med Selenium.
- [x] Layouten skall likna schema 1.
- [x] Att själv lära sig den HTML, CSS, JavaScript och Selenium 
        kunskap som behövs för att genomföra laborationen.
- [x] Det är valfritt om man vill använda ren JavaScript eller jQuery

## Bra att veta:
* ctrl + shift + v : toggle markdown preview

## TODO
-  [ ] Testa med selenium:
   -  [x] Meddelanden
   -  [x] Meddelande stoŕlek
   -  [ ] kronologisk ordning
   -  [ ] knapp som markerar läst
   -  [ ] Tydlig skillnad?
   -  [ ] Meddelanden försvinner vid reload