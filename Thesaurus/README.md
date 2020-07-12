This folder contains a thesarus provided by https://github.com/zaibacu/thesaurus written in json.

# Format
It follows `jsonl` format - meaning, that each line is a separate `json` document.
It contains:
```
word: (String) Actual word
key: (String) Some words can have multiple meanings. Each meaning will have same word, but different key.
pos: (String) part of speech tag, eg. `noun`, `verb`
synonyms: (Array of String) synonyms related to this key
```


