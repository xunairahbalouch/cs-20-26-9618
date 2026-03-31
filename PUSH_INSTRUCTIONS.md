# Instructions for Pushing to GitHub

## Option 1: Using GitHub CLI (Recommended)

1. Open a terminal in the `cs-20-26-9618` directory

2. Authenticate with GitHub:
   ```bash
   gh auth login
   ```

3. Create the repository:
   ```bash
   gh repo create cs-20-26-9618 --public --source=. --push
   ```

## Option 2: Using GitHub Web

1. Go to https://github.com/new
2. Repository name: `cs-20-26-9618`
3. Select Public
4. Don't initialize with README
5. Click "Create repository"

6. Push existing repository:
   ```bash
   cd C:\Users\hp\cs-20-26-9618
   git remote add origin https://github.com/YOUR_USERNAME/cs-20-26-9618.git
   git branch -M main
   git push -u origin main
   ```

## Option 3: Using Personal Access Token

1. Create a PAT at https://github.com/settings/tokens
2. Run:
   ```bash
   gh auth login --with-token
   ```
3. Paste your token

## Verification

After pushing, verify at:
https://github.com/YOUR_USERNAME/cs-20-26-9618
