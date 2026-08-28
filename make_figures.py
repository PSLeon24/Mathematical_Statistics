# -*- coding: utf-8 -*-
"""Figures for the mathematical statistics notes.

Every panel is a simulation or an exact computation, not an illustration. The
CLT panel really does average samples from a skewed distribution, the coverage
panel really does build 10,000 intervals and count how many contain the
parameter, and the power panel really does run the tests it reports.
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from scipy import stats  # noqa: E402

OUT = "figures"
BLUE, ORANGE, GREEN, GREY = "#2a78d6", "#eb6834", "#1baf7a", "#999999"
plt.rcParams.update({"font.size": 9, "axes.spines.top": False,
                     "axes.spines.right": False, "figure.dpi": 150})


def fig_clt():
    """The CLT is about the mean, not about the data."""
    rng = np.random.default_rng(0)
    pop = lambda n: rng.exponential(2.0, n)        # noqa: E731  strongly skewed
    fig, axes = plt.subplots(1, 4, figsize=(11.6, 3.0))
    axes[0].hist(pop(60000), bins=70, color=GREY, density=True)
    axes[0].set_title("Population: Exp(2)\nskew = 2, nothing normal about it", fontsize=9)
    for ax, n in zip(axes[1:], (2, 10, 40)):
        m = pop(60000 * n).reshape(60000, n).mean(1)
        ax.hist(m, bins=70, color=BLUE, density=True, alpha=0.85)
        xs = np.linspace(m.min(), m.max(), 300)
        ax.plot(xs, stats.norm.pdf(xs, 2.0, 2.0 / np.sqrt(n)), color=ORANGE, lw=1.8)
        ax.set_title("Mean of n = %d\nN(2, 2²/%d) overlaid" % (n, n), fontsize=9)
    for ax in axes:
        ax.set_yticks([])
    fig.suptitle("Central limit theorem: the sampling distribution of the mean "
                 "becomes normal even when the population is not", fontsize=10)
    fig.tight_layout(rect=(0, 0, 1, 0.87))
    fig.savefig(os.path.join(OUT, "clt.png"))
    plt.close(fig)


def fig_poisson():
    """Binomial to Poisson, with the approximation error measured."""
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(9.6, 3.6))
    k = np.arange(0, 15)
    lam = 3.0
    for n, col in ((10, "#9ec5f0"), (50, BLUE), (500, "#12406e")):
        p = lam / n
        a1.plot(k, stats.binom.pmf(k, n, p), "o-", ms=4, color=col, lw=1.2,
                label="Binomial(n=%d, p=%.3f)" % (n, p))
    a1.plot(k, stats.poisson.pmf(k, lam), "s--", color=ORANGE, ms=5,
            label="Poisson(λ=3)")
    a1.set_xlabel("k")
    a1.set_ylabel("P(X = k)")
    a1.set_title("Binomial → Poisson as n grows with np fixed", fontsize=10)
    a1.legend(frameon=False, fontsize=8)

    ns = np.array([5, 10, 20, 50, 100, 200, 500, 1000, 2000])
    err = [np.abs(stats.binom.pmf(k, n, lam / n) - stats.poisson.pmf(k, lam)).max()
           for n in ns]
    a2.loglog(ns, err, "o-", color=BLUE)
    a2.set_xlabel("n  (with np = 3 held fixed)")
    a2.set_ylabel("max |binomial − Poisson|")
    a2.set_title("Approximation error, measured\nslope ≈ −1, i.e. error ~ 1/n", fontsize=10)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "poisson.png"))
    plt.close(fig)


def fig_coverage():
    """What a 95% confidence interval actually promises."""
    rng = np.random.default_rng(1)
    n, mu, sd, trials = 12, 5.0, 2.0, 10000
    x = rng.normal(mu, sd, (trials, n))
    m = x.mean(1)
    s = x.std(1, ddof=1)
    tcrit = stats.t.ppf(0.975, n - 1)
    lo, hi = m - tcrit * s / np.sqrt(n), m + tcrit * s / np.sqrt(n)
    covered = (lo <= mu) & (mu <= hi)
    # the same intervals built with the normal quantile instead of t
    zlo, zhi = m - 1.96 * s / np.sqrt(n), m + 1.96 * s / np.sqrt(n)
    zcov = (zlo <= mu) & (mu <= zhi)

    fig, (a1, a2) = plt.subplots(1, 2, figsize=(9.8, 3.9),
                                 gridspec_kw={"width_ratios": [2, 1]})
    show = 60
    for i in range(show):
        col = BLUE if covered[i] else ORANGE
        a1.plot([lo[i], hi[i]], [i, i], color=col, lw=1.4)
    a1.axvline(mu, color="#333333", lw=1.4, ls="--")
    a1.set_yticks([])
    a1.set_xlabel("interval")
    a1.set_title("First 60 of 10,000 intervals\norange ones miss μ = 5", fontsize=10)

    a2.bar(["t\nquantile", "normal\nquantile"],
           [100 * covered.mean(), 100 * zcov.mean()],
           color=[BLUE, GREY])
    a2.axhline(95, color=ORANGE, lw=1.4, ls="--")
    a2.set_ylim(85, 100)
    a2.set_ylabel("coverage (%)")
    a2.set_title("Coverage over 10,000 trials, n = 12\n"
                 "t: %.1f%%   normal: %.1f%%" % (100 * covered.mean(), 100 * zcov.mean()),
                 fontsize=10)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "coverage.png"))
    plt.close(fig)


def fig_power():
    """Type I and II error, and the power curve those two imply."""
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(9.8, 3.7))
    x = np.linspace(-4, 8, 600)
    h0 = stats.norm.pdf(x, 0, 1)
    h1 = stats.norm.pdf(x, 2.8, 1)
    crit = stats.norm.ppf(0.95)
    a1.plot(x, h0, color=BLUE, lw=1.8, label="H₀: μ = 0")
    a1.plot(x, h1, color=GREEN, lw=1.8, label="H₁: μ = 2.8")
    a1.fill_between(x, 0, h0, where=(x > crit), color=ORANGE, alpha=0.55,
                    label="α = 0.05 (type I)")
    a1.fill_between(x, 0, h1, where=(x <= crit), color=GREY, alpha=0.55,
                    label="β (type II)")
    a1.axvline(crit, color="#333333", lw=1.2, ls="--")
    a1.set_title("The two errors are traded against each other\n"
                 "by moving one threshold", fontsize=10)
    a1.legend(frameon=False, fontsize=8)
    a1.set_yticks([])

    rng = np.random.default_rng(2)
    effects = np.linspace(0, 1.6, 17)
    for n, col in ((10, "#9ec5f0"), (30, BLUE), (100, "#12406e")):
        pw = []
        for d in effects:
            a = rng.normal(0, 1, (2000, n))
            b = rng.normal(d, 1, (2000, n))
            t, p = stats.ttest_ind(a, b, axis=1)
            pw.append((p < 0.05).mean())
        a2.plot(effects, pw, "o-", ms=3, color=col, lw=1.4, label="n = %d per group" % n)
    a2.axhline(0.8, color=ORANGE, ls="--", lw=1.2)
    a2.text(0.03, 0.82, "conventional 80% power", fontsize=8, color=ORANGE)
    a2.set_xlabel("true effect size (difference in means, σ = 1)")
    a2.set_ylabel("power  = P(reject | H₁ true)")
    a2.set_title("Power, from 2,000 simulated t-tests per point", fontsize=10)
    a2.legend(frameon=False, fontsize=8)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "power.png"))
    plt.close(fig)


def fig_families():
    """Where chi-squared, t and F come from, and how they relate."""
    fig, axes = plt.subplots(1, 3, figsize=(11.2, 3.3))
    x = np.linspace(0, 18, 500)
    for df, col in ((1, "#9ec5f0"), (3, BLUE), (8, "#12406e")):
        axes[0].plot(x, stats.chi2.pdf(x, df), color=col, lw=1.8, label="k = %d" % df)
    axes[0].set_title("χ²(k): sum of k squared\nstandard normals", fontsize=9)
    axes[0].set_ylim(0, 0.5)

    x = np.linspace(-5, 5, 500)
    for df, col in ((1, "#f6b394"), (5, ORANGE), (30, "#8c3a12")):
        axes[1].plot(x, stats.t.pdf(x, df), color=col, lw=1.8, label="ν = %d" % df)
    axes[1].plot(x, stats.norm.pdf(x), color=GREY, lw=1.6, ls="--", label="N(0,1)")
    axes[1].set_title("t(ν) = Z / √(χ²ᵥ/ν)\nheavier tails, → normal as ν grows", fontsize=9)

    x = np.linspace(0, 5, 500)
    for d, col in (((5, 5), "#a9e2c8"), ((10, 20), GREEN), ((50, 50), "#0d6b48")):
        axes[2].plot(x, stats.f.pdf(x, *d), color=col, lw=1.8, label="d = %s" % (d,))
    axes[2].set_title("F(d₁,d₂): ratio of two\nscaled χ² — the ANOVA statistic", fontsize=9)

    for ax in axes:
        ax.legend(frameon=False, fontsize=8)
        ax.set_yticks([])
    fig.suptitle("All three are built from normals, which is why they show up "
                 "wherever a normal model does", fontsize=10)
    fig.tight_layout(rect=(0, 0, 1, 0.88))
    fig.savefig(os.path.join(OUT, "families.png"))
    plt.close(fig)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    fig_clt()
    fig_poisson()
    fig_coverage()
    fig_power()
    fig_families()
    print("wrote", sorted(os.listdir(OUT)))
