### HowTos

#### Generating Icns file from SVG

This will generate an icns file in packaging/data/icons/

```
$ ./mk-icns.sh $PWD/contextual/images/contextually.svg contextually
```

#### Running PyInstaller with Docker

Works for Linux

```
docker run --rm -ti -v $(pwd):/data imon/pyinstaller build packaging/pyinstaller/contextually.osx.spec
```

For Apple

```
python3 -m PyInstaller --clean packaging/pyinstaller/contextually.osx.spec
```

#### Icons from

https://icons8.com/icon/pack/free-icons/ios-glyphs