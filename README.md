# The Real Belize News Mobile Studio

A mobile-first newsroom production workspace for The Real Belize. The application is intended for editorial preparation and media assembly. It is not authorized to publish, schedule, reply publicly, boost posts, or spend provider credits automatically.

## Repository status

This repository was initially created with only a short README. The reviewed application source bundle exists separately as release **v1.1.0** and has not yet been imported into this repository. Therefore this repository is **not currently deployable**. Do not connect a production host to this repository until the complete reviewed application source and required assets are committed.

## Editorial and safety controls

- Eloim Ellis retains final editorial and publication approval.
- Keep The Real Belize News identity separate from Belize People's Front party communications.
- Use the approved News palette: magenta, silver/grey, white and charcoal.
- Preserve the official News logo unchanged.
- Clearly distinguish verified facts, allegations, proposals and developing reports.
- Do not expose provider API keys, OAuth tokens, encryption keys or passwords in browser code or Git.
- ChatGPT connector access does not authenticate this standalone app with those providers.
- Publishing, scheduling, public replies, paid generation and paid promotion remain disabled unless separately approved.

## Deployment

See [DEPLOYMENT_READINESS.md](DEPLOYMENT_READINESS.md) and [SECURITY.md](SECURITY.md). Deployment must remain blocked until the application source is imported, dependencies and assets are audited, build checks pass, and the owner approves the preview.

## Current reviewed release

The separately prepared v1.1.0 bundle contains a browser-based mobile studio, PWA files, a Remotion/TypeScript media assembly scaffold, Supabase schema and Edge Function scaffolding, and setup documentation. It is a development package—not proof of a live deployment, authenticated provider integrations, or completed lip-synced broadcast rendering.
