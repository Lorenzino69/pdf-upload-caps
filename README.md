# PDF upload caps on public portals (2026)

How large can a PDF be before a government, university or job portal rejects it? This dataset records the published file size limit of 162 portals in France, the United States, the United Kingdom, Germany, Spain and India, each with the exact wording of the limit and a link to the official page where it was found.

It was collected in September 2026 for the EasyPDF study [The 1 MB Problem: PDF File Size Statistics for 2026](https://www.easypdf.fr/blog/pdf-file-size-statistics-2026) (French version: [Le problème du 1 Mo](https://www.easypdf.fr/fr/blog/statistiques-taille-fichier-pdf-2026)).

## Key figures

| Country | Entries | Published caps | Not documented | Lowest cap | Median cap | Highest cap |
|---|---|---|---|---|---|---|
| France | 29 | 22 | 7 | 500 KB | 5 MB | 200 MB |
| United States | 18 | 10 | 7 | 2,000 KB | 20 MB | 100 MB |
| United Kingdom | 12 | 8 | 4 | 1 MB | 5.5 MB | 100 MB |
| Germany | 30 | 17 | 12 | 3 MB | 10 MB | 200 MB |
| Spain | 30 | 22 | 7 | 2 MB | 10 MB | 100 MB |
| India | 44 | 18 | 25 | 150 KB | 500 KB | 25 MB |

- The United States and the United Kingdom taken together (18 published caps) have a median of 10 MB, the figure used in the study.
- 62 of the 163 entries publish no limit at all: the user finds out when the upload fails.
- Indian exam and recruitment forms are the strictest group: most PDF caps sit between 150 and 500 KB, and several also set a minimum size.
- LinkedIn publishes a recommended size (2 MB), not a limit. Its four entries are kept in the data with `cap_type = recommendation` and are left out of the medians.

The dataset has 163 entries for 162 portals because the French ANTS agency publishes two different caps for two services.

## Files

| File | Content |
|---|---|
| `data/all-portals.csv` | All 163 entries, one row per portal and usage |
| `data/all-portals.json` | Same content as JSON |
| `data/summary-by-country.csv` | Counts, lowest, median and highest cap per country |
| `data/france.csv`, `data/germany.csv`, `data/spain.csv`, `data/india.csv`, `data/united-states.csv`, `data/united-kingdom.csv` | Source files per country, the ones to edit |
| `scripts/build.py` | Rebuilds the combined files from the per-country files (Python standard library only) |
| `datapackage.json` | Frictionless Data descriptor |

All files are UTF-8, comma separated, every field quoted.

## Columns

| Column | Description |
|---|---|
| `portal` | Name of the portal or service |
| `country` | `FR`, `US`, `UK`, `DE`, `ES` or `IN` |
| `usage` | What the upload is for (resume, supporting document, exam certificate...) |
| `published_cap` | The limit as worded on the source page, in the original language, or `not documented` |
| `cap_kb` | The same limit in kilobytes (1 MB = 1,024 KB), empty when not documented |
| `cap_type` | `published_cap`, `recommendation` or `not_documented` (combined files only) |
| `total_or_max_files` | Any limit on the total size of a submission or on the number of files |
| `formats` | Accepted file formats |
| `source_url` | Page where the figure was read |
| `date_checked` | Date the page was checked (ISO 8601) |
| `confidence` | `official` (the portal's own help or documentation), `institutional` (another public body or the software vendor) or `not documented`, followed by caveats in brackets when the figure needs context |

## Method and limits

- Each portal's own help pages, FAQs, user guides and technical documentation were searched for a published limit on uploaded PDF files. Figures quoted only by third-party sites were not used.
- When a portal publishes several limits, the one applying to the most common PDF upload by an individual was kept, and the others are described in `total_or_max_files` or `confidence`.
- `not documented` means no figure was found in public documentation on the date checked. The portal may still enforce a limit inside the logged-in area.
- Some caps are totals per submission rather than per file (CAF in France, several Spanish e-registries, the German JOBBÖRSE). This is stated in `total_or_max_files`.
- Portals change their limits without notice. Check `source_url` before relying on a figure, and see below to report a change.
- The selection of portals is not a random sample. It covers the services individuals use most for job applications, higher education, benefits, tax, immigration, justice and exams in each country.

## Corrections and additions

Found a limit that changed, or a portal that is missing? Open an issue or a pull request that edits the relevant `data/<country>.csv` file, with the official source URL and the date you checked it. Then run:

```bash
python scripts/build.py
```

## License and citation

The data is published under [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) (see `LICENSE`). The build script is under the MIT license (see `LICENSE-CODE`).

You can reuse, republish and adapt the data, including commercially, as long as you credit the source with a link:

> Source: [EasyPDF, PDF upload caps on public portals (2026)](https://www.easypdf.fr/blog/pdf-file-size-statistics-2026)

Citation metadata is in `CITATION.cff`.

## En français

Ce jeu de données recense le plafond de taille publié pour l'envoi d'un PDF sur 162 portails publics et privés (emploi, études, aides, impôts, justice, concours) dans six pays, avec la formulation exacte du plafond et le lien vers la page officielle. En France, les 22 plafonds publiés vont de 500 Ko (HelloWork) à 200 Mo (Démarches simplifiées), avec une médiane de 5 Mo, et 7 portails ne publient aucun chiffre (impots.gouv.fr, Ameli, Parcoursup, messervices.etudiant.gouv.fr, Mon Compte Formation, Action Logement, Indeed).

Analyse complète : [Le problème du 1 Mo : statistiques taille PDF 2026](https://www.easypdf.fr/fr/blog/statistiques-taille-fichier-pdf-2026). Réutilisation libre sous licence CC BY 4.0, en citant la source avec un lien.

## About

Collected and maintained by [EasyPDF](https://www.easypdf.fr), an online PDF editor and compressor. Contact: hello@easypdf.fr
