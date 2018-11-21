# slackbot-test
研究室のゴミ捨て担当者通知用slackbot 

# 定期的に通知
- 以下のスクリプトを用いて, Google App Scriptから定期実行する
- メッセージに基づきgarbage-notification botが発火

```ruby:qiita.rb
var postUrl = 'Incoming WebhooksのURL';
var username = 'trigger-bot';
var message = '@garbage-notification 今月のゴミ';  // 投稿メッセージ

function myFunction() {
  var jsonData =
  {
     "username" : username,
     "text" : message,
     "link_names": 1
  };
  var payload = JSON.stringify(jsonData);

  var options =
  {
    "method" : "post",
    "contentType" : "application/json",
    "payload" : payload
  };

  UrlFetchApp.fetch(postUrl, options);
}
```
