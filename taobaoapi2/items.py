#coding=utf8

from base import TaoBao

#搜索商品信息
class ItemsGet(TaoBao):
    data_name = 'items'
    data_type = 'item'
    method = 'items.get'
    fields = 'iid,title,nick,pic_url,cid,price,type,delist_time,post_fee,score,volume,location.city,location.state'


