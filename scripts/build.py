"""Rebuilds the combined files from the per-country CSVs.

Usage: python scripts/build.py
Standard library only. Edit data/<country>.csv, then run this script.
"""
import csv
import json
import os
import statistics

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, 'data')

COUNTRIES = [
    ('france.csv', 'France'),
    ('united-states.csv', 'United States'),
    ('united-kingdom.csv', 'United Kingdom'),
    ('germany.csv', 'Germany'),
    ('spain.csv', 'Spain'),
    ('india.csv', 'India'),
]

FIELDS = [
    'portal', 'country', 'usage', 'published_cap', 'cap_kb', 'cap_type',
    'total_or_max_files', 'formats', 'source_url', 'date_checked', 'confidence',
]


def cap_type(row):
    if not row['cap_kb'].strip():
        return 'not_documented'
    # LinkedIn and Grants.gov publish a recommended size, not a limit. They stay in the
    # data but is left out of the medians.
    if row['portal'] in ('LinkedIn', 'Grants.gov'):
        return 'recommendation'
    return 'published_cap'


def load():
    rows = []
    for filename, _ in COUNTRIES:
        with open(os.path.join(DATA, filename), encoding='utf-8', newline='') as fh:
            for row in csv.DictReader(fh):
                row['cap_type'] = cap_type(row)
                rows.append({k: row[k] for k in FIELDS})
    return rows


def summarize(rows):
    names = {'FR': 'France', 'US': 'United States', 'UK': 'United Kingdom',
             'DE': 'Germany', 'ES': 'Spain', 'IN': 'India'}
    out = []
    for code, name in names.items():
        subset = [r for r in rows if r['country'] == code]
        caps = [float(r['cap_kb']) for r in subset if r['cap_type'] == 'published_cap']
        out.append({
            'country': code,
            'country_name': name,
            'entries': len(subset),
            'published_caps': len(caps),
            'recommendations': sum(r['cap_type'] == 'recommendation' for r in subset),
            'not_documented': sum(r['cap_type'] == 'not_documented' for r in subset),
            'min_cap_kb': int(min(caps)),
            'median_cap_kb': int(statistics.median(caps)),
            'max_cap_kb': int(max(caps)),
        })
    return out


def write_csv(path, fields, rows):
    with open(path, 'w', encoding='utf-8', newline='') as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, quoting=csv.QUOTE_ALL, lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)


def main():
    rows = load()
    summary = summarize(rows)
    write_csv(os.path.join(DATA, 'all-portals.csv'), FIELDS, rows)
    write_csv(os.path.join(DATA, 'summary-by-country.csv'), list(summary[0].keys()), summary)
    with open(os.path.join(DATA, 'all-portals.json'), 'w', encoding='utf-8') as fh:
        json.dump(rows, fh, ensure_ascii=False, indent=2)
        fh.write('\n')
    print(len(rows), 'entries')
    for line in summary:
        print(line)


if __name__ == '__main__':
    main()
