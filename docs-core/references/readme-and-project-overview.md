# README and Project Overview

## README job

A README is a reliable entrance, not a complete encyclopedia. It should let the intended reader understand the project and reach first success quickly.

## Core structure

Use only applicable sections:

1. **Name and purpose:** what exists, for whom, and why.
2. **Status:** active, experimental, archived, internal, or production.
3. **Quick start:** shortest verified path to useful behavior.
4. **Prerequisites:** exact tools and supported versions from repository evidence.
5. **Configuration:** variable names and safe placeholders from `.env.example` only; never secret values.
6. **Run and verify:** command plus observable successful result.
7. **Tests and quality:** actual repository commands.
8. **Architecture/navigation:** short map and links to deeper docs.
9. **Deployment/operations:** link to authoritative delivery docs, not duplicated commands.
10. **Contributing/support/license:** only when relevant and verified.

Do not add badges, screenshots, feature claims, roadmaps, or compatibility matrices without an owner and source.

## Quick-start quality

A good quick start:

- starts from a declared initial state;
- uses commands copied from actual scripts, manifests, or CI;
- names the working directory;
- separates install, configure, run, and verify;
- states expected output or reachable behavior;
- offers one likely troubleshooting path;
- avoids production targets and destructive steps;
- does not expose or ask for secrets.

Do not claim “five minutes” unless the path has been measured in a representative environment.

## Project overview

For a deeper overview capture:

- users and supported workflows;
- system boundaries and external dependencies;
- deployable units and durable data;
- trust boundaries and operational ownership;
- major constraints and known limitations;
- links to architecture, API, runbooks, and handoff.

Use a compact diagram only when it clarifies three or more components or flows. Every node and edge must map to verified reality.

## Repository navigation

Explain structure by responsibility:

| Path | Responsibility | Entry point | Owner/source |
| --- | --- | --- | --- |

Avoid listing every folder. Highlight where a contributor reads, changes, tests, and verifies common work.

## Verification

Before finalizing:

- execute safe setup/build/test commands when feasible;
- confirm paths, anchors, filenames, ports, and package names;
- compare instructions with CI and deployment configuration;
- test relative links;
- ensure a new reader can identify the next document without guessing.
