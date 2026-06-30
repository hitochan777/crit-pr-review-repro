# crit bug repro: PR diff vanishes on round-complete

Reproduces the bug where `crit --pr 1` shows the correct diff on initial load,
but after firing round-complete (re-running `crit`) the diff disappears.

## Reproduction steps

1. Clone this repo and check out `main`:
   ```
   git clone https://github.com/hitochan777/crit-pr-review-repro
   cd crit-pr-review-repro
   git checkout main
   ```
   `main` is clean and is the merge-base with the default branch — this is the
   key condition that triggers the bug.

2. Start a PR review:
   ```
   crit --pr 1
   ```
   The diff for `feat/add-logging` renders correctly on the initial load.

3. Fire round-complete by re-running `crit` (or advancing the round via the `/crit` loop).

4. **Bug:** the PR diff disappears, leaving only comment files. The focus state
   (`kind=range`, `base_sha`, `head_sha`) is preserved, but `RefreshFileList`
   ignores it and falls back to `git diff <baseRef>` against the working tree,
   which is empty because `main` == `baseRef`.

## Root cause

`RefreshFileList` (`internal/session/watch.go:77`) reads `s.BaseRef` and calls
`changedFilesForSession`, which runs `git diff <baseRef>` against the working
tree. It never consults `s.Focus`. The initial load correctly uses
`buildFilesForFocus` → `git diff base..head`, but round-complete skips that path.

See the full bug report for call-chain details and fix options.
