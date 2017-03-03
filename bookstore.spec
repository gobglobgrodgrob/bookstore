# -*- mode: python -*-

block_cipher = None


a = Analysis(['bookstore.py'],
             pathex=['C:\\Users\\Nicholas Chow\\Google Drive\\projects\\python_mega_course\\bookstore'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='bookstore',
          debug=False,
          strip=False,
          upx=True,
          console=False )
