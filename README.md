## Creating new projects

You can create new projects by adding new Markdown files in the [\_projects](_projects/) directory. The easiest way to do this is to copy an existing project and modify it.

## Adding a new publication

To add publications create a new entry in the [\_bibliography/papers.bib](_bibliography/papers.bib) file. You can find the BibTeX entry of a publication in Google Scholar by clicking on the quotation marks below the publication title, then clicking on "BibTeX", or also in the conference page itself. By default, the publications will be sorted by year and the most recent will be displayed first. 

You can add extra information to a publication, like a PDF file in the `assets/pdfs/` directory and add the path to the PDF file in the BibTeX entry with the `pdf` field. Some of the supported fields are: `abstract`, `altmetric`, `annotation`, `arxiv`, `bibtex_show`, `blog`, `code`, `dimensions`, `doi`, `eprint`, `html`, `isbn`, `pdf`, `pmid`, `poster`, `slides`, `supp`, `video`, and `website`.

### Author annotation

If the entry matches one form of the last names and the first names, it will be underlined. Keep meta-information about your co-authors in [\_data/coauthors.yml](_data/coauthors.yml) and Jekyll will insert links to their webpages automatically. The co-author data format is as follows,

```yaml
"adams":
  - firstname: ["Edwin", "E.", "E. P.", "Edwin Plimpton"]
    url: https://en.wikipedia.org/wiki/Edwin_Plimpton_Adams

"podolsky":
  - firstname: ["Boris", "B.", "B. Y.", "Boris Yakovlevich"]
    url: https://en.wikipedia.org/wiki/Boris_Podolsky

"rosen":
  - firstname: ["Nathan", "N."]
    url: https://en.wikipedia.org/wiki/Nathan_Rosen

"bach":
  - firstname: ["Johann Sebastian", "J. S."]
    url: https://en.wikipedia.org/wiki/Johann_Sebastian_Bach

  - firstname: ["Carl Philipp Emanuel", "C. P. E."]
    url: https://en.wikipedia.org/wiki/Carl_Philipp_Emanuel_Bach
```

If the entry matches one of the combinations of the last names and the first names, it will be highlighted and linked to the url provided.

### Buttons (through custom bibtex keywords)

There are several custom bibtex keywords that you can use to affect how the entries are displayed on the webpage:

- `abbr`: Adds an abbreviation to the left of the entry. You can add links to these by creating a venue.yaml-file in the \_data folder and adding entries that match.
- `abstract`: Adds an "Abs" button that expands a hidden text field when clicked to show the abstract text
- `altmetric`: Adds an [Altmetric](https://www.altmetric.com/) badge (Note: if DOI is provided just use `true`, otherwise only add the altmetric identifier here - the link is generated automatically)
- `annotation`: Adds a popover info message to the end of the author list that can potentially be used to clarify superscripts. HTML is allowed.
- `arxiv`: Adds a link to the Arxiv website (Note: only add the arxiv identifier here - the link is generated automatically)
- `bibtex_show`: Adds a "Bib" button that expands a hidden text field with the full bibliography entry
- `blog`: Adds a "Blog" button redirecting to the specified link
- `code`: Adds a "Code" button redirecting to the specified link
- `dimensions`: Adds a [Dimensions](https://www.dimensions.ai/) badge (Note: if DOI or PMID is provided just use `true`, otherwise only add the Dimensions' identifier here - the link is generated automatically)
- `html`: Inserts an "HTML" button redirecting to the user-specified link
- `pdf`: Adds a "PDF" button redirecting to a specified file (if a full link is not specified, the file will be assumed to be placed in the /assets/pdf/ directory)
- `poster`: Adds a "Poster" button redirecting to a specified file (if a full link is not specified, the file will be assumed to be placed in the /assets/pdf/ directory)
- `slides`: Adds a "Slides" button redirecting to a specified file (if a full link is not specified, the file will be assumed to be placed in the /assets/pdf/ directory)
- `supp`: Adds a "Supp" button to a specified file (if a full link is not specified, the file will be assumed to be placed in the /assets/pdf/ directory)
- `website`: Adds a "Website" button redirecting to the specified link

You can implement your own buttons by editing the [\_layouts/bib.liquid](_layouts/bib.liquid) file.

## Add personal pages

Add new Markdown files in the [\_people](_people/) directory.

```
---
layout: page
title: your position
description: A short intro
img: assets/img/your_photo
importance: 1
category: 
github: https://github.com/user_name
email: 
redirect: your website (if you have)
---

Your personal page.
```
