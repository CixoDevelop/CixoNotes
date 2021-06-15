#Witaj w pojekcie CixoNotes

##Wprowadzenie
Aplikacja CixoNotes to aplikacja podobna do Sticky Notes znanego z Windows 7, lecz działa na linuxie w terminalu. Po prostym wywołaniu cixo-notes zobaczymy notatkę na dziś, wywołanie takie najlepiej umieścić w .bashrc, aby widzieć je za każdym otwarciem terminala.

##Wymagane technologie
 * python >3.5
 
##Instalacja
...
 $ git clone https://github.com/CixoDevelop/CixoNotes.git
 $ cd CixoNotes
 $ sudo ./install-it.sh
 $ cixo-notes-config
 $ (opcjonalnie) echo cixo-notes > .bashrc
...

##Deinstalacja
...
 $ git clone https://github.com/CixoDevelop/CixoNotes.git
 $ cd CixoNotes
 $ sudo ./uninstall-it.sh
...

##Użytkowanie
 * cixo-notes : pokaże notatkę na dziś
 * cixo-notes <opcja> <wartosc>
 *  -d --day <%Y-%m-%d> : zamiast aktualnego dnia użyje dnia podanego w parametrze
 *  -m --mode <write|add|drop|read> : 
 *    * read - odczyta notatkę (domyślne)
 *    * add - doda do istniejącej notatki kolejną treść
 *    * drop - usunie istniejącą notatkę
 *    * write - stworzy notatkę
 
##Przykłady użycia
 * cixo-notes --day 2021-06-12 : pokaże notatkę na 12 czerwca 2021
 * cixo-notes -m write : stworzy notatkę na dziś
 * cixo-notes --mode drop --day 2021-06-11 : usunie notatkę z dnia 11 czerwca 2021
 
##Pliki projektu
 * cixo-notes.py : główny skrypt
 * cixo-notes-config.py : skrypt konfigurujący aplikację dla użytkownika
 * install-it.sh : skrypt instalujący aplikację w systemie
 * uninstall-it.sh : skrypt usuwający aplikację z systemu
 * readme.md : ten plik
 * todo.md : plik zawierający plany nowych treści do aplikacji
 * cixo_notes : moduł z klasami potrzebnymi do działania aplikacji
 * cixo_notes/notes_class.py : plik przechowujący klasę notatki 
 * cixo_notes/notes_saver.py : plik reprezentujący notatkę w systemie plików
 * cixo_notes/language.ini : plik z tekstami jakie pokazuje aplikacja
