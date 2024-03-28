# cube_to_clf


intel macに対してのappが動作していない。
terminalの方は動いている。



2024/03/28時点では
brewからopnecolorioをinstlallしている前提で動くようにしている。


The only environment variable you must configure manually is OCIO, which points to the configuration file you wish to use. For prebuilt config files, see the Downloads section
To do this, you would add a line to ~/.bashrc (or a per-project configuration script etc), for example:


手動で設定しなければならない唯一の環境変数はOCIOで、これは使用したい設定ファイルを指す。ビルド済みの設定ファイルについては、ダウンロードのセクションを参照してください。
https://opencolorio.readthedocs.io/en/latest/quick_start/installation.html


OCIO 環境変数については自分でconfig.ocioがある場所を示さないといけない。
```
export OCIO="/path/to/my/config.ocio"
```
