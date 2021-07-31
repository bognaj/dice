# Kości

Projekt inspirowany rozmowami toczącymi się na wakacjach przy długich rozgrywkach w kości. 


Zasady liczenia punktów:
- wyrzucenie wartości `1` na kostce -> 10 punktów;
- wyrzucenie wartości `5` na kostce -> 5 punktów;
- wyrzucenie takich samych wartości na trzech kostkach -> potrójna wartość pomnożona przez 10
  - `PRZYKŁAD:` wyrzucenie [3, 3, 3] to 30 punktów, wyrzucenie [6, 6, 6] to 60 punktów;
  - `UWAGA:` zasada ta nie dotyczy jedynek: wyrzucenie zestawu [1, 1, 1] to po prostu 30 punktów (10 + 10 + 10);
- wyrzucenie takich samych wartości na 4 kostkach
  - `PRZYKŁAD:` wyrzucenie [3, 3, 3, 3]. Zgodnie z poprzednim podpunktem [3, 3, 3] oznacza 30 punktów. Mnożymy wynik przez kolejną trójkę i otrzymujemy 90 punktów. Analogicznie zestaw [6, 6, 6, 6] ma wartość 360 punktów;
  - `UWAGA:` w przypadku wyrzucenia zestawu [1, 1, 1, 1] przyznawane jest 1000 punktów;
- wyrzucenie takich samych wartości na 5 kostkach
  - `PRZYKŁAD:` wyrzucenie [3, 3, 3, 3, 3] to zgodnie z poprzednimi podpunktami 90x3 = 270 punktów, analogicznie zestaw [6, 6, 6, 6, 6] to 360x6 = 2160 punktów;
  - `UWAGA:` wyrzucenie [1, 1, 1, 1, 1] to 1000 punktów;
- po każdym rzucie odkłada się na bok punktowane kości i wykonuje się rzuty pozostałymi
  - `PRZYKŁAD 1:` gracz wyrzucił w pierwszym rzucie [1, 3, 2, 6, 3]. Zdobywa 10 punktów za wyrzucenie jedynki. Następny rzut wykonuje czterema kośćmi. Wyrzuca [4, 5, 4, 4]. Zdobywa 45 punktów. Wszystkie kości dostarczyły punktów, następny rzut wykonuje zatem wszystkimi kośćmi. 
  - `PRZYKŁAD 2:` gracz w pierwszym rzucie otrzymał zestaw [2, 2, 4, 6, 6]. Nie ma tu żadnych punktowanych zestawów, stąd przekazuje on kości następnemu graczowi.
  - `PRZYKŁAD 3:` graxz w pierwszym rzucie otrzymał zestaw [1, 1, 1, 1, 6]. Otrzymuje 100 punktów, decyduje nie kontynuować rzutów, zapisuje tę wartość i przekazuje kości następnemu graczowi.
- w przypadku braku zapisania wyniku i braku punktowego wyniku na kościach, punkty przepadają;
- aby wejść do gry należy zdobyć i zapisać 75 punktów;
- zapisać można wartości >= 25;
  - `UWAGA`: gdy wynik oscyluje w okolicy 900 możliwe jest zapisanie dowolnej liczby punktów;
- gdy gracz zdobędzie >= 900 punktów brakującą do 1000 wartość musi otrzymać w jednej kolejce
  - `PRZYKŁAD:`: zawodnik ma 870 punktów. W następnej kolejce zdobywa i zapisuje 80 punktów. 870+80=950, stąd może odtąd zapisać wyniki nie mniejsze niż 1000-950=50 punktów.
- gra toczy się do momentu uzyskania przez jednego z graczy 1000 punktów.
