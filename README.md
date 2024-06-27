# Qrcode generator

Non c'è molto da dire su questo programa. Il titolo dice già tutto (penso?)😅

### indice
- installazione
- come funziona ? 🤔

## installazoine

In relata se siete utenit Windows non serve istallare nulla. trovate il fai .exe già pronto.il file .exe si trova al percorso riportato qui sotto 🔽

    \Qrcode_generator\dist\querreCode\querreCode.exe

### Linux 
Per i sitemi Linux bisogna acertarsi di avere queste componetni.
Per eseguire il codice bisogna installare python consiglio(non obligatoria) la versione 3.11.7.  

Per la componete grafica installare Kivy (melgio se la versione 2.3.0)  

    pip install Kivy
per mggiori info lascio anche il link per la libreria [Kivy](https://kivy.org/)  

NB: il file querrecode.kv e il file che gestisce la parte grafica. Diciamo che è un simil file css.La libreria e compatibile per essere coimplialta per file .exe, .apk, eccc (puo essere compilata per Windous, Linux, Macos, Android, Ios nel caso si volesse creare una app mobile )

Invece querreCode.py gestisce la parte logica che andra a generare il qrcode.    

Per la generazione del qrcode installare PyQRCode (meglio la verisone  1.2.1)  

    pip install pyqrcode

Per mggiori info lascio anche il link per la libreria [pyqrcode](https://pypi.org/project/PyQRCode/)  

    pip install pypng

Questa libreria serve per poter salvare il file nel formato PNG (formato di immagine)

Poi inseriamo al inizio del file python queta stringa di codice

     #!/usr/bin/env python3

Ciò permette di redere il file exeguibile senza dover pasare per l'interprete python.

Poi bisogna dargli i permessi di eseguzione 

    chmod +x /percorso/completo/al/tuo/script/nome del tuo 
    script.py

Ora basta creare il file .desktop per avere un launcer cioè un lanciatore della applicazione, ovviamnte sul desktop (l'icone sul desktop)

    ini
    [Desktop Entry]
    Version=1.0
    Name=MyApp
    Comment=Descrizione della mia applicazione
    Exec=/percorso/completo/al/tuo/script/nome del tuo 
    script.py
    Icon=/percorso/completo/alla/tua/icona.png
    Terminal=false  
    Type=Application
    Categories=Utility;Application;

anche a questo file bisogna dare i permessi di eseguzione

    chmod +x /percorso/completo/a/nome defl file .desktop

Congraturlazione ora facendo un click sul file realizato prima comparia l'icona della vostra applicazoipne e clicandoci sopra si avviera.👍 

## come funziona? 🤔

Molto semplice. Appena si avvia l'applicazione vedremo questa scermata.

![plot](c.png)

Ora bastera riempire i campi richiesti  
 - url : inserire l'indirizzo link che si vuole convertire in qrcode.
 - name: il nome del file che vera generato.
 - scala: e la grandezza della immagine. di defoult e impostato a 15%.
 - poi si puo decidere il colore dello sfondo e dei quadrati neri . Se non modificati lo sfondo e bianco e i quadrati neri.

Ultimo passagio cliccare il tasto **Clik**

⚠⚠ **Il file vera generato nella stessa cartella del eseguibile** (più avanti implementero anche la possibilita di scelgiere la cartella dove salvare il file)⚠⚠
