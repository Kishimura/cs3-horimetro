# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['src/flet_app.py'],
    pathex=[],
    binaries=[],
    datas=[('assets/icone.ico', 'assets')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[r'C:\Users\tiago\AppData\Local\Programs\Python\Python313\Lib\site-packages\flet_cli\__pyinstaller\rthooks\pyi_rth_localhost_fletd.py'],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Calculadora_Horimetro',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['assets/icone.ico'],
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Calculadora_Horimetro',
)
