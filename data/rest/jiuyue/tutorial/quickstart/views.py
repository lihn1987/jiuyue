from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from django.db import connection
# Create your views here.
def test(request):
    a = {
        "a":"bbbb"
    }
    return JsonResponse(a)

def img(request, path):
    print("???????????")
    print(img)
    rtn = []
    sql = """
    """
    with open(path, 'rb') as f:
        image_data = f.read()
    return HttpResponse(image_data, content_type="image/png")
            
def get_type1_list(request):
    # rtn = {
    #     "result": 0,
    #     "data":[]
    # }
    # sql = """
    #     select 
    #         `name`
    #     from 
    #         quickstart_type1
    #     order by `index`,id
    # """
    # with connection.cursor() as cursor:
    #     cursor.execute(sql)
    #     rtn["data"] = cursor.fetchall()
    # return JsonResponse(rtn)
    rtn = {
        "result":0,
        "data":[]
    }
    sql = """
    select 
        quickstart_type1.id as type_id,
        quickstart_type1.name as type_name,
        quickstart_detail.name as detail_name,
        quickstart_detail.logo,
        quickstart_detail.`desc`,
        quickstart_detail.`url`
    from 
        quickstart_type1, 
        quickstart_detail
    where 
        quickstart_type1.id = quickstart_detail.type_id
        order by quickstart_type1.index, quickstart_type1.id, quickstart_detail.index,quickstart_detail.id
    """

    with connection.cursor() as cursor:
        cursor.execute(sql)
    lines = cursor.fetchall()
    last_type_id = None
    for line in lines:
        if line[0] != last_type_id:
            last_type_id = line[0] 
            rtn["data"].append({
                'id': line[0],
                'name': line[1],
                'list':[]
            })
        rtn["data"][len(rtn["data"])-1]["list"].append({
            'name': line[2],
            'logo': line[3],
            'desc': line[4],
            'url': line[5] 
        })
    
    return JsonResponse(rtn)