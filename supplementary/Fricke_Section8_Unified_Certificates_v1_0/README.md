# Unified Section 8 certificates and replacement text

6 November 2026.

This package reruns the existing exact certification routines at all fifteen prime levels
2,3,5,7,11,13,17,19,23,29,31,41,47,59,71 over one common range:
prime 5<=p<=47, excluding p=N. It is a presentation/consolidation exercise,
not a claim that this common range had never previously been checked.

## Drop-in manuscript text

`Section_8_Certificates_Replacement.tex` replaces the beginning of Section 8,
from its section heading up to, but not including,
`\subsection{Computational consequences and timings}` in v1.10.
Keep the timings subsection and the existing Data and software paragraph.
If working from a manuscript without that timing subsection, replace the
finite-certificate/evidence text up to the Data and software paragraph instead.

The replacement retains the finite-certificate proposition and its proof verbatim.
It replaces the two certificate tables with one table covering all fifteen levels
at the same primes, and shortens the surrounding account. Old table labels are
retained as aliases for the unified table, preventing broken cross-references.
The stronger archived five-level range through p=211, candidate-free/Hecke checks,
and further double-pole checks are retained in a short paragraph. Separate Velu
and factorial checks remain identified as separate computations.

No earlier manuscript sections are supplied as replacement text. In particular,
this fragment will not overwrite the user's local Proposition 3.4 edit. The
benchmark table is deliberately not merged with the certificate table: it measures
a different task and has different coverage/input contracts.

## Reproduce

```
python -m pip install python-flint==0.9.0
python run_all.py
python create_revision.py
```

Run from a copy to preserve the supplied fresh records. `run_all.py` writes
unified_results.json, raw_results.json and console output. It uses the unmodified
inherited routines in inherited/. Full source precision is at least p^3+2;
these are finite certificates, not only product-formula reconstructions. The
five-level and ten-level coordinate models differ as described in the text,
so a unified table does not imply a single coordinate model or identical code.

`create_revision.py` also checks every fresh numerator and denominator against
its archived counterpart. Its default manuscript is the unchanged v1.10 TeX under input/.
It does not read or overwrite your later locally edited manuscript. It produces a validation manuscript only for compilation;
that file is not intended to replace a later locally edited manuscript.

## Contents

- Section_8_Certificates_Replacement.tex: insertion-ready fragment.
- counts.json: per-level counts, totals and verification summary.
- unified_results.json / raw_results.json / run.log: new calculation records.
- run_all.py / create_revision.py: reproduction and text-generation scripts.
- inherited/: unchanged original fifteen-level package, including model data,
  historical records and their original hashes. Historical status language there
  does not replace the theorem statements in v1.10.
- INPUT_PROVENANCE.json / SHA256SUMS.txt: source identities and release hashes.

Original input manuscripts and evidence archives are not modified. The validation
PDF and temporary compilation files are internal layout checks, not new results.
