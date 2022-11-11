# ラインライブ配信監視ツール

## 概要

ラインライブの配信開始を LINE Notify で通知する。

## 使用例

まず CH_NUMBER と LINE_TOKEN を編集する。CH_NUMBER には監視したいチャンネルの番号を入力する。例えばウェザーニュースのラインライブ URL を見ると

`https://live.line.me/channels/659`

であるからチャンネル番号は 659 である。

LINE_TOKEN には LINE のトークンを入力する。トークンの発行は各自調べる。

CH_NUMBER と LINE_TOKEN が入力し終わったらあとは実行するだけ。

```
$ ./main.py
```

監視が開始され、監視対象のライブが始まると LINE Notify で通知が行われる。
