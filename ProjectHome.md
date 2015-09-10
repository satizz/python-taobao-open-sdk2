大家好，我是duma 。<br>
我是个python爱好者。<br>
我要贡献出自己封装好的 taobao api ，目前只针对OPEN 2.0 版本。<br>
下面我来简单介绍使用方法 ：<br><br>
普通用法:<br>
<pre><code>from taobaoapi2 imoprt *<br>
<br>
itemsget = ItemsGet()<br>
itemsget.setParams(nicks='etanliuyang')<br>
itemsget.fetch()<br>
for x in itemsget.datas:<br>
  print x['title']<br>
</code></pre>

错误信息处理：<br>
<pre><code>from taobaoapi2 imoprt *<br>
<br>
itemsget = ItemsGet()<br>
itemsget.setParams(nicks='v')<br>
itemsget.fetch()<br>
if itemsget.error_msg: print itemsget.error_msg<br>
</code></pre>
下载:<br>

svn checkout <a href='http://python-taobao-open-sdk2.googlecode.com/svn/trunk/'>http://python-taobao-open-sdk2.googlecode.com/svn/trunk/</a> python-taobao-open-sdk2-read-only