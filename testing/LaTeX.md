# LaTeX Mathematics Cheat Sheet

This guide covers the most common LaTeX syntax used for rendering mathematical formulas in Markdown documents using engines like 

When $a \ne 0$, there are two solutions to $$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

[MathJax](https://www.mathjax.org/) or [KaTeX](https://katex.org/)

.

---

## 1. Core Syntax & Delimiters

*   **Inline Math:** Wrap formulas in single dollar signs `$ ... $` to include them within a sentence.
    *   *Example:* The equation `$E=mc^2$` renders as E=mc².
*   **Display Math:** Wrap formulas in double dollar signs `$$ ... $$` to place them on their own centered line.
    *   *Example:* `$$E=mc^2$$` renders on its own distinct line.

---

## 2. Arithmetic & Basic Algebra

| Concept | Syntax | Example | Rendered |
| :--- | :--- | :--- | :--- |
| Exponents (Superscript) | `x^{2}` | `$x^{2}$` | x² |
| Subscripts | `x_{i}` | `$x_{i}$` | \(x_{i}\) |
| Multi-character scripts | `e^{i\pi}` | `$e^{i\pi}$` | \(e^{i\pi}\) |
| Fractions | `\frac{a}{b}` | `$\frac{1}{2}$` | \(\frac{1}{2}\) |
| Square Roots | `\sqrt{x}` | `$\sqrt{x}$` | \(\sqrt{x}\) |
| Higher-order Roots | `\sqrt[n]{x}` | `$\sqrt[3]{8}$` | \(\sqrt[3]{8}\) |
| Multiplication (Dot) | `\cdot` | `$a \cdot b$` | a ⋅ b |
| Multiplication (Cross) | `\times` | `$2 \times 3$` | 2 × 3 |
| Division Symbol | `\div` | `$6 \div 2$` | 6 ÷ 2 |
| Plus-Minus | `\pm` | `$\pm x$` | ± x |

---

## 3. Relations & Logic

| Concept | Syntax | Example | Rendered |
| :--- | :--- | :--- | :--- |
| Greater / Less Than | `<` , `>` | `$a < b > c$` | a < b > c |
| Less / Equal to | `\le` or `\leq` | `$a \le b$` | a ≤ b |
| Greater / Equal to | `\ge` or `\geq` | `$a \ge b$` | a ≥ b |
| Not Equal To | `\ne` or `\neq` | `$a \ne b$` | a ≠ b |
| Approximately Equal | `\approx` | `$\pi \approx 3.14$` | π ≈ 3.14 |
| Proportional To | `\propto` | `$y \propto x$` | \(y \propto x\) |
| Equivalence (Infinity) | `\infty` | `$x \to \infty$` | x → ∞ |
| Therefore / Because | `\therefore` , `\because` | `$\therefore x = 1$` | \(\therefore x = 1\) |

---

## 4. Greek Letters

### Lowercase

| Letter | Syntax | Rendered | Letter | Syntax | Rendered |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Alpha | `\alpha` | α | Beta | `\beta` | β |
| Gamma | `\gamma` | γ | Delta | `\delta` | δ |
| Epsilon | `\epsilon` | ε | Theta | `\theta` | θ |
| Lambda | `\lambda` | λ | Mu | `\mu` | μ |
| Pi | `\pi` | π | Rho | `\rho` | ρ |
| Sigma | `\sigma` | σ | Tau | `\tau` | τ |
| Phi | `\phi` | φ | Omega | `\omega` | ω |

### Uppercase

| Letter | Syntax | Rendered | Letter | Syntax | Rendered |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Gamma | `\Gamma` | Γ | Delta | `\Delta` | Δ |
| Theta | `\Theta` | Θ | Lambda | `\Lambda` | Λ |
| Pi | `\Pi` | Π | Sigma | `\Sigma` | Σ |
| Phi | `\Phi` | Φ | Omega | `\Omega` | Ω |

---

## 5. Calculus & Advanced Math

| Concept | Syntax | Example | Rendered |
| :--- | :--- | :--- | :--- |
| Limits | `\lim_{x \to a}` | `$\lim_{x \to 0} x$` | \(\lim_{x \to 0} x\) |
| Integrals | `\int` | `$\int f(x)dx$` | \(\int f(x)dx\) |
| Definite Integrals | `\int_{a}^{b}` | `$\int_{0}^{1} x dx$` | \(\int_{0}^{1} x dx\) |
| Double Integrals | `\iint` | `$\iint_D dxdy$` | \(\iint_D dxdy\) |
| Summation | `\sum_{i=1}^{n}` | `$\sum_{i=1}^{n} i$` | \(\sum_{i=1}^{n} i\) |
| Products | `\prod` | `$\prod_{i=1}^{n} x_i$` | \(\prod_{i=1}^{n} x_i\) |
| Partial Derivative | `\partial` | `$\frac{\partial f}{\partial x}$` | \(\frac{\partial f}{\partial x}\) |
| Gradient / Del | `\nabla` | `$\nabla f$` | ∇ f |

---

## 6. Vectors & Matrices

### Vector Accents
*   Single character vector: `$\vec{v}$` \(\to \vec{v}\)
*   Multi-character vector: `$\overrightarrow{AB}$` \(\to \overrightarrow{AB}\)
*   Bold matrix/vector notation: `$\mathbf{X}$` \(\to \mathbf{X}\)

### Matrices
Matrices use an environment structure starting with `\begin{matrix}` and ending with `\end{matrix}`. Use `&` to separate columns and `\\` to separate rows.

**Standard Matrix (No Brackets):**
```text
$$\begin{matrix} a & b \\ c & d \end{matrix}$$
```
\[\begin{matrix} a & b \\ c & d \end{matrix}\]

**Bracketed Matrix (b丰富):**
```text
$$\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$$
```
\[\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}\]

**Parenthesized Matrix (p丰富):**
```text
\[\begin{pmatrix} x & y \\ z & w \end{pmatrix}\]
```
$$\begin{pmatrix} x & y \\ z & w \end{pmatrix}$$

---

## 7. Brackets & Parentheses (Auto-Sizing)

Standard text brackets like `(x)` do not scale automatically if the math inside them is tall (like a fraction). Use `\left` and `\right` modifiers to automatically size your brackets to match the content inside.

*   **Wrong (Fixed Size):** `$(\frac{1}{2})$` $\to (\frac{1}{2})$
*   **Right (Dynamic Size):** `$\left( \frac{1}{2} \right)$` $\to \left( \frac{1}{2} \right)$

### Bracket Types
*   Parentheses: `\left( ... \right)`
*   Square Brackets: `\left[ ... \right]`
*   Curly Braces (Must be escaped with a backslash): `\left\{ ... \right\}` $\to \left\{ x \right\}$
