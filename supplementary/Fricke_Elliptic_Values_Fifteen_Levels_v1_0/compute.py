import sympy as s,json,pathlib
u,T=s.symbols('u T');ROOT=pathlib.Path(__file__).resolve().parent
DATA=json.loads((ROOT/'inherited/hyperelliptic_data.json').read_text());out=[]
def poly(a):return s.Poly(sum(v*u**i for i,v in enumerate(a)),u)
for N0,d in DATA.items():
 N=int(N0);f=poly(d['hyper_poly']);alpha=poly(d['alpha']);Q=poly(d['Q']);special=[]
 for j,aut,condition in [(0,3,N%3==1),(1728,2,N%4==1)]:
  common=s.gcd(Q-j*alpha+j*j,alpha-2*j).sqf_part()
  factors=s.factor_list(common)[1]
  for factor,m in factors:
   if s.rem(f,factor).is_zero:continue
   mu=0;test=Q-j*alpha+j*j
   while s.rem(test,factor).is_zero:
    mu+=1;test=s.exquo(test,factor)
   if 2*aut//mu>1:special.append((factor,2*aut//mu))
  assert bool(special and any(e==aut for p,e in special))==condition or not condition
 fT=s.Poly(f.as_expr().subs(u,T+d['shift']),T)
 fac=[(s.Poly(p.as_expr().subs(u,T+d['shift']),T),e) for p,e in special]
 h=fT
 for p,e in fac:h*=p
 disc=int(s.discriminant(h.as_expr(),T))
 out.append({'N':N,'branch_polynomial':str(fT.as_expr()),'branch_factors':[(str(p.as_expr()),m) for p,m in s.factor_list(fT)[1]],'other_factors':[(str(p.as_expr()),e) for p,e in fac],'h_coefficients':[int(x) for x in reversed(h.all_coeffs())],'discriminant_factorisation':str(s.factorint(disc))})
 print(N,'branch',s.factor(fT.as_expr()),'extras',[(p.as_expr(),e) for p,e in fac],'disc',s.factorint(disc),flush=True)
(ROOT/'computed.json').write_text(json.dumps(out,indent=2))
