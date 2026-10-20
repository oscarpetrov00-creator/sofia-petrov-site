# sofiapetrovdds.com redesign

Mom's practice site (Integrative Periodontology and Implant Center, Dr. Sofia Petrov), rebuilt 2026-10-20 at her request.

- `src/*.html`: page bodies. `build.py` wraps them in the shared header/footer and writes them to `site/`.
- `site/`: the deployable site. Static HTML/CSS with no framework, no jQuery, no Bootstrap.
- `_original/`: a snapshot of the live site as of 2026-10-20 (pages, images, PDFs) for reference.

## Constraints kept from the live site
- Same file names (index, treatments, dr_petrov, forms, doctor-referral, contact-us, privacy_policy), so old links and Google results still work.
- Forms POST to the existing `send_email.php` on the GoDaddy/Apache host, with the same field names and the same reCAPTCHA site keys. **That PHP file lives only on the server and isn't in this repo; deploy over the top of it, never wipe the folder.**
- All original copy is kept. Only typos were fixed (see the commit message).
