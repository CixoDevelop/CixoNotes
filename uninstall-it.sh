#!/bin/sh

remove_file(){
	echo "	Usuwam... $1"
	rm $1 -r
}

is_user_root () { [ "$(id -u)" -eq 0 ]; }

if is_user_root; then
	if test -f "/bin/cixo-notes"; then
		echo "Deinstalacja cixo-notes:"
		remove_file "/bin/cixo-notes"
		remove_file "/bin/cixo-notes-config"
		remove_file "/bin/CixoNotes" 2> /dev/null
		remove_file "/bin/cixo_notes"
	else
		echo "Nie zainstalowano CixoNotes!"
	fi
else
    echo 'Musisz uruchomić skrypt jako root' >&2
    exit 1
fi
