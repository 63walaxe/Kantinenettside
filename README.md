# Kantinenettside

Dette er en nettside for kantina på skolen som jeg har laget i Flask. På siden kan du se hva kantina selger, hva som er ukens meny og hvordan du kan kontakte kantina.

## Hva er på siden

- **Hjem** - en liten velkomstmelding
- **Varer** - drikke og mat med bilde, pris, kalorier og allergener
- **Meny** - en varmrett for hver dag i uka, og på fredag er det pizza
- **Kontakt** - telefon, e-post, adresse og når kantina er åpen

## Hvordan kjøre den

Først oppretter du et venv:

python3 -m venv env

Så aktiverer du venv:

source env/bin/activate

Hvis du ikke har flask må du installere det:

pip install flask

Så starter du siden med:

python app.py

Og så åpner du http://127.0.0.1:5000 i nettleseren.

## Litt om filene

- `app.py` har alle rutene
- `data.py` er der alle varene, menyen og kontaktinfoen ligger
- `templates/` har html-filene, og alle arver fra `base.html`
- `static/style.css` er stylingen

## Kilder

Datasettet med varer i `data.py` er generert med KI. Kaloriene og allergenene er bare ca, så de er ikke helt riktige.

Klassene og grunnleggende styling i `style.css` er laget med litt hjelp fra KI.

Bildene er tatt fra forskjellige nettsider på nettet og er ikke mine.

Kontaktinfoen til kantina er funnet på.
