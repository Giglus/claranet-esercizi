**Nome candidato: Gabriele Giglio
Data: 22.08.2023**


# Esercizio 1 - ContaScript

“Scrivi uno script bash o python che conta il numero di file script in una directory raggruppandoli in base allo shebang interpreter. 

Esempio di output: 
`$ contaScript /usr/bin
81 #!/usr/bin/perl
52 #!/usr/bin/perl5.18
47 #!/bin/sh
44 #!/usr/bin/perl5.28
22 #!/usr/sbin/dtrace -s
…”`

## Soluzione 1 - Python: (claranet-esercizi/Esercizio 1 - ContaScript/contaScript.py)

`import os
from collections import defaultdict`

La prima riga importa il modulo “os” che fornisce funzionalità per l'interazione con il sistema operativo, in questo caso la navigazione delle directory e la gestione dei file.
Nella seconda riga viene importata la classe defaultdict dal modulo collections. Con defaultdict si intende una sottoclasse di dizionario che restituisce un valore predefinito quando si cerca di accedere a una chiave inesistente.

`def contaScript(directory):
    interpreter_count = defaultdict(int)`

Questa riga definisce una funzione chiamata contaScript che prende come argomento il percorso di una directory.
Dentro la funzione, `interpreter_count = defaultdict(int)`, viene creato un oggetto defaultdict che sarà utilizzato per tracciare il conteggio degli interpreti delle linee shabang.

    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".sh"):
                filepath = os.path.join(root, filename)
                with open(filepath, "r") as file:
                    first_line = file.readline().strip()
                    if first_line.startswith("#!"):
                        interpreter_count[first_line] += 1

La prima riga include un ciclo for che utilizza la funzione `os.walk()` per iterare attraverso tutti i file e le directory presenti nella directory specificata e nelle sue sotto-directory.
Nella seconda riga, nel primo ciclo for si scorre attraverso i file nella directory corrente.
Nella terza riga si verifica se il nome del file termina con ".sh", il che indica che potrebbe trattarsi di uno script shell.
Nella quarta riga viene creato il percorso completo al file combinando (effettuando un “join”) la directory radice root con il nome del file filename.
Nella quinta riga è presente una struttura with che apre il file specificato in modalità di lettura ("r"), garantendo che il file verrà chiuso correttamente alla fine dell'uso.
Nella sesta riga viene letta la prima riga del file e viene rimossa qualsiasi spazio bianco iniziale o finale con il metodo strip(). Questa riga rappresenta la presunta linea shabang.
Nella settima riga viene impostata una condizione che verifica se la prima riga inizia con #!, che è un indicatore di una linea shabang.
Nell’ottava riga, se la riga shabang è stata trovata, il conteggio dell'interprete corrispondente viene incrementato di uno all'interno del dizionario interpreter_count.

    for interpreter, count in interpreter_count.items():
        print(f"{count} {interpreter}")

Nella prima riga, dopo aver attraversato tutti i file e le directory, il ciclo successivo for scorre attraverso tutte le coppie chiave-valore nel dizionario interpreter_count.
Per terminare si stampa il conteggio e l'interprete associato

`contaScript("/usr/bin")`

L'invocazione del metodo `contaScript("/usr/bin")` chiamerà la funzione contaScript passando la directory /usr/bin come argomento.

## Soluzione 2 - Python: (claranet-esercizi/Esercizio 1 - ContaScript/contaScript_input.py)

La soluzione 2 è pressoché simile alla soluzione 1, solamente che viene aggiunta questa riga di codice: 

`user_directory = input("Inserisci il PATH di una directory: ")`

La quale stampa a schermo un messaggio che chiede in input il PATH della directory che si vuole analizzare.


# Esercizio 2 - Crontab Backup

“Scrivi una stringa crontab che ogni domenica notte crea un backup della cartella /home/user e lo invia ad un server remoto raggiungibile tramite SSH con user@192.168.1.100 (indica quale configurazione potrebbe essere necessaria per gestire l'autenticazione sul server remoto).”

Soluzione - crontab (claranet-esercizi/Esercizio 2 - Crontab Backup/giglus.txt)

`0 3 * * 7 rsync -az /home/user user@192.168.1.100:/path/to/backup/folder/`

La riga di comando crontab, come richiede l’esercizio, effettua il backup della cartella /home/user e la invia ad un server remoto. La stringa funziona effettuando il comando rsync (copia e sincronizzazione) ogni domenica alle 3 di notte, copiando la cartella sul server remoto tramite SSH.

È inoltre richiesto dalla consegna di indicare la configurazione necessaria al fine di gestire l’autenticazione sul server remoto. Per la gestione dell'autenticazione sul server remoto, si configura l'autenticazione tramite chiavi SSH, generando una coppia di chiavi SSH mediante la riga di codice ssh-keygen -t rsa e copiare la chiave pubblica (~/.ssh/id_rsa.pub) sul server remoto nella directory ~/.ssh/authorized_keys dell'utente user.


# Esercizio 3 - Infrastruttura AWS-Wordpress

“Il team di sviluppo ha rilasciato una nuova web app basata sull'ultima versione di WordPress.

Il tuo compito è creare l'infrastruttura di produzione sulla base di queste indicazioni:

Usa AWS come public cloud provider
Scegli Apache, Nginx o un altro webserver/servizio AWS per pubblicare il sito su internet
I dati devono essere memorizzati in un database MySQL.
[opzionale] L'infrastruttura dev'essere sicura, tollerante ai guasti e in grado di adattarsi a variazioni di carico
[opzionale] Per il provisioning dell'infrastruttura puoi usare lo strumento di IaC che conosci meglio scegliendo tra CloudFormation, Terraform e CDK.

Descrivi in un file di testo tutte le componenti dell'infrastruttura e il motivo per cui hai scelto di usarle. Crea un diagramma infrastrutturale con i servizi che compongono l'infrastruttura e i collegamenti tra di essi.”

Soluzione (claranet-esercizi/Esercizio 3 - Infrastruttura AWS-Wordpress/)

Il documento dettagliato che descrive tutto nel dettaglio si trova all’interno della repository.
