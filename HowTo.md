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
py2app ...
```

#### Icons from

https://icons8.com/icon/pack/free-icons/ios-glyphs

#### Generate Resources

```
$ pyrcc5 -compress 9 -o contextual/resources_rc.py contextual/resources.qrc
```

#### Generate code from ui files

```
$ for i in `ls resources/ui/*.ui`; do FNAME=`basename $i ".ui"`; pyuic5 $i > "contextual/ui/generated/$FNAME.py"; done
```