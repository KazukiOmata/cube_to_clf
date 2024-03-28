# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['cube_to_clf.py'],
    pathex=[],
    binaries=[],
    datas=[('./ocio/bin/ociomakeclf', 'ocio/bin/')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='cube_to_clf',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
app = BUNDLE(
    exe,
    name='cube_to_clf.app',
    icon=None,
    bundle_identifier=None,
)
