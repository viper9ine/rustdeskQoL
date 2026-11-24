"""QoL fork: make the Windows privacy screen pure black.

RustDesk's privacy mode (Mode 1) covers the screen with a window drawn by
WindowInjection.dll, built from rustdesk-org/RustDeskTempTopMostWindow.
That window is cleared to black and then a "Privacy Mode" picture is drawn
on top. This script removes the picture so only the black background is left.

Usage: python patch_topmost_window.py <path to RustDeskTempTopMostWindow checkout>

The script fails loudly if the upstream code changed, so the build stops
instead of silently shipping the stock picture.
"""

import pathlib
import sys

OLD = "graphics.DrawImage(bitmap, dest);"
NEW = "(void)dest; // QoL fork: keep the privacy screen pure black (no picture)."


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    src = pathlib.Path(sys.argv[1]) / "WindowInjection" / "dllmain.cpp"
    data = src.read_bytes().decode("utf-8")
    count = data.count(OLD)
    if count != 1:
        print(f"Expected exactly one '{OLD}' in {src}, found {count}.")
        print("RustDeskTempTopMostWindow changed upstream; update this script.")
        return 1
    src.write_bytes(data.replace(OLD, NEW).encode("utf-8"))
    print(f"Patched {src}: privacy screen will be pure black.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
