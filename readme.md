# Project Xe

xoroshiro128+が連続して出力する128個の乱数列(64bit)の下位1bitから内部状態(128bit=64bit+64bit)を逆算するプログラムです.

src/test.pyが逆算が成功しているproofになっています. たぶん色々書き換えれば逆算ツールになるはずです.

このアルゴリズムの提案者は[pattirudon](https://github.com/pattirudon/xoroshiroseed-java)氏のもので, 私のオリジナルではありません.

# Reference
### xoroshiro128+の状態遷移の逆算の考察
https://hackmd.io/@yatsuna827/r1ez2-n3S

### 【TinyMT】なぜ乱数値の最下位bit列から元の内部状態を復元できるのか考えてみた。
https://ameblo.jp/yatsuna/entry-12337825820.html
