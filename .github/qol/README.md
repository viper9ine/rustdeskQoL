# RustDesk QoL fork

Personal RustDesk fork tuned for controlling a Windows PC from an iPad.

## Changes

| Change | Where | How |
| --- | --- | --- |
| Privacy mode screen is pure black instead of the "Privacy Mode" picture | Windows | `patch_topmost_window.py`, applied to WindowInjection.dll during the build |

## Builds

`.github/workflows/qol-windows.yml` ("QoL Windows build") builds the Windows x64 app with these changes:

- every push to `master` publishes the installer to the **qol-windows** release of this repository;
- pull requests are built but not published;
- it can be started by hand from the Actions tab.

To pick up a new RustDesk version, press **Sync fork** on the repository page. The push to `master` starts a new build.

Everything this fork adds lives under `.github/` (`.github/qol/` and `.github/workflows/qol-windows.yml`), so syncing with upstream does not conflict.
