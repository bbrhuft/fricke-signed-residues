# A factorial supersingular congruence and signed discriminant ratios

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24084789.svg)](https://doi.org/10.5281/zenodo.24084789)

**David Jordan** · Maynooth University Social Sciences Institute (MUSSI), Maynooth University · Manuscript v1.13, 7 November 2026

> This repository was previously titled *Supersingular poles and signed residues of prime-level Fricke Hauptmoduln* (manuscript v1.11). From v1.13 the paper leads with the factorial congruence and the discriminant-ratio sign; the Fricke residue formula is now the main application.

## About the paper

Let $`p \ge 5`$ be prime, $`h = (p-1)/2`$ and $`k = (p^2-1)/24`$. Baker's supersingular congruence determines the *square* of a ratio formed from $`E_{p+1}`$ and $`\Delta`$. The paper evaluates the ratio itself: on the supersingular locus it equals a factorial times a Legendre symbol, the same for every supersingular elliptic curve. Combined with Robert's isogeny identity, this fixes the half-exponent sign of the discriminant ratio along every prime-to-$`p`$ isogeny. Neither result needs a genus-zero hypothesis.

### Main results

**Theorem 1.1 (supersingular factorial evaluation).** For every prime $`p \ge 5`$,

```math
E_{p+1}^{(p-1)/2} \equiv \left(\frac{6}{p}\right)\left(\frac{p-1}{2}\right)!\,\Delta^{(p^2-1)/24} \pmod{(p, E_{p-1})}.
```

The proof applies an iterated theta operator to $`\eta^{p+1}`$, and Euler's pentagonal identity determines the sign.

**Corollary 1.2 (constancy and Baker's congruence).** The ratio $`c(E) = E_{p+1}(E)^h / \Delta(E)^k`$ takes the single value $`c_p = \left(\frac{6}{p}\right) h!`$ at every supersingular $`E`$. Squaring gives $`c_p^2 = -\left(\frac{-1}{p}\right)`$, which recovers Baker's congruence.

**Theorem 1.3 (signed discriminant ratio).** For every prime $`\ell \ne p`$, at every supersingular point of $`X_0(\ell)`$,

```math
\left(\frac{\Delta(\tau)}{\Delta(\ell\tau)}\right)^{(p^2-1)/24} = \left(\frac{\ell}{p}\right).
```

This determines the half-exponent sign in Ono's supersingular discriminant-ratio identity, and the paper extends it to arbitrary prime-to-$`p`$ isogenies.

### Application: Fricke Hauptmoduln

There are exactly fifteen prime levels $`N`$ for which $`X_0(N)^+`$ has genus zero:
$`N \in \{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 47, 59, 71\}`$.
Let $`T_N = q^{-1} + O(q)`$ be the normalized Hauptmodul and $`p \ge 5`$ a prime with $`p \ne N`$.

**Theorem 1.4 (Fricke residue formula).** The rational function representing $`T_N \mid U_p`$ modulo $`p`$ has poles exactly at the supersingular values $`t_i`$ with effective ramification index $`e_i = 1`$. All poles are simple, and

```math
\mathrm{Res}_{T=t_i} \cdot \prod_{j \ne i} (t_i - t_j)^{(p+1)/e_j} = -\left(\frac{-N}{p}\right),
```

where the product runs over all distinct supersingular values, including ramified ones.

**Corollary 1.5 (reconstruction).** The reduced function vanishes at the cusp and has only simple poles, so the residues determine it. The supersingular values and their indices therefore rebuild the whole reduced $`U_p`$ image without a long $`q`$-expansion.

The ramification indices also describe node thicknesses in the Deligne–Rapoport model of the Fricke quotient.

**Computational evidence.** Exact-arithmetic computations give finite certificates for the factorial evaluation and the discriminant-ratio sign, and for the residue formula at all fifteen levels. The code, per-pair data and benchmarks are in `supplementary/`.

> **Status:** Preprint, not yet peer reviewed. The work was AI-assisted (OpenAI GPT-6.1 Sol and Claude Opus 5.5) in developing arguments, checking calculations and preparing the manuscript. This assistance is not independent specialist refereeing.

**Keywords:** supersingular congruences; Eisenstein series; discriminant ratios; isogenies; Fricke Hauptmoduln; Hecke operators.

## How to cite

Jordan, D. (2026). *A factorial supersingular congruence and signed discriminant ratios: Manuscript, code and data* (Version v1.13) [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.24084789

## Repository layout

| Path | Contents |
|---|---|
| `paper/` | Manuscript source (`.tex`) and compiled PDF, version 1.13 |
| `supplementary/Factorial_Conjecture_Result_v1_0/` | Factorial-evaluation code and recorded results under `new_work/`; reproduce with `new_work/run_all.sh` |
| `supplementary/Eta_Frobenius_Lemma_Audit_v1_0/` | Eta-multiplier and Vélu sign audit: code, results, audit report |
| `supplementary/Signed_Weighted_Residue_v1_0/` | Signed weighted-residue code, per-pair JSON results, proof note (levels 2, 3, 5, 7, 13) |
| `supplementary/Fricke_Elliptic_Values_Fifteen_Levels_v1_0/` | Exact elliptic values and model calculations for all fifteen levels (Table 2) |
| `supplementary/Fricke_Section8_Unified_Certificates_v1_0/` | Reruns the existing exact certification routines at all fifteen prime levels |
| `supplementary/Fricke_Fifteen_Levels_Extension_v1_0/` | Fifteen-level extension of the Fricke residue formula: proof, ten-level verifier, five-level regression, per-pair certificates |
| `supplementary/Theorem_1_3_Benchmark_v1_0/` | Factorial-evaluation benchmark (Theorem 1.1 in v1.13): timing code, exact inputs and outputs, raw timings, verification records |
| `supplementary/Corollary_1_2_Reconstruction_Benchmark_v1_0/` | Reconstruction benchmark (Corollary 1.5 in v1.13): code, results, verification records |

The package names follow the theorem numbering of manuscript v1.11 and are kept unchanged so that the archived manifests and the manuscript's references stay valid. Each package has its own README with reproduction instructions and a SHA-256 manifest. The packages are included exactly as archived, with one exception: three copyrighted third-party papers were removed from `Factorial_Conjecture_Result_v1_0/sources/`. See the `REMOVED_FROM_PUBLIC_REPO.md` file in that folder.

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
