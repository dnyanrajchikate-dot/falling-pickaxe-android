# Falling Pickaxe LIVE — Android APK

This project is prepared for an Android portrait APK using Buildozer + python-for-android + SDL2.

## Build

Run on Linux/WSL:

```bash
buildozer -v android debug
```

The APK will be created in `bin/`.

## Important

1. Put the YouTube API key in `src/config.json` before building if YouTube Live Chat commands are required.
2. The game is portrait/9:16.
3. The PC filesystem paths were adjusted for the Android source layout.
4. The debug APK is for local installation/testing.

python-for-android requires Android SDK/NDK and its compiled dependencies; Buildozer automates this build process.
