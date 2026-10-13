# Exact certificate reproduction

The arithmetic uses only Python's standard library: arbitrary integers, `fractions.Fraction`, finite products and permutations. Use the installed Python 3.12 interpreter with assertions enabled:

```sh
python -I -B code/verify_certificate.py
```

The program is independent of the current working directory. It reads no manuscript, external paper or certificate file and writes no file; its complete result is JSON on stdout. If preserving a new run, redirect stdout to a new file outside this package and retain stderr separately. Do not use Python's `-O` option.

The minimal entry reconstructs exactly these finite objects:

- 1,638 product/rectangle comparisons on 0<=d<=20, 0<=n<=11 and 0<=k<=n.
- All 24 permutation degree bounds for the four-by-four determinant.
- All 21 exact identity nodes d=0,...,20, with row prefixes and both a signed-permutation determinant and rational Gaussian elimination.
- The full d=3/order6, d=4/order5 and d=5/order4 shifted matrices, their negative determinants and the d=5 quadratic-form witness.
- The ten coefficients of P(t+5), and finite consistency checks for the two positive row-sum formulas.

The printed proof supplies the general rectangular-product identity, the degree argument converting the 21 exact equalities into an identity, the sign proof and the positive measures. A successful finite run does not replace these arguments. The two determinant implementations are distinct arithmetic routes in this same program, not a claim of independent human or formal verification.

## Execution records

The original implementation ran successfully on 13 October 2026 at 09:04:24 UTC. Its saved receipt records exit0, 0.141 seconds external wall time, 5,840,896 bytes peak process commit and 7,122,944 bytes peak job commit under a 128-MiB process/job commit limit and a 60-second wall limit. The saved receipt did not record an interpreter version or physical working-set/RSS measurement; neither is inferred retrospectively. These are historical observations, not performance predictions.

`verification/original_execution.json` is a path-free summary of that execution. `data/exact_certificate.json` retains the original successful certificate bytes. The packaged program retains all six arithmetic functions and the complete arithmetic block; only the output location, explanatory header and assertion-mode guard were adapted. The stdout-only adaptation completed one local replay on 14 October 2026 with Python 3.12.10. Its JSON output was structurally identical to the archived certificate, including all 21 nodes, 24 degree bounds, three negative matrices and 1,638 product comparisons. Child, guard and shell exited 0; stderr was empty. External wall time was 0.125 seconds, peak child working set 13,705,216 bytes, peak process commit 8,409,088 bytes and peak job commit 9,670,656 bytes.

The suspended child was assigned to a single-process Windows Job before execution. The limits were 128 MiB for process/job commit and sampled peak working set, 60 seconds wall time, 256 MiB available at startup and termination at the first sample below 128 MiB available. Actual available memory was 562,466,816 bytes at startup and at least 552,583,168 bytes during monitoring; no limit was triggered. These measurements describe this run, not a performance promise. The path-free current record is verification/packaged_execution.json. The older original_execution record remains an unchanged historical snapshot; its then-unrun packaging status is superseded by this separate current record.

The larger original author proofs-only/full-suite programs are not part of this entry and are not rerun by it. Earlier author executions are not promoted into fresh independent proof reviews. No claim about coefficientwise Stieltjes properties, unrelated experiments or literature priority is produced by the program.

## Rebuilding the manuscript

`paper/proof.tex` is standalone. With its standard LaTeX packages installed, run `pdflatex proof.tex` twice from `paper/` to resolve citations and cross-references. A rebuild may change PDF metadata and font encoding; the manifest identifies the exact distributed PDF. No third-party source PDF is needed.
