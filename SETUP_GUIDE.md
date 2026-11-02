# Setup Instructions for gowripriya521 GitHub Profile Repository

Follow these steps to deploy this repository directly to your GitHub profile:

1. Create a Special Repository:
   - Go to GitHub and click "New repository"
   - Repository name MUST be exactly: `gowripriya521` (matches your username)
   - Set visibility to **Public**
   - Check "Add a README file" (or leave empty to push this repo)

2. Push this Repository:
   ```bash
   git init
   git add .
   git commit -m "Initialize terminal HUD profile README and Snake workflow"
   git branch -M main
   git remote add origin https://github.com/gowripriya521/gowripriya521.git
   git push -u origin main --force
   ```

3. Enable GitHub Actions Permissions (Critical for Snake Contribution Animation):
   - In your repo `gowripriya521/gowripriya521`, go to **Settings** > **Actions** > **General**.
   - Scroll down to **Workflow permissions**.
   - Select **Read and write permissions**.
   - Click **Save**.

4. Run the Workflow:
   - Go to the **Actions** tab in your repository.
   - Click **Generate Snake Animation** on the left sidebar.
   - Click **Run workflow** > **Run workflow**.
   - This creates the `output` branch containing your contribution snake SVGs.

5. Adding Custom Terminal Animation:
   - Drop your custom particle GIF or animation into the `assets/` folder (e.g. `assets/hero-terminal.gif`).
   - In `README.md`, update the `<img>` src inside the HUD table to:
     `https://raw.githubusercontent.com/gowripriya521/gowripriya521/main/assets/hero-terminal.gif`
