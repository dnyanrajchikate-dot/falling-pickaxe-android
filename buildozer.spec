[app]
title = Falling Pickaxe LIVE
package.name = fallingpickaxe
package.domain = org.dnyarox
source.dir = src
source.include_exts = py,png,jpg,jpeg,wav,mp3,json,txt
source.exclude_dirs = .venv,logs,tests,.git,__pycache__,android_build
source.exclude_patterns = *.pyc,src/*.IMP.py,src/*.old.py,src/*.MOST.py
version = 1.0.0
requirements = python3,pygame-ce,pymunk,grpcio,protobuf,google-api-python-client,google-auth,google-auth-httplib2,python-dateutil
orientation = portrait
fullscreen = 1
android.api = 35
android.minapi = 24
android.ndk_api = 24
android.ndk = 28c
android.accept_sdk_license = True
android.archs = arm64-v8a
android.permissions = INTERNET,WAKE_LOCK
android.allow_backup = True
android.debug_artifact = apk
android.release_artifact = aab
p4a.bootstrap = sdl2
p4a.branch = develop
p4a.local_recipes = ../p4a-recipes
p4a.extra_args = --color=always

[buildozer]
log_level = 2
warn_on_root = 1
