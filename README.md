# TASK 1
## Subtask 1: konfiguracja oprogramowania.
### Subtask 1: Dlaczego zdecydowałem się wziąć udział w wyzwaniu Dare IT Challenge?

Nazywam się Beata i brałam udział w poprzedniej edycji DARE IT Testowania Manualnego.

Teraz jestem testerką manualną aplikacji mobilnych, ale chciałabym poszerzyć zakres mojej wiedzy, by może w przyszłości wprowadzić testowania automatyczne do moich projektów. Będzie to przydatne przede wszystkim dla mnie w poszukiwaniu pracy w dziedzinie QA, ale też potencjalnie w mojej obecnej pracy.

Spodziewam się, że dowiem się wielu nowych rzeczy, które pomogą mi rozwijać swoje umiejętności, szczególnie, że z testowaniem automatycznym i z Pythonem nie miałam jeszcze do czynienia.

*Beata*


## Podzadanie 2
N/A


## Subtask 3
Wykonano

## Subtask 4

Wynik: 13/14


ZADANIE 2: selektory
## Subtask 1: Zadanie dodatkowe -> Nowy Branch
## Subtask 2: Wyszukiwanie selektorów na stronie logowania. Wymień wszystkie elementy, które znajdują się na stronie logowania.

//*[contains(@type,'sub')]

### Scouts_Panel_text_xpath
* //*[@id="__next"]/form/div/div[1]/h5
* //*[text()="Scouts Panel"]
* //*[contains(@class,'MuiTypography-root MuiTypography')]


### Login_xpath
* //*[@id='login']
* //input[@id='login']
* /input[@name='login']


### Password_xpath
* //input[@id='password']
* /input[@name='password']
* //*[text()="Password"]
  

### Remind_password_button_xpath
* //*[@id="__next"]/form/div/div[1]/a
* //*[contains(@class,'MuiTypography-root MuiLink-root')]
* //*[text()="Remind password"]


### Language_selection_EN_xpath
* //*[@id="__next"]/form/div/div[2]/div/div
* //*[starts-with(@class,'MuiSelect-root Mui')]
* //*[contains(@class,'MuiSelect-root')]

  
### Sign_in_button_xpath
* //*[@id="__next"]/form/div/div[2]/button/span[2]
* //*[contains(@class,'MuiTouchRipple-root')]
* //*[starts-with(@class,'MuiTouch')]
