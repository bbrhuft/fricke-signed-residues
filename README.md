# Supersingular poles and signed residues of prime-level Fricke Hauptmoduln

Manuscript, code and data for:

> Jordan, D. (2026). *Supersingular poles and signed residues of prime-level Fricke Hauptmoduln* [Manuscript, version 1.11]. Maynooth University Social Sciences Institute, Maynooth University.

The research was AI-assisted, and the paper has not yet been refereed.

## Repository layout

| Path | Contents |
|---|---|
| `paper/` | Manuscript source (`.tex`) and compiled PDF, version 1.11 |
| `supplementary/Signed_Weighted_Residue_v1_0/` | Signed weighted-residue code, per-pair JSON results, proof note (levels 2, 3, 5, 7, 13) |
| `supplementary/Eta_Frobenius_Lemma_Audit_v1_0/` | Eta-multiplier and Vélu sign audit: code, results, audit report |
| `supplementary/Factorial_Conjecture_Result_v1_0/` | Factorial-evaluation code and recorded results under `new_work/`; reproduce with `new_work/run_all.sh` |
| `supplementary/Fricke_Elliptic_Values_Fifteen_Levels_v1_0/` | Exact elliptic values and model calculations for all fifteen levels (Table 2) |
| `supplementary/Theorem_1_3_Benchmark_v1_0/` | Timing code, exact inputs and outputs, raw timings, verification records |
| `supplementary/Corollary_1_2_Reconstruction_Benchmark_v1_0/` | Reconstruction benchmark: code, results, verification records |

Each package has its own README with reproduction instructions and a SHA-256 manifest. The packages are included exactly as archived, with one exception: three copyrighted third-party papers were removed from `Factorial_Conjecture_Result_v1_0/sources/`. See the `REMOVED_FROM_PUBLIC_REPO.md` file in that folder.

## Software environment

All computations use exact arithmetic. Tested with Python 3.13 on Linux x86_64.

- `python-flint` 0.9.0
- `mpmath` 1.3.0
- `cypari2` 2.2.4, bundling PARI/GP 2.17.2 (factorial package only)
- A C compiler for the optional native kernels in the two benchmark packages

Pinned versions are in each package's `requirements.txt`.

## Verifying file integrity

From inside a package directory:

```sh
sha256sum -c SHA256SUMS.txt
```

## Licence

- **Code** (all `*.py`, `*.c`, `*.gp`, `*.sh` files): MIT Licence; see `LICENSE`.
- **Manuscript and notes** (`paper/` and the `.tex`/`.pdf` notes inside the packages): © 2026 David Jordan, all rights reserved, pending journal publication.
- **Data** (JSON, CSV and log outputs): free to reuse with attribution.

## Contact

David Jordan, Maynooth University Social Sciences Institute (MUSSI), Maynooth University, Maynooth, Co. Kildare, Ireland. David.Jordan@mu.ie
