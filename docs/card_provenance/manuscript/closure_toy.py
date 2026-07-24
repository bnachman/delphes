#!/usr/bin/env python3
"""Standalone PREVIEW of the Z->mumu closure test (NOT a Delphes run).

Delphes' MomentumSmearing module smears each track/muon by scaling its momentum
by a Gaussian of relative width sigma/pt = ResolutionFormula(pt, eta). This script
reproduces exactly that operation on a toy Z->mumu sample, using the *actual*
ResolutionFormula strings from the stock and baseline ATLAS cards, to preview how
much the muon-resolution revision (barrel floor 1.0%->1.7%) widens the
reconstructed dimuon mass peak.

Caveats (why this is a preview, not the real closure test): no detector geometry,
acceptance, reconstruction inefficiency, FSR, or backgrounds; muon direction is
held fixed (as MomentumSmearing does) and only |p|~pt is scaled. The real test
runs the cards through Delphes on a generated sample -- see closure_test_plan.md.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

rng = np.random.default_rng(20260724)   # fixed seed -> reproducible
MZ, GZ, MMU = 91.1876, 2.4952, 0.10566
N = 200_000

# --- ATLAS muon ResolutionFormula, transcribed verbatim from the cards --------
# sqrt(a^2 + (b*pt)^2), per |eta| bin. (stock: barrel floor 0.010; baseline 0.017)
def res_atlas_stock(pt, aeta):
    a = np.where(aeta <= 0.5, 0.010, np.where(aeta <= 1.5, 0.015, 0.025))
    b = np.where(aeta <= 0.5, 1.0e-4, np.where(aeta <= 1.5, 1.5e-4, 3.5e-4))
    return np.sqrt(a**2 + (b*pt)**2)

def res_atlas_baseline(pt, aeta):
    a = np.where(aeta <= 0.5, 0.017, np.where(aeta <= 1.5, 0.017, 0.025))
    b = np.where(aeta <= 0.5, 1.0e-4, np.where(aeta <= 1.5, 1.5e-4, 3.5e-4))
    return np.sqrt(a**2 + (b*pt)**2)

# --- toy Z->mumu: Breit-Wigner mass, flat-ish production, isotropic decay ------
def make_zmumu(n):
    # Z 4-momentum: modest pT spectrum + rapidity, resonance mass ~ BW
    m = MZ + GZ/2*np.tan(np.pi*(rng.random(n)-0.5))          # Cauchy ~ BW
    m = np.clip(m, 60, 120)
    zpt = rng.exponential(15, n)                              # soft Z pT
    zphi = rng.uniform(-np.pi, np.pi, n)
    zy = rng.normal(0, 1.6, n)                               # rapidity
    mt = np.sqrt(m**2 + zpt**2)
    pz = mt*np.sinh(zy); E = mt*np.cosh(zy)
    zx, zy_, zz = zpt*np.cos(zphi), zpt*np.sin(zphi), pz
    # isotropic decay in Z rest frame
    ct = rng.uniform(-1, 1, n); st = np.sqrt(1-ct**2)
    ph = rng.uniform(-np.pi, np.pi, n)
    pstar = np.sqrt(np.clip((m/2)**2 - MMU**2, 0, None))
    px1, py1, pz1 = pstar*st*np.cos(ph), pstar*st*np.sin(ph), pstar*ct
    E1 = m/2
    # boost each muon to lab (boost vector = Z p / E)
    bx, by, bz = zx/E, zy_/E, zz/E
    def boost(px, py, pz, E0):
        b2 = bx**2+by**2+bz**2; g = 1/np.sqrt(1-np.clip(b2,0,0.999999))
        bp = bx*px+by*py+bz*pz
        f = (g-1)*np.divide(bp, b2, out=np.zeros_like(b2), where=b2>0) + g*E0
        return px+f*bx, py+f*by, pz+f*bz, g*(E0+bp)
    mu1 = boost(px1, py1, pz1, E1)
    mu2 = boost(-px1, -py1, -pz1, E1)
    return mu1, mu2

def kin(mu):
    px, py, pz, E = mu
    pt = np.hypot(px, py); p = np.sqrt(px**2+py**2+pz**2)
    eta = np.arctanh(np.clip(pz/p, -0.999999, 0.999999))
    return pt, eta, (px, py, pz, E)

def smear(mu, resfn):
    pt, eta, (px, py, pz, E) = kin(mu)
    aeta = np.abs(eta)
    s = resfn(pt, aeta)
    scale = 1 + rng.normal(0, 1, len(pt))*s      # scale momentum magnitude
    return px*scale, py*scale, pz*scale, np.sqrt((px*scale)**2+(py*scale)**2+(pz*scale)**2+MMU**2)

def mass(a, b):
    E = a[3]+b[3]; px=a[0]+b[0]; py=a[1]+b[1]; pz=a[2]+b[2]
    return np.sqrt(np.clip(E**2-px**2-py**2-pz**2, 0, None))

mu1, mu2 = make_zmumu(N)
pt1, eta1, _ = kin(mu1); pt2, eta2, _ = kin(mu2)
m_gen = mass(mu1, mu2)                                        # pre-smear (truth)
# fiducial: both muons pt>20, |eta|<2.5 (typical Z selection), both barrel
sel = (pt1>20)&(pt2>20)&(np.abs(eta1)<1.0)&(np.abs(eta2)<1.0)
def apply(resfn):
    s1 = smear((mu1[0][sel],mu1[1][sel],mu1[2][sel],mu1[3][sel]), resfn)
    s2 = smear((mu2[0][sel],mu2[1][sel],mu2[2][sel],mu2[3][sel]), resfn)
    return mass(s1, s2)

mg = m_gen[sel]
# mass RESPONSE (m_reco/m_gen - 1): cancels the Breit-Wigner, isolates resolution
r_stock = apply(res_atlas_stock)/mg - 1
r_base  = apply(res_atlas_baseline)/mg - 1
print("Panel A -- ATLAS Z->mumu (barrel) mass RESPONSE, resolution isolated:")
print(f"  stock card    sigma(m_reco/m_gen) = {100*r_stock.std():.2f}%")
print(f"  baseline card sigma(m_reco/m_gen) = {100*r_base.std():.2f}%  "
      f"(measured single-mu 1.7-2.3% -> ~1.2-1.6% on the pair)")

# --- Panel B: the headline block -- CMS charged-hadron track resolution (~3x) --
# single-track sigma(pt)/pt vs pt, barrel (|eta|<0.5), stock vs baseline card.
def res_cms_trk_stock(pt):    return np.sqrt(0.06**2  + (1.3e-3*pt)**2)
def res_cms_trk_base(pt):     return np.sqrt(0.009**2 + (2.3e-4*pt)**2)
ptgrid = np.logspace(0, 3, 200)

fig, axes = plt.subplots(1, 2, figsize=(7.6, 3.1))
ax = axes[0]
bins = np.linspace(-0.06, 0.06, 80)
ax.hist(r_stock, bins=bins, histtype="step", color="k", lw=1.4,
        label=f"stock ($\\sigma${100*r_stock.std():.2f}%)")
ax.hist(r_base, bins=bins, histtype="step", color="#d62728", lw=1.6,
        label=f"baseline ($\\sigma${100*r_base.std():.2f}%)")
ax.axvline(0, color="0.6", ls=":", lw=0.8)
ax.set_xlabel(r"$m_{\mu\mu}^{\rm reco}/m_{\mu\mu}^{\rm gen}-1$")
ax.set_ylabel("muon pairs / bin")
ax.set_title(r"A. ATLAS muon revision (Z, barrel)", fontsize=8.5)
ax.legend(fontsize=7, frameon=False, loc="upper right")

ax = axes[1]
ax.plot(ptgrid, 100*res_cms_trk_stock(ptgrid), "k-", lw=1.4, label="stock card")
ax.plot(ptgrid, 100*res_cms_trk_base(ptgrid), color="#1f77b4", lw=1.6,
        label="baseline (1405.6569)")
ax.set_xscale("log")
ax.set_xlabel(r"track $p_\mathrm{T}$ [GeV]")
ax.set_ylabel(r"$\sigma(p_\mathrm{T})/p_\mathrm{T}$ [%]")
ax.set_title(r"B. CMS charged-hadron track res. ($\sim$3$\times$)", fontsize=8.5)
ax.set_ylim(0, 25); ax.grid(True, which="both", ls=":", alpha=0.4)
ax.legend(fontsize=7, frameon=False, loc="upper left")

fig.suptitle("Closure PREVIEW (toy, not Delphes): muon revision is modest (BW-"
             "dominated at the Z); the track-resolution revision is the ~3x headline",
             fontsize=8, y=1.03)
fig.tight_layout()
fig.savefig("closure_toy.pdf", bbox_inches="tight")
print("wrote closure_toy.pdf")
