#!/usr/bin/env python3
"""SVG generator — charts, shapes, fractals."""
import math, sys

class SVG:
    def __init__(self, width=400, height=400):
        self.w=width; self.h=height; self.elements=[]
    def rect(self, x, y, w, h, fill="blue", opacity=1):
        self.elements.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" opacity="{opacity}"/>')
    def circle(self, cx, cy, r, fill="red"):
        self.elements.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"/>')
    def line(self, x1, y1, x2, y2, stroke="black", width=1):
        self.elements.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{width}"/>')
    def text(self, x, y, txt, size=12, fill="black"):
        self.elements.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}">{txt}</text>')
    def path(self, d, stroke="black", fill="none", width=1):
        self.elements.append(f'<path d="{d}" stroke="{stroke}" fill="{fill}" stroke-width="{width}"/>')
    def render(self):
        return f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}" height="{self.h}">\n' + "\n".join(self.elements) + "\n</svg>"
    def save(self, filename):
        with open(filename, "w") as f: f.write(self.render())

def bar_chart(data, filename="chart.svg"):
    svg = SVG(400, 300); max_val = max(data.values())
    bar_w = 300 / len(data); i = 0
    for label, val in data.items():
        h = val / max_val * 200; x = 50 + i * bar_w
        svg.rect(x, 250 - h, bar_w * 0.8, h, fill=f"hsl({i*60},70%,50%)")
        svg.text(x, 270, label, size=10); i += 1
    svg.save(filename); return filename

if __name__ == "__main__":
    data = {"Mon": 10, "Tue": 25, "Wed": 18, "Thu": 30, "Fri": 22}
    out = bar_chart(data)
    print(f"Generated: {out}")
    # Spiral
    svg = SVG(400, 400)
    for i in range(200):
        t = i * 0.1; r = t * 3
        x = 200 + r * math.cos(t); y = 200 + r * math.sin(t)
        svg.circle(x, y, 2, f"hsl({i*2},80%,50%)")
    svg.save("spiral.svg"); print("Generated: spiral.svg")
