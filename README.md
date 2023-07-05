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

### Scouts Panel text
* #__next > form > div > div.MuiCardContent-root > h5

* //*[@id="__next"]/form/div/div[1]/h5
* //*[text()="Scouts Panel"]
* //*[contains(@class,'MuiFormLabel-root MuiInputLabel')]


### Login
* <input type="text" aria-invalid="false" id="login" name="login" value="" class="MuiInputBase-input MuiInput-input">

* //*[@id="__next"]/form/div/div[1]/h5
* //*[@id="login-label"]
* //*[text()="Login"]


### Password
<input type="password" aria-invalid="false" id="password" name="password" value="" class="MuiInputBase-input MuiInput-input">

* //*[@id="password"]
* //*[text()="password"]
* //*[@id="password-label"]

### 'Remind password' button
#__next > form > div > div.MuiCardContent-root > a
<a class="MuiTypography-root MuiLink-root MuiLink-underlineHover jss4 MuiTypography-colorPrimary" tabindex="-1">Remind password</a>
//*[@id="__next"]/form/div/div[1]/a

### Language selection_EN
#__next > form > div > div.MuiCardActions-root > div > div
<div class="MuiSelect-root MuiSelect-select MuiSelect-selectMenu MuiInputBase-input MuiInput-input" tabindex="0" role="button" aria-haspopup="listbox">English</div>
//*[@id="__next"]/form/div/div[2]/div/div

### 'Sign in button
#__next > form > div > div.MuiCardActions-root > button
<span class="MuiButton-label">Sign in</span>
//*[@id="__next"]/form/div/div[2]/button
