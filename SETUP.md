# Setup guide — gowripriya521

## 1. Add these files to your profile repository

Copy the contents of this folder into the root of:
`https://github.com/gowripriya521/gowripriya521`

Files included:
- `README.md` — profile layout
- `.github/workflows/snake.yml` — contribution snake generator
- `assets/profile-banner.svg` — terminal-style placeholder banner

## 2. Enable GitHub Actions write permissions

In your repository:
1. Open **Settings → Actions → General**.
2. Under **Workflow permissions**, select **Read and write permissions**.
3. Save.

## 3. Run the contribution snake workflow

1. Open the **Actions** tab.
2. Select **Generate contribution snake**.
3. Click **Run workflow**.
4. Wait for the workflow to finish successfully.

The workflow publishes generated SVG files to a branch named `output`. The README image may take a short time to appear after the first run.

## 4. Optional: update the banner

The current banner is a designed placeholder, not a portrait. Upload a clear head-and-shoulders photo if you want the portrait effect from the reference video. Avoid committing private information or secrets.

## 5. Optional: personalize social links

The LinkedIn badge currently links to the LinkedIn homepage. Replace it with your own profile URL if you want a personal link.

## Notes

- GitHub stats and language cards use public third-party services; their uptime and rate limits are outside your control.
- The README uses the standard GitHub Readme Stats hosted endpoint. If the cards stop loading, you can deploy your own instance and replace the image URLs.
- The animated, morphing technology logos and photo-dither effect from the video need custom assets/animation to reproduce exactly. This starter includes the profile structure and contribution snake workflow, and the banner can be customized once you provide a photo.
