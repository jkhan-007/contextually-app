import os
import sys

sys.path.insert(0, '.')
sys.path.insert(0, '../..')

import contextual

block_cipher = None
# noinspection PyUnresolvedReferences
import PyQt5

# noinspection PyUnresolvedReferences
a = Analysis(['../../contextual/application.py'],
             pathex=[
                 os.path.join(sys.modules['PyQt5'].__path__[0], 'Qt', 'bin'),
                 '../..'
             ],
             binaries=[],
             datas=[
                 ('../../contextual/__init__.py', '.')
             ],
             hiddenimports=['PyQt5.sip'],
             hookspath=[],
             runtime_hooks=[],
             excludes=['numpy'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher
             )

# noinspection PyUnresolvedReferences
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

# noinspection PyUnresolvedReferences
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name=contextual.__appname__,
          debug=False,
          strip=True,
          upx=False,
          console=False,
          icon='../data/icons/contextually.icns')

# noinspection PyUnresolvedReferences
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=True,
               upx=False,
               name=contextual.__appname__)

# noinspection PyUnresolvedReferences
app = BUNDLE(coll,
             name='{}.app'.format(contextual.__appname__),
             icon='../data/icons/contextually.icns',
             bundle_identifier=contextual.__desktopid__,
             info_plist={
                 'CFBundleShortVersionString': contextual.__version__,
                 'NSHighResolutionCapable': 'True'
             })
