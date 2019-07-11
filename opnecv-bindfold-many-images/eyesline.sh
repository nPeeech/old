#!/bin/bash

# 画像ディレクトリ定義
out='./input/'

# 画像処理スクリプト名定義
script='eyesline.py'

for file in `ls ${out}`; do
    python ${script} ${file}
done
