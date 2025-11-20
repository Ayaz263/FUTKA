# Здесь ваш правильный buildozer.spec код
[app]
title = FUTKA
package.name = com.Utka.FUTKA
version = 0.1 
source.dir = . 
android.api = 21
android.min_api = 21
android.target_api = 21
orientation = portrait
android.permissions = INTERNET
source.include_exts = py,png,jpg,kv,atlas,pc
requirements = python3,kivy,socket
buildozer.build_mode = debug
icon.filename = %(source.dir)s/icon.png
[buildozer]
log_level = 2
