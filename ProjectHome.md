大家好，我是duma 。<br>
我是个python爱好者。<br>
我要贡献出自己封装好的 taobao api ，目前只针对OPEN 2.0 版本。<br>
下面我来简单介绍使用方法 ：<br><br>
普通用法:<br>
<pre><code>from taobaoapi2 imoprt *

itemsget = ItemsGet()
itemsget.setParams(nicks='etanliuyang')
itemsget.fetch()
for x in itemsget.datas:
  print x['title']
</code></pre>

错误信息处理：<br>
<pre><code>from taobaoapi2 imoprt *

itemsget = ItemsGet()
itemsget.setParams(nicks='v')
itemsget.fetch()
if itemsget.error_msg: print itemsget.error_msg
</code></pre>
下载:<br>

svn checkout <a href='http://python-taobao-open-sdk2.googlecode.com/svn/trunk/'>http://python-taobao-open-sdk2.googlecode.com/svn/trunk/</a> python-taobao-open-sdk2-read-only