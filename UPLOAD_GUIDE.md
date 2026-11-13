# Upload the v1.1.0 review package from Android

The GitHub connector can create text files and Git objects, but its exposed write actions do not accept a local binary file reference. This branch therefore includes a safe one-time bulk-import bridge: upload the ZIP through GitHub's normal web file picker, and GitHub Actions will unpack it into the review branch and run validation.

## Before uploading
This GitHub repository is currently **public**. Anything committed to a branch—including the ZIP, source, logo and presenter image assets—is publicly visible. Do not upload credentials, private newsroom material or assets you do not intend to make public. If that is not acceptable, stop and make a separate private repository first.

## Android steps
1. Download the attached review ZIP to your phone: `real-belize-news-mobile-studio-v1.1.0-option-c-review.zip`.
2. Open this branch's `incoming` folder: https://github.com/real-belize-news-studio/The-Real-Belize-Mobile-Studio/tree/review/v1.1.0-option-c-import/incoming
3. Tap **Add file** → **Upload files**.
4. Select the ZIP from Downloads. Keep its filename exactly: `real-belize-news-mobile-studio-v1.1.0-option-c-review.zip`.
5. Commit the upload to branch `review/v1.1.0-option-c-import` (not main).
6. GitHub Actions will validate the archive, unpack it to `app/real-belize-smart-news-studio/`, commit the source to this review branch, then attempt dependency installation, TypeScript checks and a Remotion preview render.
7. Return to the pull request and review the Actions results. Do not merge the PR or deploy until Eloim approves.

The importer rejects path traversal, symlinks, unexpected root folders, credential-like files, corrupted archives and oversized packages. The ZIP is retained under `incoming/` as the source artifact for reproducibility. The workflow does not deploy or publish the application.
