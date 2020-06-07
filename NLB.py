def get_route():
    import urllib.request as request
    import json
    src='https://rt.data.gov.hk/v1/transport/nlb/route.php?action=list'
    with request.urlopen(src) as response:
        data=json.load(response)
    clist=data["routes"]
    for routes in clist:
        if routes["overnightRoute"]==1:
            ONR="(夜間巴士路線)"
        else:
            ONR=""
        if routes["specialRoute"]==1:
            SP="(特別路線)"
        else:
            SP=""            
        print('RouteID:'+routes["routeId"]+' 路線:'+routes["routeNo"]+' '+routes["routeName_c"]+' '+ONR+' '+SP)


while True:
    print("""1.路線 (Get list of all routes)
2.路線的車站 (Get list of stops of a route) 
3.巴士預計抵站時間 (Get ETA of a stop of a route)
4.離開
""")
    print()
    choice=input("請輸入查詢的選項 :")
    print()
    if choice=="1":
        get_route()
        input()
    elif choice=="2":
        routeId=input("請輸入RouteID :")
        get_stop(routeId)
        input()
    elif choice=="3":
        routeId=input("請輸入RouteID :")
        stop_id=input("請輸入巴士站編號 :")
        get_stopETA(routeId,stop_id)
        input()
    elif choice=="4":
        exit()
    else:
        print("輸入錯誤，請重新輸入")
        input()