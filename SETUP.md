# Setup guide — gowripriya521 GitHub profile

This repository package follows the supplied **GitHub-Profile-Master-Prompt.pdf** and
**GitHub-Profile-Setup-Guide.pdf**, with biography and projects based on `gowri_resume.pdf`.

## Files included

- `README.md` — profile content, themed stats-card layout, social badge, and commented banner/snake display blocks.
- `.github/workflows/snake.yml` — scheduled contribution-snake workflow.
- `SETUP.md` — this guide.

## 1. Push the repository

The profile repository must be public and named exactly `gowripriya521/gowripriya521`, with the default branch named `main`.

From the extracted folder, run:

```powershell
git init
git branch -M main
git add README.md SETUP.md .github/workflows/snake.yml
git commit -m "feat: prepare GitHub profile repository"
git remote add origin https://github.com/gowripriya521/gowripriya521.git
git push -u origin main
```

If the remote repository already contains commits, clone it first and copy these files into that clone instead of running `git init`.

## 2. Phase 1 — animated terminal banner

The Master Prompt specifies `dark.svg` and `light.svg` generated from your own head-and-shoulders photo and three logo references. Those source images were not present with the files available for this task, so this package does **not** invent a portrait or claim the custom animated banner is finished.

1. Choose a sharp head-and-shoulders photo with even lighting and a plain background; ideally the short edge is at least 1000 px.
2. Supply reference images for the three logos you want to morph between.
3. Generate and review both theme SVGs according to the Master Prompt.
4. Put `dark.svg` and `light.svg` in the repository root.
5. Uncomment the banner `<picture>` block near the top of `README.md`.

The specified banner is a substantial custom asset (roughly 900 KB–1 MB per the prompt). Keep the generator script and `.npy` source data with the project; the SVGs alone are not the source of truth.

## 3. Phase 2 — self-host GitHub stats (required by the PDF)

Do not use the shared public `github-readme-stats` instance for the stats and top-language cards.

1. Open https://github.com/settings/tokens and select **Tokens (classic)**.
2. Generate a token with the `repo` scope. The PDF specifies no expiration; choose an expiration policy you are comfortable managing if your account offers one.
3. Copy the token immediately. Treat it like a password. **Never put it in README.md, this repository, a chat, or a public website.**
4. Fork https://github.com/anuraghazra/github-readme-stats.
5. Sign in to https://vercel.com with GitHub and import your fork into a project on the free Hobby plan.
6. In the Vercel project's environment variables, add `PAT_1` with the token as its value, then deploy.
7. Copy your deployed host name, such as `your-instance.vercel.app`.
8. In `README.md`, replace both instances of `YOUR-VERCEL-INSTANCE` with that host name (without `https://`).
9. Test `https://YOUR-VERCEL-INSTANCE.vercel.app/api?username=gowripriya521&show_icons=true`.

`hide_rank=true` is intentional: the letter grade is heavily influenced by repository popularity/stars and can be misleading for newer accounts.

The streak card uses the URL and palette specified by the setup PDF. If the external streak service is unavailable, the card may temporarily fail.

## 4. Phase 3 — enable the contribution snake

1. Open this repository's **Settings → Actions → General**.
2. Under **Workflow permissions**, select **Read and write permissions**, then save. This is the repository's settings, not your account settings.
3. Commit `.github/workflows/snake.yml` to `main`.
4. Open the repository's **Actions** tab and run **Generate Snake Animation**, or wait for the workflow to run.
5. Confirm the run succeeds and creates the `output` branch containing `github-snake.svg` and `github-snake-dark.svg`.
6. Only after the run is green, uncomment the snake `<picture>` block in `README.md`.

The workflow runs on pushes to `main`, manually, and every 12 hours. Scheduled workflows can pause after prolonged repository inactivity.

## 5. Phase 4 — social badges

- The email badge is configured for `gowripriyagaddam@gmail.com`.
- The resume lists LinkedIn but does not expose a verified profile URL. Add the correct LinkedIn URL before uncommenting its badge.
- The profile setup PDF recommends skipping a GitHub badge on your own profile because your avatar already links to GitHub.

## 6. Verify the final profile

- Check the README in both GitHub light and dark appearance settings.
- Open SVGs directly if a card looks stale; GitHub's CDN may cache images.
- Check the latest workflow run if the snake is missing.
- Avoid publishing API tokens, passwords, or other secrets.
