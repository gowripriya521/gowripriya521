# Setup guide — gowripriya521

## 1. Publish the profile
1. Create a **public** repository named exactly `gowripriya521` (the same as your username).
2. Upload the contents of this project to the repository root, including `README.md`, `dark_mode.svg`, `light_mode.svg`, `assets/`, and `.github/workflows/snake.yml`.
3. Keep `generate_banner.py` and `assets/priya.jpeg` as the source files. The SVG banner renders an ASCII-character portrait derived from the supplied image; it does not embed the original photo as a normal photo.

## 2. Regenerate the banners locally
Requires Python 3.10+ and Pillow. Run `python -m pip install -r requirements.txt`, then `python generate_banner.py`. The script writes `dark_mode.svg`, `light_mode.svg` and compatibility copies `dark.svg`/`light.svg`. Commit the changed SVGs. SVG SMIL animation support can vary across viewers; test in a browser and GitHub.

## 3. Self-host GitHub Readme Stats on Vercel
1. Open GitHub Settings → Developer settings → Personal access tokens → Tokens (classic). Generate a token with `repo` scope if you need private-repository stats. Copy it immediately; GitHub shows it once. Never paste it into chat or commit it to a repository.
2. Fork `anuraghazra/github-readme-stats`.
3. Sign in to Vercel with GitHub, add a project, and import your fork.
4. Add environment variable `PAT_1` with the token value. Keep it secret. Deploy.
5. Replace `YOUR-VERCEL-INSTANCE` in README.md with your deployment host (without `https://`).

`hide_rank=true` is intentional: the rank is strongly influenced by stars and followers, so it is not a direct measure of coding skill.

## 4. Enable the contribution snake workflow
In the **gowripriya521/gowripriya521 repository** go to Settings → Actions → General → Workflow permissions. Select **Read and write permissions**, then Save. This is repository settings, not account settings.

The workflow runs on pushes to `main`, manual dispatch, and every 12 hours. It publishes two SVGs to the `output` branch. Only add the snake block in the README after the first workflow run succeeds and the `output` branch exists.

## 5. LinkedIn badge note
LinkedIn's logo may only render reliably in its official brand blue `#0A66C2`; the badge uses that blue for compatibility.

## 6. Profile details used
- Name: Gaddam Gowri Priya
- Role: Full-Stack Developer
- Location: Bangulore, Madanapalle (as supplied)
- Education: B.Tech
- Skills: Python, FastAPI, Pydantic AI, HTML, CSS, JavaScript
- LinkedIn: https://www.linkedin.com/in/gaddamgowripriya/
- Email: gowripriyagaddam@gmail.com

Instagram and portfolio links were not supplied, so they are omitted rather than invented.
