# LAVIS demo

以下リポジトリの内容をデモしたリポジトリ

[salesforce/LAVIS: LAVIS - A One-stop Library for Language-Vision Intelligence](https://github.com/salesforce/LAVIS)

## Env

- Python3.10.8
- Windows 11

## Libary

```bash
# 必要に応じて仮想環境を作成
python -m venv .venv
.\.venv\Scripts\activate  # Windowsの場合
pip install salesforce-lavis
```

## How to

### [demo.ipynb](./demo.ipynb)

ライブラリのインストールから、`BLIP`を使ったデモ（[キャプション生成](https://github.com/salesforce/LAVIS#image-captioning)、[画像質疑応答（VQA）](https://github.com/salesforce/LAVIS#visual-question-answering-vqa)、[ゼロショット画像分類](https://github.com/salesforce/LAVIS/blob/main/examples/blip_zero_shot_classification.ipynb)）をステップ by ステップで実行

### [blip_captioning_demo.py](./blip_captioning_demo.py)

`BLIP`による画像のキャプション生成を実行

```python:例
python blip_captioning_demo.py ./sample_images/sample_1.JPG
```

出力例

![fig_1](./docs/a%20security%20guard%20in%20front%20of%20tokyo%20dome.png)


### [blip_vqa_demo.py](./blip_vqa_demo.py)

`BLIP`による画像に関する自由形式の質問応答

```python:例
python blip_vqa_demo.py ./sample_images/sample_2.jpg "How many usb ports?"
```

出力例

![fig_2](./docs/how%20many%20usb%20ports%20-%203.png)
