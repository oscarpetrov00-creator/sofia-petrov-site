#!/usr/bin/env python3
"""Wrap src/*.html page bodies in the shared header/footer and write site/*.html.

File names match the live site (sofiapetrovdds.com) so existing links, Google
results and the server's send_email.php keep working when this replaces it.
"""
from pathlib import Path

ROOT = Path(__file__).parent
SRC, OUT = ROOT / "src", ROOT / "site"

PHONE = "360-775-4437"
TEL = "tel:+13607754437"
EMAIL = "sofiapetrovdds@gmail.com"
ADDRESS = "512 E. Washington St. Suite 1, Sequim, WA 98382"
MAPS = "https://maps.app.goo.gl/dTypHLrK5n7s6mwi9"

PAGES = {
    "index": ("Integrative Periodontology and Implant Center | Sofia Petrov, DDS, MSD | Sequim, WA",
              "Board-certified periodontist Dr. Sofia Petrov offers LANAP laser gum treatment, dental implants and advanced periodontal care in Sequim, WA."),
    "treatments": ("Treatments | LANAP, Implants & Periodontal Care | Integrative Periodontology",
                   "LANAP and LAPIP laser therapy, dental implants, bone grafting, gum recession treatment, crown lengthening, PAOO, salivary diagnostics and PRP/PRF in Sequim, WA."),
    "dr_petrov": ("Dr. Sofia Petrov, DDS, MSD | Board-Certified Periodontist | Sequim, WA",
                  "Diplomate of the American Board of Periodontology and past President of the Washington State Society of Periodontists."),
    "forms": ("Patient Forms & Instructions | Integrative Periodontology and Implant Center",
              "Registration, consent forms, post-operative instructions and patient education from Dr. Sofia Petrov's office."),
    "doctor-referral": ("Doctor Referral | Integrative Periodontology and Implant Center",
                        "Refer a patient to Dr. Sofia Petrov, board-certified periodontist in Sequim, WA."),
    "contact-us": ("Contact | Integrative Periodontology and Implant Center | Sequim, WA",
                   f"Call {PHONE} or send a message. {ADDRESS}."),
    "privacy_policy": ("Privacy Policy & Disclosure | Integrative Periodontology and Implant Center",
                       "Privacy policy and disclosure for sofiapetrovdds.com."),
}

NAV = [
    ("treatments.html#lanap", "LANAP", "nav-lanap", None),
    ("treatments.html", "Treatments", "", "treatments"),
    ("dr_petrov.html", "Dr. Petrov", "", "dr_petrov"),
    ("forms.html", "Patient Forms", "", "forms"),
    ("doctor-referral.html", "Referring Doctors", "", "doctor-referral"),
    ("contact-us.html", "Contact", "", "contact-us"),
]


def header(page):
    links = "\n".join(
        f'      <a href="{href}"'
        + (f' class="{cls}"' if cls else "")
        + (' aria-current="page"' if key == page else "")
        + f">{label}</a>"
        for href, label, cls, key in NAV
    )
    return f"""<a class="skip" href="#main">Skip to content</a>
<div class="topbar">
  <div class="wrap">
    <div><span>Tue – Thu 9:00am – 4:30pm</span><span class="hide-sm">Saturday by appointment</span></div>
    <div><span class="hide-sm"><a href="{MAPS}">512 E. Washington St., Sequim</a></span><span><a href="{TEL}">{PHONE}</a></span></div>
  </div>
</div>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="index.html">
      <img src="img/logo.png" alt="Festina Lente butterfly logo" width="58" height="48">
      <span><span class="brand-name">Integrative Periodontology<br>and Implant Center</span>
      <span class="brand-sub">Sofia Petrov, DDS, MSD</span></span>
    </a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="nav">Menu</button>
    <nav class="nav" id="nav" aria-label="Main">
{links}
      <a class="btn btn-primary" href="{TEL}">Call {PHONE}</a>
    </nav>
  </div>
</header>"""


FOOTER = f"""<footer class="site-footer">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <div class="foot-brand"><img src="img/logo.png" alt="" width="56" height="46"><strong>Integrative Periodontology<br>and Implant Center</strong></div>
        <p>At Integrative Periodontology and Implant Center we are dedicated to providing exceptional dental care with a focus on your health, comfort, and satisfaction. Our team of experienced and compassionate professionals is committed to delivering personalized treatments, utilizing advanced technology, and fostering a warm, welcoming atmosphere.</p>
        <p class="foot-motto">Festina lente.</p>
        <div class="social">
          <a href="https://www.facebook.com/share/nNpQZf5EVuX414TU/?mibextid=LQQJ4d">Facebook</a>
          <a href="https://www.linkedin.com/in/sofia-petrov-7b5b9a47">LinkedIn</a>
        </div>
      </div>
      <div>
        <h4>Navigation</h4>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="treatments.html">Treatment Options</a></li>
          <li><a href="treatments.html#lanap">LANAP Laser Therapy</a></li>
          <li><a href="dr_petrov.html">Dr. Sofia Petrov</a></li>
          <li><a href="forms.html">Patient Forms</a></li>
          <li><a href="doctor-referral.html">Doctor Referral</a></li>
          <li><a href="contact-us.html">Contact Us</a></li>
        </ul>
      </div>
      <div>
        <h4>Office Hours</h4>
        <p>Tuesday – Thursday<br>9:00am – 4:30pm</p>
        <p>Saturday by appointment only</p>
      </div>
      <div>
        <h4>Contact</h4>
        <ul>
          <li><a href="{TEL}">{PHONE}</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><a href="{MAPS}">512 E. Washington St. Suite 1<br>Sequim, WA 98382</a></li>
        </ul>
      </div>
    </div>
    <div class="foot-bottom">
      <span>© 2024–2026 Integrative Periodontology and Implant Center. All rights reserved.</span>
      <span><a href="privacy_policy.html">Privacy Policy &amp; Disclosure</a></span>
    </div>
  </div>
</footer>
<script>
  (function () {{
    var b = document.querySelector('.nav-toggle'), n = document.getElementById('nav');
    if (!b || !n) return;
    b.addEventListener('click', function () {{
      var open = n.classList.toggle('open');
      b.setAttribute('aria-expanded', open ? 'true' : 'false');
      b.textContent = open ? 'Close' : 'Menu';
    }});
  }})();
</script>"""


def page(name, title, desc, body):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="img/favicon.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,500;0,8..60,600;1,8..60,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/site.css">
</head>
<body>
{header(name)}
<main id="main">
{body}
</main>
{FOOTER}
</body>
</html>
"""


PREVIEW_BANNER = """<div style="background:#e2ab3f;color:#1c2140;text-align:center;font:600 14px/1.4 Inter,system-ui,sans-serif;padding:9px 16px">
  Preview of the new site. The contact and referral forms don't send yet; please call 360-775-4437.
</div>"""

PREVIEW_JS = """<script>
  document.querySelectorAll('form').forEach(function (f) {
    f.addEventListener('submit', function (e) {
      e.preventDefault(); e.stopImmediatePropagation();
      alert('This is a preview. Forms will work once the new site is live. Please call 360-775-4437.');
    }, true);
  });
</script>"""


def main():
    """`build.py` writes site/. `build.py --preview DIR` writes a GitHub Pages copy
    with a preview banner and forms disabled (send_email.php only exists on GoDaddy)."""
    import shutil, sys
    preview = "--preview" in sys.argv
    out = Path(sys.argv[sys.argv.index("--preview") + 1]) if preview else OUT
    if preview:
        for sub in ("css", "img", "pdf"):
            shutil.copytree(OUT / sub, out / sub, dirs_exist_ok=True)
        (out / ".nojekyll").write_text("")
    for name, (title, desc) in PAGES.items():
        body = (SRC / f"{name}.html").read_text()
        html = page(name, title, desc, body)
        if preview:
            html = html.replace('<a class="skip"', PREVIEW_BANNER + '\n<a class="skip"', 1)
            html = html.replace("</body>", PREVIEW_JS + "\n</body>")
            html = html.replace("<head>", '<head>\n<meta name="robots" content="noindex">', 1)
        (out / f"{name}.html").write_text(html)
        print("built", name, "(preview)" if preview else "")


if __name__ == "__main__":
    main()
