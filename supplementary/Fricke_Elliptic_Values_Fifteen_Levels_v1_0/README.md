# Table 2: all fifteen prime Fricke genus-zero levels

This is a drop-in extension of Table 2 (elliptic-value polynomials and effective indices), based on Fricke_Signed_Residues_Journal_v1_10.tex. It is distinct from the Section 8 computational-certificates table.

## Installation

Recommended: replace the complete block beginning `\begin{lemma}[elliptic values and specialization]` and ending at the end of its following table with `Lemma_and_Table_2_All_Fifteen_Levels.tex`. This extends the lemma from the five eta-quotient levels to all fifteen levels as well as extending the table. The original labels are retained.

For the table alone, use `Table_2_All_Fifteen_Levels.tex` in place of the existing table. That change alone leaves the adjoining lemma restricted to the original five levels.

Do not insert both fragments. The table uses the manuscript's existing amsmath, booktabs and natbib packages and JST19 bibliography entry. It occupies one page in the validation build. No supplied manuscript or historical evidence was overwritten; input/ contains the unchanged v1.10 used for validation. These fragments do not disturb the user's separate Proposition 3.4 edits or Section 8 replacement.

## Provenance and status

The characteristic-zero polynomials are published in Jorgenson, Smajlović and Then (2019), Section 4.2, Table 1 (the existing JST19 reference). They are not claimed as new. The published table was checked in https://research-information.bris.ac.uk/files/141315762/jst4journal_may31.pdf . Its coordinate has the same q^(-1)+O(q) normalization.

The ten additional rows were also reconstructed exactly from the inherited hyperelliptic modular models. If u=T+s_N and w_N(u,v)=(u,-v), the branch factor is f_N(T+s_N), with effective index two. Additional automorphism factors arise over j=0 or 1728. They are T+2 at N=17,29 and T at N=41 (index two), and T+3 at N=19 and T at N=31 (index three).

The mathematical specialization argument is included in the replacement lemma. Exact computation verifies the full discriminant of every h_N is supported on {2,3,N}, and the factor degrees and indices satisfy the genus-zero signature formula. These are exact polynomial identities, not an inference from a finite search.

Fresh finite-field verification checked every admissible pair with 5<=p<=211: 662 pairs across all fifteen levels. It reconstructs supersingular j-values by the Deuring polynomial, uses the inherited modular models to compute effective indices, and compares them with the table. All passed. These are checks of elliptic support and indices, NOT new q-expansion or signed-residue certificates; inherited Section 8 evidence is unchanged. Finite checks support, but do not replace, the specialization proof.

## Reproduce

Python 3, sympy 1.14.0 and python-flint 0.9.0 were used.

    python compute.py
    python build_table.py
    python check_reductions.py

computed.json contains the ten model derivations. all_fifteen.json contains factor expressions, indices, coefficients (ascending order), and exact discriminants for all fifteen rows. reduction_checks.json and checks.log record the bounded finite-field checks. build_table.py also creates an internal validation manuscript from the unchanged input; that full manuscript is not intended to replace the user's current copy.

The three files under inherited/ were copied byte-for-byte from Fricke_Fifteen_Levels_Extension_v1_0/code. Their scope and limitations remain inherited. SHA256SUMS.json records included input and result hashes. No files from previous evidence bundles were edited.
