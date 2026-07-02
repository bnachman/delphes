"""Reusable: overlay Delphes curves on a rendered source-figure image."""
import numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
from PIL import Image

def _map(vals, cal, log=False):
    p1,v1,p2,v2 = cal
    if log: v1,v2,vals = np.log10(v1),np.log10(v2),np.log10(vals)
    return p1 + (p2-p1)*(vals-v1)/(v2-v1)

def overlay(image, out, title, curves, xcal, ycal, xlog=False, ylog=False, legend_loc="upper left"):
    """curves: list of dict(x,y,label,color,band=(lo,hi) optional)."""
    img = np.asarray(Image.open(image).convert("RGB")); H,W,_ = img.shape
    fig, ax = plt.subplots(figsize=(6.2,5.4)); ax.imshow(img)
    for c in curves:
        px = _map(np.asarray(c["x"]), xcal, xlog); py = _map(np.asarray(c["y"]), ycal, ylog)
        ax.plot(px, py, color=c["color"], lw=2.4, label=c["label"])
        if "band" in c:
            lo = _map(np.asarray(c["band"][0]), ycal, ylog); hi = _map(np.asarray(c["band"][1]), ycal, ylog)
            ax.fill_between(px, lo, hi, color=c["color"], alpha=0.22)
    ax.set_xlim(0,W); ax.set_ylim(H,0); ax.axis("off")
    ax.legend(loc=legend_loc, fontsize=8.5, framealpha=0.9)
    ax.set_title(title, fontsize=9)
    fig.tight_layout(); fig.savefig(out, bbox_inches="tight"); fig.savefig(out.replace(".pdf",".png"), bbox_inches="tight", dpi=130)
    print("wrote", out)
