# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_all

block_cipher = None

tkdnd_datas, tkdnd_binaries, tkdnd_hidden = collect_all("tkinterdnd2")

a = Analysis(
    ["app.py"],
    binaries=tkdnd_binaries,
    datas=tkdnd_datas,
    hiddenimports=tkdnd_hidden,
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data)

exe = EXE(
    pyz,
    a.scripts,
    exclude_binaries=True,
    name="ImageFlow",
    console=False,
    icon="icon.ico",
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    name="ImageFlow",
)
