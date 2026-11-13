# Security Policy

## Scope

The Real Belize News Mobile Studio may handle unpublished reporting, source records, newsroom credentials, media files and audience information. Treat all such information as confidential unless approved for public release.

## Credential handling

- Never commit API keys, OAuth client secrets, access/refresh tokens, passwords, encryption keys, service-role keys or database connection strings.
- Do not place secrets in HTML, JavaScript bundles, local storage, public JSON manifests or client-visible environment variables.
- Use server-side environment variables or Supabase Edge Function secrets.
- Use a dedicated least-privilege service identity for each integration.
- Rotate any credential that may have been exposed and review access logs.
- Do not request credentials from the owner in chat; use the provider's secure authorization flow.

## Data protection

- Keep unpublished story leads, source identities, private audience messages and personal data out of public repositories and public storage.
- Require authenticated access and row-level security for newsroom records.
- Use private media buckets and short-lived signed URLs where appropriate.
- Validate file type, size and content server-side; do not trust browser-provided MIME types.
- Apply rate limits, origin validation, input validation and audit logs to backend endpoints.
- Define retention and deletion rules before importing real audience or source data.

## Editorial and publishing controls

- Do not automatically publish, schedule, boost, delete or reply publicly.
- Require explicit editor approval before any external publication action.
- Preserve source links, evidence, verification status, corrections and revision history.
- Clearly label allegations and unverified claims.

## Reporting

Report suspected vulnerabilities privately to the repository owner. Do not publish exploit details or private data in public issues.
