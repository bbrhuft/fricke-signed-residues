from pathlib import Path
import json
ROOT=Path(__file__).resolve().parent
source=ROOT/'input/Fricke_Signed_Residues_Journal_v1_10.tex'
s=source.read_text();start=s.index(r'\section{Finite certificates');end=s.index(r'\subsection{Computational consequences and timings}',start)
old=s[start:end]
prop=old[old.index(r'\begin{proposition}'):old.index(r'\end{proof}')+len(r'\end{proof}')]
rows=json.loads((ROOT/'unified_results.json').read_text());levels=[2,3,5,7,11,13,17,19,23,29,31,41,47,59,71]
assert len(rows)==184 and all(r['certificate'] for r in rows)
counts=[]
for N in levels:
 a=[r for r in rows if r['N']==N]
 counts.append({'N':N,'pairs':len(a),'thin':sum(r['thin'] for r in a),'nonrational':sum(r['nonrational_thin'] for r in a)})
total={key:sum(x[key] for x in counts) for key in ['pairs','thin','nonrational']}
assert total=={'pairs':184,'thin':4458,'nonrational':3448}
# Compare all fresh numerator/denominator certificates with the inherited data.
base=ROOT/'inherited/Fricke_Fifteen_Levels_Extension_v1_0/results'
previous=json.loads((base/'five_level_regression_p47.json').read_text())+json.loads((base/'new_levels_p47.json').read_text())
raw=json.loads((ROOT/'raw_results.json').read_text());lookup={(x['N'],x['p']):x for x in previous}
for r in raw:
 p=lookup[r['N'],r['p']]
 if r['N'] in [2,3,5,7,13]:assert r['R_numerator']==p['R_numerator'] and r['D_thin']==p['D_thin']
 else:assert r['numerator']==p['numerator'] and r['denominator']==p['denominator']
lines='\n'.join(f"{x['N']}&{x['pairs']}&{x['thin']}&{x['nonrational']}\\\\" for x in counts)
new=r'''\section{Finite certificates and computational evidence}\label{sec:comp}
A unified exact-arithmetic rerun covers all fifteen levels in $\mathcal N$
for $5\le p\le47$, excluding $p=N$. The computations reconstruct
$R_{N,p}$ independently of the signed residue formula and then verify
that formula. They are checks on the theorems, not inputs to their proofs.
The following bound specifies the strength of the certificates.

'''+prop+r'''

For each pair, the supersingular values and effective indices are determined
from the modular model, giving $D_{\rm thin}$. A separate $q$-expansion
calculation recovers the numerator without using the residue signs and
checks Proposition~\ref{prop:certificate}, using source precision at least
$p^3+2$. The reduced fraction, mass identity, weighted supersingular
polynomial and signed residue products are also checked.

At $N\in\mathcal N_0$, the inputs are the eta coordinate and its rational
$j$-map. At the other ten levels, we use the standard smooth elliptic or
hyperelliptic models $v^2=f_N(u)$ with $w_N(u,v)=(u,-v)$ and relations
\[
j+j\circ w_N=\alpha_N(u),\qquad
j(j\circ w_N)=Q_N(u),
\]
\[
j=\frac{\alpha_N(u)+\beta_N(u)v}{2},
\quad Q_N=\frac{\alpha_N^2-f_N\beta_N^2}{4}.
\]
These are the model data used by SageMath's prime-isogeny routines
\citep{SageModels}. The coordinate is $T_N=u-s_N$, where
$s_N=-[u^{N-1}]\alpha_N/N$. Formal Newton inversion of
$\alpha_N(u(q))=j(q)+j(q^N)$ gives its expansion, with the product relation
checked separately. Supersingular fibres satisfy
$j_0^2-j_0\alpha_N(u)+Q_N(u)=0$; the roots of $f_N$ detect Fricke
ramification, and fibre multiplicities over $j_0=0,1728$ give the reduced
automorphism orders. Thus the indices are obtained independently of both
the signed residue formula and the weighted Hasse polynomial.

All 184 admissible pairs pass the finite certificate. They contain
4458 thin values, of which 3448 lie outside $\Fp$
(Table~\ref{tab:all-levels}). The freshly reconstructed numerators and
denominators also agree exactly with the corresponding archived certificates.
At every thin value the weighted residue product is
$-\left(\frac{-N}{p}\right)$; pairs with no thin values have an empty
residue-product set.

\begin{table}[htbp]\centering\small
\begin{tabular}{rrrr}\toprule
$N$ & certified pairs & thin values & outside $\Fp$\\\midrule
TABLE_ROWS
\midrule
Total&184&4458&3448\\\bottomrule
\end{tabular}
\caption{Unified certified reconstructions at all fifteen levels for
$5\le p\le47$, $p\ne N$. Values are distinct geometric $T_N$-values
within each pair $(N,p)$; counts are summed over the tested primes.}
\label{tab:all-levels}\label{tab:n0-levels}\label{tab:new-levels}
\end{table}

The broader archived tests remain supplementary evidence. At the original
five levels, all 222 admissible pairs through $p=211$ are certified
(6246 thin values, 4696 outside $\Fp$); candidate-free denominator recovery
was checked through $p=37$, and Hecke polynomials modulo $p^2$ through
$p=31$. A further 960 pairs for $223\le p\le1499$ were checked using the
double-pole formula of Lemma~\ref{lem:g}; these are not independent
reconstructions from $T|U_p$.

The eta/Frobenius identity was tested independently using normalized
V\'elu quotients and discriminants, without eta functions or Hauptmoduln.
For the 15 primes $\ell\le47$ and admissible $5\le p\le199$, all 647 pairs
and 127541 cyclic-kernel checks gave the asserted discriminant-ratio sign.
These count kernels on chosen supersingular representatives, not distinct
coarse points, since automorphisms can identify kernels at $j=0,1728$.

For Theorem~\ref{thm:factorial}, exact polynomial remainders and evaluations
at all 6430 supersingular $j$-values for the 166 primes $5\le p\le997$
(4734 outside $\Fp$) agree with the asserted constant. Evaluations use three
randomly rescaled models per value, with additional Legendre and Weierstrass
coefficient routes. Negating the constant fails at every tested prime.
The two theta identities in the proof were also checked in
$\Fp[E_4,E_6]$ at $p=23,47,71,167$, where $\eta^{p+1}$ has level one.
The fresh all-level records and reproduction script are supplied in
\path{Fricke_Section8_Unified_Certificates_v1_0}; historical evidence
packages are retained unchanged.

'''.replace('TABLE_ROWS',lines)
(ROOT/'Section_8_Certificates_Replacement.tex').write_text('% Replace Section 8 from its heading up to, but not including,\n% \\subsection{Computational consequences and timings}.\n% Keep that subsection and the existing Data and software paragraph.\n'+new)
(ROOT/'validation_manuscript.tex').write_text(s[:start]+new+s[end:])
(ROOT/'counts.json').write_text(json.dumps({'levels':counts,'total':total,'all_certificates_pass':True,'historical_fraction_matches':len(raw)},indent=2))
print('PASS',total,'historical fractions matched:',len(raw),'word counts before/after:',len(old.split()),len(new.split()))
