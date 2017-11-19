**************
Pandas
**************


Miks
=====
* Miks mitte Excel?
* Miks mitte Pythoni dict ja list?

Plaan
======
* Top-down: Alustan csv/Exceli laadimisega => DataFrame => Series
    * Mida saab Series-iga teha (nt. korrutada arvuga, võrrelda)
    * Näita kahe indeksi liitmist (sh. NaN-ideg)
    * näita kahest eri failist erineva info ühendamist indeksi abil
* näitan universaalseid operatsioone enne ja spetsiaalseid hiljem
    * nt replace üldosas ja fillna spets-osas
* Eeldan tidy formaati?
    * siis peab näitama, kuidas seda saada
* Võiks olla mingi näide, mida oleks Exceliga raske teha
* Sõna indeks: kas see on üks võti või mitu?
* dot-süntaksi näitad alles hiljem, trikkide juures

Gotchas
===========
* http://www.elasticmining.com/post/2015-12-24/gochas-using-pandas.html
* Indeksit ei tohi unustada! Series ei ole list. (Too sisse primary key mõiste??)
* Indeksit võib ignoreerida kuni DF-de kombineerimiseni
    * aga mõnikord on kombineerimine implicit
* NaN-iga tuleb olla tähelepanelik
* Muteerimine uue veeru lisamiseks vs copy warning:
    * https://stackoverflow.com/questions/43423347/why-is-blindly-using-df-copy-a-bad-idea-to-fix-the-settingwithcopywarning
    * https://stackoverflow.com/a/43165629/261181
* Data type conversion (including NaN-s)
* ole tähelepanelik, mis tagastab koopia ja mis vaate
* veergude muutmisel soovitada teha uus veerg ja üle kirjutada?
    * df["blaa"] = df["blaa"].replace(...) ??
    * Siis saab öelda, et aluseks ongi uute veergude tegemine
* ridade filtreerimisel (ja tulemuse hilisemal muutmisel) tuleb arvestada ka warninguga. Soovitada sel juhul filtreerimisoperatsiooni lõppu panna copy? Kas veergude filtreerimisel samuti?
* changing copies instead of views
* https://stackoverflow.com/questions/23296282/what-rules-does-pandas-use-to-generate-a-view-vs-a-copy
* Sometimes you want copy but Pd warns about it
* Prefere pure operations??
* Don't confuse arrays and series
* | ja & tingimused tuleks sulgudesse panna
* selecting bool-indexing Numpy array always creates a copy. Pandas as well?
    - that's the reason behind double-indexing issues

Operatsioonid
==============
* Series => Series
    .isin
    .
* indexing
    * Mess: https://github.com/pandas-dev/pandas/issues/9595
* loc, iloc
    * shortcuts
* sorting
    * df.sort_index
    * df.sort_values
    * s.sort_values
* drop
* summaries (reducing dimensions / amount)
    * describe
    * min, max
    // * idxmax (ei maksa näidata, kuna ei anna mitut suurimat)
    * sum, mean
* unique, value_counts
* io
    * peab saama käsitsi DF kokku panna (parim: from dict)
* NA
    * isnull, notnull
    * fillna
* .drop_duplicates
* replacing
    * by looking on values only
    * by key
    * df.replace on vist ka kasulik
    * rename keys
* iteration ???
* query ?
* concat from several files, add column identifying file
    * add column before concat
    * use concat(..., keys=...)