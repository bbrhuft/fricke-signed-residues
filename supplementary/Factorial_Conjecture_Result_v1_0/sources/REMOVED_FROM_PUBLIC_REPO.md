# Third-party papers not redistributed

The original package contained user-supplied copies of three published papers.
They are copyrighted by their publishers and are not included in this public repository:

- Robert, G. (1980). Congruences entre séries d'Eisenstein, dans le cas supersingulier. *Inventiones Mathematicae*, 61, 103–158.
- Landweber, P. S. (1988). Supersingular elliptic curves and congruences for Legendre polynomials. *Lecture Notes in Mathematics*, 1326, 69–93.
- Kaneko, M., & Zagier, D. (1998). Supersingular j-invariants, hypergeometric series, and Atkin's orthogonal polynomials. *AMS/IP Studies in Advanced Mathematics*, 7, 97–126.

Consequently, `sha256sum -c SHA256SUMS.txt` in this package reports these three
entries as missing (lines 28–30). Every other file is unchanged and verifies.
