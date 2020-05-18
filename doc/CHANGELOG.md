# Changelog

## 1.6.0-dev
- Correctly implement iterator protocol for MarkdownReader. This will enable users to use `next(iterator_content)` rather than rely on indexes.

## 1.5.0

- Major depencies updates including pattern matching callbacks & better performance building graphs
- Navbar highlight bug corrected

## 1.4.5

- New sidebar menu, both the menu and the content are now a bit more responsive
- Expose HEVA's plotly theme in app.py for ease of use
- Remove uneeded dependencies for a lighter deployment
- New favicon

## 1.4.4

- Major improvements on deployment
- Analytics cookies & RGPD compliance
- Toolbar component
- Quality checklist :white_check_mark:

## 1.4.3

- Visual improvements

## 1.4.2

- Improve simple tables. Using DataFrames, users may now reorient tables & group row by a label
- Allow users to pass a configuration dict to figure in order to change image export size for example
- Major dependencies updates, dashboard should be notably more reactive

## 1.4.1

- Fix title padding in graph sections
- Fix an issue with tables from csv: strip empty lines

## 1.4.0

- Add utils to make tables from csv files
- Add utils to easily split markdown files in sections
- Add eula page
