# Supersingular poles and signed residues of prime-level Fricke Hauptmoduln

**David Jordan** · Maynooth University Social Sciences Institute (MUSSI), Maynooth University · Manuscript v1.11, 6 November 2026

## About the paper

There are exactly fifteen prime levels $`N`$ for which the Fricke curve $`X_0(N)^+`$ has genus zero:
$`N \in \{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 47, 59, 71\}`$.
For each of these, let $`T_N = q^{-1} + O(q)`$ be the normalized Hauptmodul for $`\Gamma_0(N)^+`$.
For every prime $`p \ge 5`$ with $`p \nmid N`$, the paper determines the poles and residues of the rational function that represents $`T_N \mid U_p`$ modulo $`p`$.

### Main results

**Poles.** The poles are exactly the supersingular values $`t_i`$ with effective ramification index $`e_i = 1`$. All poles are simple.

**Signed residues.** For each such pole,

```math
\mathrm{Res}_{T=t_i} \cdot \prod_{j \ne i} (t_i - t_j)^{(p+1)/e_j} = -\left(\frac{-N}{p}\right),
```

where the product runs over all distinct supersingular values, including ramified ones.

**Reconstruction.** The reduced function vanishes at the cusp and has only simple poles, so its residues determine it completely. The formula therefore rebuilds the reduced $`U_p`$ image from the weighted supersingular values, without a long $`q`$-expansion.

**Factorial evaluation.** On the supersingular locus,

```math
E_{p+1}^{(p-1)/2} = \left(\frac{6}{p}\right)\left(\frac{p-1}{2}\right)!\,\Delta^{(p^2-1)/24}.
```

The proof applies an iterated theta operator to $`\eta^{p+1}`$ at full level twelve. The evaluation recovers Baker's supersingular congruence.

**Discriminant-ratio sign.** Combining the factorial evaluation with Robert's isogeny identity gives

```math
\left(\frac{\Delta(\tau)}{\Delta(\ell\tau)}\right)^{(p^2-1)/24} = \left(\frac{\ell}{p}\right)
```

at every supersingular point of $`X_0(\ell)`$, for every prime $`\ell \ne p`$. This determines the sign left open in Ono's half-exponent examples, and it needs no genus-zero hypothesis.

The proof combines a Kaneko–Zagier derivative argument with the factorial evaluation. The ramification indices also have a geometric interpretation as node thicknesses in the Deligne–Rapoport model of the Fricke quotient.

**Computational evidence.** Exact-arithmetic computations give finite certificates for the five eta-coordinate levels ($`N = 2, 3, 5, 7, 13`$) with $`p \le 211`$, and for the ten other levels with $`p \le 47`$. The code, per-pair data and benchmarks are in `supplementary/`.

> **Status:** Preprint, not yet peer reviewed. The work was AI-assisted (OpenAI GPT-6.1 Sol and Claude Opus 5.5) in developing arguments, checking calculations and preparing the manuscript. This assistance is not independent specialist refereeing.

**Keywords:** supersingular elliptic curves; Fricke groups; Hauptmoduln; Hecke operators; eta quotients; congruences.

**Keywords:** supersingular elliptic curves; Fricke groups; Hauptmoduln; Hecke operators; eta quotients; congruences.
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
| `supplementary/Fricke_Section8_Unified_Certificates_v1_0/` | Reruns the existing exact certification routines at all fifteen prime levels |
| `supplementary/Fricke_Fifteen_Levels_Extension_v1_0/` | Fifteen-level extension: proof that Theorem 1.1 holds at all fifteen genus-zero prime levels, ten-level verifier, five-level regression, per-pair certificates |
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
