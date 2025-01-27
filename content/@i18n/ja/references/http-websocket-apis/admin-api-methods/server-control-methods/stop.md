---
html: stop.html
parent: server-control-methods.html
blurb: サーバーのグレースフルシャットダウンを行います。
labels:
  - コアサーバー
---
# stop
[[ソース]](https://github.com/XRPLF/rippled/blob/master/src/ripple/rpc/handlers/Stop.cpp "Source")

サーバーのグレースフルシャットダウンを行います。

_`stop`リクエストは、権限のないユーザーは実行できない*[管理メソッド](admin-api-methods.html)です。_

### リクエストのフォーマット
リクエストのフォーマットの例:

<!-- MULTICODE_BLOCK_START -->

*WebSocket*

```json
{
   "id": 0,
   "command": "stop"
}
```

*JSON-RPC*

```json
{
   "method": "stop",
   "params": [
       {}
   ]
}
```

*コマンドライン*

```
rippled stop
```

<!-- MULTICODE_BLOCK_END -->

リクエストにはパラメーターが含まれていません。

### レスポンスのフォーマット

処理が成功したレスポンスの例:

<!-- MULTICODE_BLOCK_START -->

*JSON-RPC*

```json
{
  "result" : {
     "message" : "ripple server stopping",
     "status" : "success"
  }
}
```

*コマンドライン*

```json
Loading: "/etc/rippled.cfg"
Connecting to 127.0.0.1:5005

{
  "result" : {
     "message" : "ripple server stopping",
     "status" : "success"
  }
}
```

<!-- MULTICODE_BLOCK_END -->

レスポンスは[標準フォーマット][]に従っており、正常に完了した場合は結果に次のフィールドが含まれています。

| `Field`   | 型   | 説明                          |
|:----------|:-------|:-------------------------------------|
| `message` | 文字列 | `ripple server stopping` : 正常終了の場合。 |

### 考えられるエラー

* [汎用エラータイプ][]のすべて。

<!--{# common link defs #}-->
{% include '_snippets/rippled-api-links.md' %}
{% include '_snippets/tx-type-links.md' %}
{% include '_snippets/rippled_versions.md' %}
