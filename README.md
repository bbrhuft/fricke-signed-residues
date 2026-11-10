# Supersingular poles and signed residues of prime-level Fricke Hauptmoduln

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24120142.svg)](https://doi.org/10.5281/zenodo.24120142)

**David Jordan** · Maynooth University Social Sciences Institute (MUSSI), Maynooth University · Manuscript v2.0, 9 November 2026

> **Version history.** Up to v1.11 this repository held a single paper under the present title. In v1.13 it was retitled *A factorial supersingular congruence and signed discriminant ratios* and refocused on the factorial congruence. From v2.0 the work is split into two papers: this repository holds the Fricke residue paper under its original title, and the factorial congruence paper, with its three supplementary packages, has moved to [bbrhuft/factorial-supersingular-congruence](https://github.com/bbrhuft/factorial-supersingular-congruence). The earlier combined versions remain archived on Zenodo: v1.11 ([10.5281/zenodo.24024359](https://doi.org/10.5281/zenodo.24024359)) and v1.13 ([10.5281/zenodo.24084789](https://doi.org/10.5281/zenodo.24084789)).

## About the paper

There are exactly fifteen prime levels $`N`$ for which $`X_0(N)^+`$ has genus zero:
$`N \in \{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 47, 59, 71\}`$.
Let $`T_N = q^{-1} + O(q)`$ be the normalized Hauptmodul and $`p \ge 5`$ a prime with $`p \ne N`$. The paper determines the poles and signed residues of the rational function representing $`T_N \mid U_p`$ modulo $`p`$.

### Main results

**Theorem 1.1 (supersingular inputs).** The sign in the residue formula rests on two identities: Baker's supersingular congruence and the signed discriminant-ratio identity

```math
\left(\frac{\Delta(\tau)}{\Delta(N\tau)}\right)^{(p^2-1)/24} = \left(\frac{N}{p}\right)
```

at every supersingular point of $`X_0(N)`$, proved in the companion paper.

**Theorem 1.2 (Fricke residue formula).** The rational function representing $`T_N \mid U_p`$ modulo $`p`$ has poles exactly at the supersingular values $`t_i`$ with effective ramification index $`e_i = 1`$. All poles are simple, and

```math
\mathrm{Res}_{T=t_i} \cdot \prod_{j \ne i} (t_i - t_j)^{(p+1)/e_j} = -\left(\frac{-N}{p}\right),
```

where the product runs over all distinct supersingular values, including ramified ones.

**Corollary 1.3 (reconstruction).** The reduced function vanishes at the cusp and has only simple poles, so the residues determine it. The supersingular values and their indices therefore rebuild the whole reduced $`U_p`$ image without a long $`q`$-expansion.

**Corollary 1.4 (level two).** For the Monster function $`T_{2A}`$, $`T_{2A} \mid U_p \equiv 0 \pmod p`$ if and only if $`p = 5`$ or $`7`$.

The ramification indices also describe node thicknesses in the Deligne–Rapoport model of the Fricke quotient.

**Computational evidence.** Exact-arithmetic computations give finite certificates for the residue formula at all fifteen levels. The code, per-pair data and benchmarks are in `supplementary/`.

> **Status:** Preprint, not yet peer reviewed. The work was AI-assisted (OpenAI GPT-6.1 Sol and Claude Opus 5.5) in developing arguments, checking calculations and preparing the manuscript.

**Keywords:** supersingular elliptic curves; Fricke groups; Hauptmoduln; Hecke operators; eta quotients; congruences.

## How to cite

Jordan, D. (2026). *Supersingular poles and signed residues of prime-level Fricke Hauptmoduln: Manuscript, code and data* (Version v2.0) [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.24120142

## Repository layout

| Path | Contents |
|---|---|
| `paper/` | Manuscript source (`.tex`) and compiled PDF, version 2.0 |
| `supplementary/Signed_Weighted_Residue_v1_0/` | Signed weighted-residue code, per-pair JSON results, proof note (levels 2, 3, 5, 7, 13) |
| `supplementary/Fricke_Fifteen_Levels_Extension_v1_0/` | Fifteen-level extension of the residue formula: proof, ten-level verifier, five-level regression, per-pair certificates |
| `supplementary/Fricke_Section8_Unified_Certificates_v1_0/` | Records and reproduction script for the certified reconstructions at all fifteen levels (Table 3) |
| `supplementary/Fricke_Elliptic_Values_Fifteen_Levels_v1_0/` | Exact elliptic values and model calculations for all fifteen levels (Table 2) |
| `supplementary/Corollary_1_2_Reconstruction_Benchmark_v1_0/` | Reconstruction benchmark for Corollary 1.3 (numbered Corollary 1.2 in an earlier draft): code, results, verification records |

The package names follow the theorem numbering of earlier manuscript versions and are kept unchanged so that the archived manifests stay valid. Each package has its own README with reproduction instructions and a SHA-256 manifest.

## Software environment

All computations use exact arithmetic. Tested with Python 3.13 on Linux x86_64.

- `python-flint` 0.9.0
- `mpmath` 1.3.0
- A C compiler for the optional native kernels in the benchmark package

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
