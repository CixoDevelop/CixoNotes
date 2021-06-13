#!/bin/sh

#jest to skrypt instalacyjny CixoNotes, przenosi pliki w odpowiednie miejsca oraz tworzy plik konfiguracyjny

copy_file(){
	echo "	Kopiowanie... $1"
	cp $1 $2 -r
}

is_user_root () { [ "$(id -u)" -eq 0 ]; }

if is_user_root; then
    echo 'Rozpoczynam instalację CixoNotes'
    if test -f "/bin/cixo-notes"; then
		echo 'Usuwam istniejącą instalację cixo-notes'
		./uninstall-it.sh
    fi
	echo 'Kopiowanie plików:'
	copy_file "cixo-notes" "/bin/"
	copy_file "cixo-notes-config" "/bin"
	copy_file "CixoNotes" "/bin/"
    exit 0
else
    echo 'Musisz uruchomić skrypt jako root' >&2
    exit 1
fi
