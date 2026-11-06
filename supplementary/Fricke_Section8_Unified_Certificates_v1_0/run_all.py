"""Uniform full-certificate rerun at all fifteen levels, p<=47."""
import sys,json,pathlib,time
ROOT=pathlib.Path(__file__).resolve().parent
CODE=ROOT/'inherited/Fricke_Fifteen_Levels_Extension_v1_0/code'
sys.path.insert(0,str(CODE))
import inherited_wr_core as core
sys.modules['wr_core']=core
from inherited_wr_pairs import compute_pair
from verify_extension import run
LEVELS=[2,3,5,7,11,13,17,19,23,29,31,41,47,59,71]
rows=[];raw=[]
for N in LEVELS:
 for p in core.primes_upto(47):
  if p<5 or p==N:continue
  if N in [2,3,5,7,13]:
   r=compute_pair(N,p,mode='certified',kz=True,hasse_power=True)
   assert r['certificate_ok'] and r['mass_ok']
   # The inherited routine records some checks rather than asserting all.
   for key,val in r.items():
    if isinstance(val,bool):assert val,(N,p,key)
   row={'N':N,'p':p,'thin':r['n_thin'],'nonrational_thin':r['n_thin_nonrational'],'certificate':True,'source':'eta-coordinate verifier'}
  else:
   r=run(N,p)
   assert all(r[k] for k in ['certificate','geometric_weights','weighted_polynomial','signed_residues'])
   row={'N':N,'p':p,'thin':r['n_thin'],'nonrational_thin':r['n_nonrational_thin'],'certificate':True,'source':'elliptic/hyperelliptic verifier'}
  raw.append(r);rows.append(row)
  (ROOT/'unified_results.json').write_text(json.dumps(rows,indent=2))
  (ROOT/'raw_results.json').write_text(json.dumps(raw,indent=2,default=str))
  print(N,p,'PASS',row['thin'],flush=True)
print('PASS',len(rows),'pairs',sum(r['thin'] for r in rows),'thin',sum(r['nonrational_thin'] for r in rows),'nonrational',flush=True)
