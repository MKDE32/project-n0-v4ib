# re modul
```
import re

re.search(pattern, text)      # erstes Vorkommen
re.findall(pattern, text)    # alle Treffer als Liste
re.sub(pattern, neu, text)   # ersetzen
re.match(pattern, text)      # nur am Stringanfang
```

# re functions
| Funktion         | Zweck                       |
| ---------------- | --------------------------- |
| `re.search()`    | Erstes Match finden         |
| `re.findall()`   | Alle Matches                |
| `re.finditer()`  | Iterator mit Match-Objekten |
| `re.match()`     | Nur am Anfang               |
| `re.fullmatch()` | Gesamter String muss passen |
| `re.sub()`       | Ersetzen                    |
| `re.split()`     | Aufteilen                   |




# examples

| Zweck             | Regex                  |
| ----------------- | ---------------------- |
| Zahl finden       | `\d+`                  |
| Wort finden       | `\w+`                  |
| Nicht-Leerzeichen | `\S+`                  |
| Beliebiger Text   | `.*`                   |
| URL               | `https?://\S+`         |
| E-Mail            | `[\w.-]+@[\w.-]+\.\w+` |
| Anfang der Zeile  | `^`                    |
| Ende der Zeile    | `$`                    |
| Zeichenmenge      | `[a-z]`                |
| Alles außer X     | `[^X]+`                |





# strings
| Regex | Bedeutung                       | Beispiel | Match        |
| ----- | ------------------------------- | -------- | ------------ |
| `.`   | Beliebiges Zeichen (außer `\n`) | `a.c`    | `abc`, `a7c` |
| `\d`  | Ziffer                          | `\d+`    | `123`        |
| `\D`  | Keine Ziffer                    | `\D+`    | `abc`        |
| `\w`  | Buchstabe, Zahl, `_`            | `\w+`    | `abc_123`    |
| `\W`  | Kein Buchstabe/Zahl/_           | `\W+`    | `!?@`        |
| `\s`  | Leerzeichen, Tab, Zeilenumbruch | `\s+`    | `"   "`      |
| `\S`  | Kein Leerzeichen                | `\S+`    | `hello`      |

# repeat
| Regex   | Bedeutung        | Beispiel  |
| ------- | ---------------- | --------- |
| `*`     | 0 oder mehr      | `ab*c`    |
| `+`     | 1 oder mehr      | `ab+c`    |
| `?`     | 0 oder 1         | `https?`  |
| `{3}`   | Genau 3-mal      | `\d{3}`   |
| `{2,5}` | 2 bis 5-mal      | `\w{2,5}` |
| `{2,}`  | Mindestens 2-mal | `a{2,}`   |


# character sets
| Regex         | Bedeutung         |
| ------------- | ----------------- |
| `[abc]`       | a oder b oder c   |
| `[a-z]`       | Kleinbuchstaben   |
| `[A-Z]`       | Großbuchstaben    |
| `[0-9]`       | Ziffern           |
| `[a-zA-Z0-9]` | Alphanumerisch    |
| `[^abc]`      | Alles außer a,b,c |
| `[^"]+`       | Alles außer `"`   |


# anchors
| Regex | Bedeutung          |
| ----- | ------------------ |
| `^`   | Anfang des Strings |
| `$`   | Ende des Strings   |
| `\b`  | Wortgrenze         |
| `\B`  | Keine Wortgrenze   |



# groups
| Regex     | Bedeutung           |          |
| --------- | ------------------- | -------- |
| `(abc)`   | Capture Group       |          |
| `(?:abc)` | Non-Capturing Group |          |
| `(a       | b)`                 | a ODER b |


# alternatives
| Regex | Bedeutung |              |               |
| ----- | --------- | ------------ | ------------- |
| `cat  | dog`      | cat oder dog |               |
| `jpg  | png       | gif`         | Dateiendungen |






























































