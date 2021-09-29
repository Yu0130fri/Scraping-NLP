# Scraping-NLP

'Scraping-NLP' is a scraping the rakuten-travel website then analyze reputations with SVM 

# Requirement

I already prepare Dockerfile.
So you can build Dockerfile and can use the same requirements!

# Installation

```
cd Docker
docker build . 
cd ..
docker run -p 8888:8888 -v ./:/work --rm (dockerID)
```

If you have to keep container you remove '--rm'

# Usage

DEMOの実行方法など、"hoge"の基本的な使い方を説明する

```bash
git clone https://github.com/hoge/~
cd examples
python demo.py
```
