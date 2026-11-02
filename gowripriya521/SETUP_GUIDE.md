# Deployment Instructions for gowripriya521 Profile

All assets including the custom retro stats scanline terminal screen are included.

### Option 1: Direct Browser Upload (No Git CLI needed)
1. In your `gowripriya521` repo on github.com, click **Add file** -> **Upload files**.
2. Drag and drop `README.md` and the entire `assets` directory.
3. Click **Commit changes**.
4. Click **Add file** -> **Create new file**, name it `.github/workflows/snake.yml`, paste the YAML from that file, and commit.
5. In repo **Settings** > **Actions** > **General** > **Workflow permissions**, choose **Read and write permissions**, and click **Save**.

### Option 2: Push via Git Terminal
```bash
git init
git add .
git commit -m "feat: complete terminal HUD profile with retro stats scanline animation"
git branch -M main
git remote add origin https://github.com/gowripriya521/gowripriya521.git
git push -u origin main --force
```
