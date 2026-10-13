"""Exact finite certificates for numerical Hoggatt row sums; standard library."""
from fractions import Fraction as Q
from itertools import permutations
from math import comb, prod
import json
import traceback

if not __debug__:
    raise RuntimeError('Assertions must remain enabled; do not use Python -O.')
def original(d, n, k):
    return prod((Q(comb(n+j, k), comb(k+j, k)) for j in range(d)), start=Q(1))
def rectangle(d, n, k):
    return prod((Q(d+i+j-1, i+j-1) for i in range(1, k+1) for j in range(1, n-k+1)), start=Q(1))
def rows(d, upto):
    r = [sum((original(d,n,k) for k in range(n+1)), Q(0)) for n in range(upto+1)]
    assert all(x.denominator == 1 for x in r)
    return [int(x) for x in r]
def det_permutation(a):
    n = len(a)
    return sum((-1 if sum(p[i] > p[j] for i in range(n) for j in range(i+1,n)) % 2 else 1) * prod(a[i][p[i]] for i in range(n)) for p in permutations(range(n)))
def det_elimination(a):
    a = [list(map(Q,row)) for row in a]
    result = Q(1)
    for k in range(len(a)):
        p = next((i for i in range(k,len(a)) if a[i][k]), None)
        if p is None:
            return Q(0)
        if p != k:
            a[p],a[k] = a[k],a[p]
            result = -result
        pivot = a[k][k]
        result *= pivot
        for i in range(k+1,len(a)):
            factor = a[i][k]/pivot
            for j in range(k,len(a)):
                a[i][j] -= factor*a[k][j]
    return result
def hankel(r,m):
    return [[r[i+j+1] for j in range(m)] for i in range(m)]

result = {'arithmetic':'Python standard-library arbitrary integers and Fraction; no floating arithmetic in certificates'}
try:
    checks = 0
    for d in range(21):
        for n in range(12):
            for k in range(n+1):
                assert original(d,n,k) == rectangle(d,n,k)
                checks += 1
    result['product_crosschecks'] = checks
    result['product_crosscheck_domain'] = '0<=d<=20, 0<=n<=11, 0<=k<=n (checks accompany, do not replace the general derivation)'
    degree = [{'permutation':list(p),'degree_bound':sum((i+p[i]+1)**2//4 for i in range(4))} for p in permutations(range(4))]
    assert max(x['degree_bound'] for x in degree) == 20
    result['all_degree_bounds'] = degree
    pc = [-1080,-10068,-3490,-1235,-5602,-2605,-214,83,18,1]
    shifted = [sum(pc[j]*comb(j,k)*5**(j-k) for j in range(k,10)) for k in range(10)]
    assert shifted == [190080,8752032,10009560,4978600,1393398,239300,25791,1703,63,1]
    assert all(v>0 for v in shifted)
    result['P_coefficients_ascending'] = pc
    result['P_t_plus_5_coefficients_ascending'] = shifted
    nodes = []
    for d in range(21):
        r = rows(d,7)
        a = hankel(r,4)
        actual = det_permutation(a)
        second = det_elimination(a)
        proposed = Q(-d**4*(d-1)**3*(d+1)**3*(d+2)*sum(c*d**j for j,c in enumerate(pc)),74649600)
        assert actual == second == proposed
        nodes.append({'d':d,'rows_n0_to_n7':r,'det_permutation':actual,'det_elimination':str(second),'factored_value':str(proposed),'equal':True})
    result['identity_nodes'] = nodes
    witnesses = []
    for d,m,expected in [(3,6,-115894592),(4,5,-2220868988),(5,4,-154000)]:
        r = rows(d,2*m-1)
        a = hankel(r,m)
        first,second = det_permutation(a),det_elimination(a)
        assert first == second == expected
        witnesses.append({'d':d,'order':m,'shift':1,'rows':r,'matrix':a,'determinant':first,'second_determinant':str(second)})
    a = witnesses[-1]['matrix']
    assert a == [[2,8,44,310],[8,44,310,2606],[44,310,2606,25202],[310,2606,25202,272582]]
    v = [-17017,11284,-1877,85]
    av = [sum(a[i][j]*v[j] for j in range(4)) for i in range(4)]
    q = sum(v[i]*av[i] for i in range(4))
    assert q == -327250
    result['negative_witnesses'] = witnesses
    result['quadratic_form'] = {'vector':v,'matrix_times_vector':av,'value':q}
    result['positive_case_spotchecks'] = []
    for n in range(12):
        s1,s2 = rows(1,n)[-1],rows(2,n)[-1]
        assert s1 == 2**n and s2 == Q(comb(2*n+2,n+1),n+2)
        result['positive_case_spotchecks'].append({'n':n,'S1':s1,'S2':s2})
    result['status'] = 'PASS'
except BaseException:
    result['status'] = 'FAIL'
    result['traceback'] = traceback.format_exc()
    raise
finally:
    print(json.dumps(result,indent=2))
