# How to Deploy Locy to GitHub Pages 🚀

Since this is a static website (HTML/CSS/JS), the best and free way to host it is **GitHub Pages**.

## Step 1: Create the Repository
1.  Log in to [GitHub.com](https://github.com/).
2.  Click the **+** icon in the top right -> **New repository**.
3.  **Repository name**: `locy` (or `locy-official`).
4.  **Visibility**: Public (Required for free GitHub Pages).
5.  **Initialize**: Do **NOT** check "Add a README" or .gitignore (we already have them).
6.  Click **Create repository**.

## Step 2: Push the Code
Copy the HTTPS URL of your new repository (e.g., `https://github.com/StartUp/locy.git`).

**Option A (Let me do it):**
Paste the URL in the chat, and I will run the commands for you.

**Option B (Do it yourself):**
Open your terminal in this folder and run:
```bash
git remote add origin <YOUR_REPO_URL>
git branch -M main
git push -u origin main
```

## Step 3: Activate Hosting (Live)
1.  Go to your repository **Settings** tab.
2.  On the left menu, click **Pages**.
3.  Under **Build and deployment** > **Source**, select **Deploy from a branch**.
4.  Under **Branch**, select `main` and `/ (root)`. click **Save**.
5.  Wait about 1-2 minutes. GitHub will give you a link like `https://username.github.io/locy/`.

## Step 4: Configure DNS (locy.ai) 🌐
To make `locy.ai` work, go to your domain provider (GoDaddy, Namecheap, etc.) and add these records:

**1. A Records (Point root `@` to GitHub):**
Add these 4 separate A records:
*   `185.199.108.153`
*   `185.199.109.153`
*   `185.199.110.153`
*   `185.199.111.153`

**2. CNAME Record (Point `www` to your site):**
*   **Type**: `CNAME`
*   **Name**: `www`
*   **Value**: `msaglamoz.github.io`

*Note: DNS changes can take up to 24 hours to propagate, but usually happen in minutes.*

**Done! Your site is live.** ✅
