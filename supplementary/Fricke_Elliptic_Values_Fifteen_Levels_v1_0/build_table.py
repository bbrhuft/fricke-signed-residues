import json,sympy as s,pathlib
R=pathlib.Path(__file__).resolve().parent;T=s.symbols('T');records=json.loads((R/'computed.json').read_text())
five={2:[('T+104',4),('T-152',2)],3:[('T+42',6),('T-66',2)],5:[('T+16',2),('T**2-12*T-464',2)],7:[('T+10',2),('T+9',3),('T-18',2)],13:[('T+4',2),('T+3',3),('T**2-4*T-48',2)]}
allrows=[]
for N in [2,3,5,7,11,13,17,19,23,29,31,41,47,59,71]:
 if N in five:factors=five[N]
 else:
  r=next(x for x in records if x['N']==N)
  factors=r['other_factors']+[(text,2) for text,m in r['branch_factors']]
  if N==19:factors=[('T+4',2),('T+3',3),('T**3-4*T**2-16*T-12',2)]
 polys=[s.Poly(s.sympify(text),T) for text,e in factors]
 h=s.prod(p.as_expr() for p in polys);disc=int(s.discriminant(h,T));df=s.factorint(abs(disc))
 assert set(df).issubset({2,3,N})
 assert sum(s.Rational(p.degree())*(1-s.Rational(1,e)) for p,(text,e) in zip(polys,factors))==1+s.Rational(N+1,12)
 allrows.append({'N':N,'factors':factors,'coefficients':[int(c) for c in reversed(s.Poly(h,T).all_coeffs())],'discriminant':str(disc),'discriminant_primes':sorted(df),'discriminant_prime_powers':{str(k):int(v) for k,v in df.items()}})
(R/'all_fifteen.json').write_text(json.dumps(allrows,indent=2))
# Long factor products are set on two lines; higher-degree single factors wrap algebraically.
def factor(text):return s.latex(s.sympify(text)).replace(' ', '')
def grouped(text):
 f=factor(text)
 if text=='T':return 'T'
 return '('+f+')'
lines=[]
for r in allrows:
 N=r['N'];fs=r['factors'];tex=''.join(grouped(text) for text,e in fs)
 if N in [23,47,59,71]:
  tex=r'\begin{aligned}[t]&'+grouped(fs[0][0])+r'\\[-1pt]&{}\cdot'+grouped(fs[1][0])+r'\end{aligned}'
 if N==41:
  tex=r'\begin{aligned}[t]T\bigl(&T^8+4T^7-8T^6-66T^5-120T^4\\[-1pt]&{}-56T^3+53T^2+36T-16\bigr)\end{aligned}'
 indices=',\\ '.join(str(e) for text,e in fs)
 lines.append(f'{N} & ${tex}$ & ${indices}$\\\\[3pt]')
table=r'''\begin{table}[p]\centering\small
\setlength{\tabcolsep}{4pt}
\begin{tabular}{cll}\toprule
$N$ & $h_N(T)$ & Effective indices\\\midrule
'''+ '\n'.join(lines)+r'''
\bottomrule\end{tabular}
\caption{Elliptic-value polynomials at all fifteen prime levels, in the
normalization $T_N=q^{-1}+O(q)$, from \citet[\S4.2, Table~1]{JST19}.
The indices follow the displayed factors; each index applies to every root
of its factor. At admissible primes, the supersingular roots of
$\overline h_N$ are exactly the thick values removed in
\eqref{eq:elliptic-gcd}.}
\label{tab:elliptic-values}
\end{table}
'''
(R/'Table_2_All_Fifteen_Levels.tex').write_text(table)
lemma=r'''\begin{lemma}[elliptic values and specialization]\label{lem:elliptic-specialization}
Let $N\in\mathcal N$ and let
$h_N(T)=\prod_{\tau}(T-T_N(\tau))$, where $\tau$ runs over the
inequivalent elliptic points of $\Gamma_0(N)^+$.
The fifteen polynomials and their effective indices are given in
Table~\ref{tab:elliptic-values}.
For every prime $p\ge5$ with $p\ne N$, the reduction
$\overline h_N$ is squarefree, and its roots in $\Fb$ are exactly the
values with effective index $e>1$. Consequently,
\[
\gcd(\mathcal S_{N,p},\overline h_N)=\prod_{e_i>1}(T-t_i).
\]
\end{lemma}
\begin{proof}
The characteristic-zero polynomials are those of
\citet[\S4.2, Table~1]{JST19}, with $T_N=q^{-1}+O(q)$.
Their elliptic orders give the effective indices of
Lemma~\ref{lem:inertia}. For $N\in\mathcal N_0$, the Fricke fixed values
are given by $u_N^2=b_N$. At the remaining levels, the smooth models
$v^2=f_N(u)$ of Section~\ref{sec:comp} have involution
$(u,v)\mapsto(u,-v)$ and coordinate $T_N=u-s_N$;
the branch values are the roots of $f_N(T+s_N)$, all of index two.
The additional factors are $T+2$ of index two at $N=17,29$,
$T$ of index two at $N=41$, $T+3$ of index three at $N=19$,
and $T$ of index three at $N=31$. These are obtained from the
elliptic fibres over $j=1728$ and $j=0$.

We justify specialization of the support. An effective stabilizer arises
from an automorphism of $(E,C)$ or a Fricke fixed point. For $p\ge5$,
nontrivial reduced automorphisms occur only at $j=0,1728$; their
prime-to-$p$ automorphisms lift with the corresponding CM elliptic curve,
and an invariant prime-to-$p$ cyclic subgroup lifts uniquely over a
strict henselian base. Conversely, these automorphisms persist on reduction.
The displayed Fricke branch equations give finite \'etale fixed-point
loci away from $6N$: this follows directly from their discriminants.
Thus the listed elliptic values specialize to precisely the values with
$e>1$.

Exact discriminant calculation for every displayed $h_N$ gives
\[
\operatorname{Disc}(h_N)=\pm2^{a_N}3^{b_N}N^{c_N}
\qquad(a_N,b_N,c_N\ge0).
\]
The exact values and model calculations are supplied in
\path{Fricke_Elliptic_Values_Fifteen_Levels_v1_0}.
Hence distinct elliptic values cannot collide at any admissible prime,
so $\overline h_N$ is squarefree. Intersecting its root set with the
supersingular locus proves the gcd formula.
\end{proof}
'''
# Avoid overloading the global eta-coordinate a_N,b_N: discriminant exponents use lambda,mu,nu.
lemma=lemma.replace('2^{a_N}3^{b_N}N^{c_N}', '2^{\\lambda_N}3^{\\mu_N}N^{\\nu_N}').replace('(a_N,b_N,c_N\\ge0)', '(\\lambda_N,\\mu_N,\\nu_N\\ge0)')
(R/'Lemma_and_Table_2_All_Fifteen_Levels.tex').write_text(lemma+'\n'+table)
src=(R/'input/Fricke_Signed_Residues_Journal_v1_10.tex').read_text();start=src.index(r'\begin{lemma}[elliptic values and specialization]');stop=src.index(r'\end{table}',start)+len(r'\end{table}')
(R/'validation_manuscript.tex').write_text(src[:start]+lemma+'\n'+table+src[stop:])
print('Built fifteen-level table, replacement lemma, discriminants and signature checks')
