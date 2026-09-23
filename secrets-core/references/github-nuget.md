# GitHub Packages / NuGet

## Safe repository configuration

Use this source-only `NuGet.Config`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<configuration>
  <packageSources>
    <clear />
    <add key="nuget.org" value="https://api.nuget.org/v3/index.json" protocolVersion="3" />
    <add key="github" value="https://nuget.pkg.github.com/1babii1/index.json" />
  </packageSources>
</configuration>
```

Do not add `packageSourceCredentials` with literal values.

## Local restore

Store these in the encrypted `github-nuget` vault using the interactive `~/.local/bin/secrets-edit github-nuget` command:

```dotenv
GITHUB_NUGET_USERNAME=1babii1
GITHUB_NUGET_TOKEN=<secret entered only in the SOPS editor>
```

`secrets-run` forms the standard NuGet credential variable inside the injected process:

```bash
~/.local/bin/secrets-run github-nuget -- dotnet restore
```

Never print or persist the composed variable.

## GitHub Actions restore

For a package accessible to the workflow repository:

```yaml
permissions:
  contents: read
  packages: read

steps:
  - uses: actions/checkout@v4
  - name: Restore
    env:
      NuGetPackageSourceCredentials_github: >-
        Username=${{ github.actor }};Password=${{ secrets.GITHUB_TOKEN }}
    run: dotnet restore
```

For an unconnected package in another private repository, place a minimal classic PAT in a repository or organization secret such as `GH_PACKAGES_READ_TOKEN` and substitute that secret. Never commit it.

## Publishing

Use `GITHUB_TOKEN` with `packages: write` inside the package repository workflow. Use a separate classic PAT with `write:packages` only when local publishing is required. Do not reuse a broad personal token intended for unrelated GitHub operations.
