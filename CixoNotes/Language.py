'''
	Plik z klasa zwierajaca wszyskie wyswtietlane przez aplikacje teksty
	Umozliwia latwa zmiane tekstow na takie w innym jezyku
	Tetsty to:
	 * DISPLAY_TEMPLATE - szablon notatki, {date} to string daty a {text} to tekst notatki
	 * NO_NOTES_TEXT - tekst jaki zostanie wyswietlony zamiast notatki gdy uzytkownik notatki nie stworzy
	 * CONFIG_FILE_ERROR - blad jaki pokaze sie gdy brakuje jakis wartosci w pliku konfiguracyjnym
	 * FILE_READWRITE_ERROR - blad jaki pokaze sie gdy nastapi blad zapisu lub odczytu pliku
	 * NOTES_EXIST - tekst jaki pokaze sie gdy uzytkownik zechce stworzyc od nowa juz istniejaca notatke
	 * NOTES_NOTEXIST - tekst jaki pokaze sie gdy uzytkownik zechce dodac tekst do nieistniejacej notatki
	 * BAD_MODE_ERROR - error jaki pokaze sie gdy uzytkownik poda tryb jaki nie istnieje
	 * BAD_DATE_FORMAT - error jaki pokaze sie gdy uzytkownik poda date w zly sposob
	 * NOT_MODE_SET - error jaki pokaze sie gdy uzytkownik uzyje -m albo --mode ale nic dalej nie poda
	 * NOT_DATE_SET - error jaki pokaze sie gdy uzytkownik uzyje -d albo --day ale nic dalej nie poda
	 * WANT_TO_DELETE - pytanie o ty czy napewno chcesz usunac notatke
	 * CONFIRM_LETTER - litera zatwierdzajaca w pytaniach
	 * ADD_TO_NOTE - tekst zachety do dodawania notatki
	 * CREATE_NEW_NOTE - tekst zachety podczas tworzenia notatki
	 * HELP_NOTE - tekst pomocy aplikacji
	 * NOT_CONFIG_FILE - brak pliku konfiguracyjnego
	Funkcje:
	 * tryAllIsSet - sprawdza czy ponizszy plik jest dobrze skonfigurowany
'''

class Language:
	DISPLAY_TEMPLATE = "Notatka na dzień {date} to: \n{text}"
	NO_NOTES_TEXT = "Brak notatki na ten dzień!"
	CONFIG_FILE_ERROR = "Error: Nieprawidłowo skonfigurowany plik konfiguracyjny"
	FILE_READWRITE_ERROR = "Error: Nie można dokonać operacji na dysku"
	NOTES_EXIST = "Istnieje już notatka na ten dzień. Edytować (Y/n): "
	NOTES_NOTEXIST = "Nie istnieje notatka na ten dzień, tworzę nową notatkę"
	BAD_MODE_ERROR = "Error: Nieznany tryb: "
	BAD_DATE_FORMAT = "Error: Nieprawidłowy format daty: "
	NOT_MODE_SET = "Error: Nie podano trybu"
	NOT_DATE_SET = "Error: Nie podano daty"
	WANT_TO_DELETE = "Czy napewno chcesz usunąć notatkę (Y/n): "
	CONFIRM_LETTER = "Y"
	ADD_TO_NOTE = "Podaj co dodać do notatki: "
	CREATE_NEW_NOTE = "Podaj nową treść notatki: "
	HELP_NOTE = "Witaj w aplikacji CixoNotes!\n\nAplikacja służy do tworzenia notatek, które łatwo mogą być wyświetlone na ekranie logowania poprzez dodanie skryptu do .bashrc\nOpcje jakich możesz użyć to:\n\t-d --day <data w formacie ROK-MIESIAC-DZIEN> : zamiast aktualnego dnia uzyje podanego dnia\n\t-m --mode <read|add|write|drop> : odczytuje, dodaje do treści, zaposuje od nowa, kasuje aktualną notatkę\n\t-h --help : wyświetla tę notę"
	NOT_CONFIG_FILE = "Error: Nie ma pliku konfiguracyjnego (~/.config/CixoNotesConfig.py), uruchom cixo-notes-config aby to naprawić"
	
	GOOD_APP_CONFIG = "Poprawnie skonfigurowano aplikację, życzymy miłego użytkowania. Aplikacja jest lepsza również gdy dodasz do .bashrc wpis 'cixo-notes' co odczyta Ci notatkę na dziś za każdym razem gdy otworzysz terminal!"
	BAD_APP_CONFIG = "Nie udało się stworzyć pliku konfiguracyjnego"
	DIR_NOT_EXIST = "Katalog nie istnieje, tworzę"
	NOTES_DIR = "Podaj ścieżkę do notatek ("
	DATE_FORMAT_CONFIG = "Podaj format daty (%Y-%m-%d):"
	CONFIG_FILE_EXIST = "Plik istnieje, usunąć go i zastąpić nowym (Y/n)"
	CONFIG_FILE_HELLO = "Witaj w skrypcie konfiguracyjnym aplikacji cixo-notes\nW twoim katalogu domowym, w katalogu .config pojawi się plik CixoNotesConfig.py, zapisane są tam Twoje dane konfiguracyjne\nSprawdzam czy istnieje już plik konfiguracyjny..."
	
	def tryAllIsSet() -> bool:
		return  'DISPLAY_TEMPLATE' in vars(__class__) and\
				'NO_NOTES_TEXT' in vars(__class__) and\
				'CONFIG_FILE_ERROR' in vars(__class__) and\
				'HELP_NOTE' in vars(__class__) and\
				'NOTES_NOTEXIST' in vars(__class__) and\
				'NOTES_EXIST' in vars(__class__) and\
				'FILE_READWRITE_ERROR' in vars(__class__) and\
				'BAD_MODE_ERROR' in vars(__class__) and\
				'NOT_MODE_SET' in vars(__class__) and\
				'NOT_DATE_SET' in vars(__class__) and\
				'ADD_TO_NOTE' in vars(__class__) and\
				'CREATE_NEW_NOTE' in vars(__class__) and\
				'WANT_TO_DELETE' in vars(__class__) and\
				'CONFIRM_LETTER' in vars(__class__) and\
				'BAD_DATE_FORMAT' in vars(__class__) and\
				'NOT_CONFIG_FILE' in vars(__class__) and\
				'GOOD_APP_CONFIG' in vars(__class__) and\
				'BAD_APP_CONFIG' in vars(__class__) and\
				'DIR_NOT_EXIST' in vars(__class__) and\
				'NOTES_DIR' in vars(__class__) and\
				'DATE_FORMAT_CONFIG' in vars(__class__) and\
				'CONFIG_FILE_EXIST' in vars(__class__) and\
				'CONFIG_FILE_HELLO' in vars(__class__)
		
