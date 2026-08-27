# -*- coding: utf-8 -*-
from rest_framework.views import APIView
from ..Models.ConnectToDBModel import *
from ..Models.RegionInfoModel import *
from .CommonView import *



def get_one_spot(region):

        comments_data = get_comment_data();

        data = {};
        data['id'] = region.id;
        data['name'] = region.name;
        data['address'] = region.address;
        data['lng'] = region.lng;
        data['lat'] = region.lat;
        spot_comment_data = comments_data[(comments_data['search_key'] == str(region.search_key))]
        data['commentNumber'] =   spot_comment_data.iloc[:, 0].size;
        data['commentScore'] = get_score(spot_comment_data['comment_score'].mean());
        return data;
def get_spot_list(request):
   #进行解码token
    # username = decodeToken(request);
    # print(username);
    res = {};
    try:

        list = [get_one_spot(region) for region in regioninfo.objects];
       # 返回所有的文档对象列表
        res['list'] = list;
        return json_response(res);
    except Exception:
        return json_error(error_string='查询发生错误',code = 12,api = "spotlist");



class SpotListView(APIView):

    def get(self, request, *args, **kwargs):
        try:

            return get_spot_list(request);
        except KeyError:
            return json_error(error_string="请求错误", code=500);
