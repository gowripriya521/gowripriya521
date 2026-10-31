# Final GitHub Profile Package — gowripriya521

## Included files

- `README.md` — complete profile page with banner, profile details, skills, projects, contribution image, LinkedIn, and Gmail.
- `dark.svg` and `light.svg` — theme-aware profile banner files.
- `.github/workflows/snake.yml` — contribution image generation workflow.

## Upload to GitHub

1. Open `https://github.com/gowripriya521/gowripriya521`.
2. Make sure the repository is public and the default branch is `main`.
3. Upload/replace `README.md`, `dark.svg`, and `light.svg` in the repository root.
4. Upload `.github/workflows/snake.yml` while preserving its folder path.
5. Commit the changes.

## GitHub Actions permission

In the profile repository (not account settings), open:

`Settings → Actions → General → Workflow permissions`

Choose **Read and write permissions**, then save.

## Stats cards — not configured yet

The supplied profile guide requires a private GitHub Readme Stats deployment on Vercel. This package deliberately does not contain fake or placeholder stats URLs. To add the stats and top-language cards, deploy your fork of `anuraghazra/github-readme-stats` to Vercel, set `PAT_1` in Vercel's environment variables (never in this repository), and then use your actual Vercel hostname.

## Contribution image note

The current workflow publishes `github-snake.gif` to the `output` branch. The file is included in the README as a contribution visual. You previously observed that it appears still in your viewer, so this package does not promise that it is visibly animated in every browser.

## Social links

- LinkedIn: `https://www.linkedin.com/in/gaddamgowripriya`
- Gmail: `gowripriyagaddam@gmail.com`

## Final checks

- Check the profile in both GitHub light and dark themes.
- Confirm `dark.svg` and `light.svg` load.
- Confirm the latest Actions workflow run succeeds and the `output` branch contains `github-snake.gif`.
- Do not upload your GitHub token or any other secret to this repository.
