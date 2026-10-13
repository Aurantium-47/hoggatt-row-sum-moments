# Stieltjes moment classification of numerical Hoggatt row sums

Aurantium · v0.1.0 · 14 October 2026

For each positive integer d, define H_d(n,k) by the standard Hoggatt product and S_d(n) as its row sum, with n starting at zero. This note gives the numerical classification: (S_d(n)) is a Stieltjes moment sequence exactly when d is 1 or 2.

- [Complete manuscript](paper/proof.pdf) and [standalone LaTeX](paper/proof.tex)
- [Exact finite certificate](data/exact_certificate.json)
- [Minimal standard-library reproduction](code/verify_certificate.py) and [execution scope](REPRODUCIBILITY.md)
- [References](REFERENCES.md) and [rights](RIGHTS.md)

The proof includes the two positive measures, shifted-Hankel obstructions for d=3 and 4, the rectangular product identity, the degree bound for a uniform determinant, all 21 exact interpolation nodes and the strict sign argument for every d>=5. The data record contains the full matrices and two exact determinant evaluations. This is a statement about numerical row sums, not coefficientwise q-moment properties.

The saved certificate records an earlier successful exact-arithmetic run. The stdout-only packaged entry also completed one local replay with Python 3.12.10 on 14 October 2026: all exact checks passed, its output JSON matched the archived certificate, child/guard/shell exited 0 and stderr was empty. External wall time was 0.125 seconds and peak child working set was 13,705,216 bytes. No original author full suite is claimed to have been rerun; see REPRODUCIBILITY.md for the separate statuses.

Fang–Zhang–Zhao explicitly state non-Stieltjesness for positively indexed Baxter numbers. Here S_3(n)=B_(n+1), so their prior assertion is relevant. The exact alignment of their negative fifth-order Hankel hint with this normalized sequence has not been established, and the final journal text was not checked. This note supplies explicit normalized certificates and makes no first-discovery or worldwide-priority claim for the classification or its determinant formula.

Prepared with AI assistance. This research note has no assigned journal venue and claims no independent human peer-review or proof-assistant certification. Third-party papers are linked, not redistributed. WHITELIST.txt lists the complete payload, and MANIFEST.json gives hashes except for its own file.
