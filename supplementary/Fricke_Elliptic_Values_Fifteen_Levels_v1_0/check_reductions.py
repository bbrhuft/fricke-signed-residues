"""Exact polynomial/geometry checks; these are not new U_p certificates."""
import json,pathlib,sys,sympy as s
from flint import fmpz_poly
ROOT=pathlib.Path(__file__).resolve().parent
CODE=ROOT/'inherited'
sys.path.insert(0,str(CODE))
import inherited_wr_core as c
from verify_extension import DATA
records=json.loads((ROOT/'all_fifteen.json').read_text());byN={r['N']:r for r in records}
counts=[]
for N in [2,3,5,7,11,13,17,19,23,29,31,41,47,59,71]:
 r=byN[N];pcount=0
 T=s.symbols('T');spec=[(s.Poly(s.sympify(text),T),e) for text,e in r['factors']]
 if str(N) in DATA:d=DATA[str(N)]
 for p in c.primes_upto(211):
  if p<5 or p==N:continue
  F=c.Field(p);js,_=c.ss_j_deuring(F)
  h=F.poly_from_ints(r['coefficients']);assert h.gcd(h.derivative()).degree()==0
  if N in [2,3,5,7,13]:
   for point in c.ss_points(N,F,js):
    t=point['t'];expected=1
    for poly,e in spec:
     if F.poly_from_ints([int(x) for x in reversed(poly.all_coeffs())])(t)==0:expected=e
    assert point['e']==expected,(N,p,t,point['e'],expected)
   pcount+=1
   continue
  alpha=F.poly_from_ints(d['alpha']);Q=F.poly_from_ints(d['Q']);ff=F.poly_from_ints(d['hyper_poly'])
  points={}
  for j in js.values():
   H=Q-j*alpha+j*j;roots=H.roots();assert sum(mu for u,mu in roots)==N+1
   for u,mu in roots:
    branch=ff(u)==0;aut=3 if j==F.el(0) else 2 if j==F.el(1728) else 1
    both=alpha(u)==2*j;num=aut*(2 if both and not branch else 1)
    if aut==1:idx=2 if branch else 1
    else:
     assert num%mu==0;idx=(num//mu)*(2 if branch else 1)
    t=u-F.el(d['shift']);assert (h(t)==0)==(idx>1),(N,p,t,idx)
    expected=2 if branch else 1
    for poly,e in spec:
     if F.poly_from_ints([int(x) for x in reversed(poly.all_coeffs())])(t)==0:expected=e
    assert idx==expected,(N,p,t,idx,expected)
    key=F.key(t)
    if key in points:assert points[key]==idx
    points[key]=idx
  pcount+=1
 counts.append({'N':N,'primes_checked':pcount});print(N,pcount,'PASS',flush=True)
(ROOT/'reduction_checks.json').write_text(json.dumps({'status':'PASS','scope':'All fifteen levels, all admissible 5<=p<=211; independent smooth-model inertia vs char-zero polynomial roots and indices, not q-series certification','counts':counts,'pairs':sum(x['primes_checked'] for x in counts)},indent=2))
