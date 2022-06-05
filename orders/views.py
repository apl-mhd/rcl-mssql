from decimal import Decimal
from urllib import response
from django.shortcuts import render
from . models import ORDER_DETAILS, ORDER_MASTER, RETURN_REQ_DETAILS, RETURN_REQ_MASTER
from products.models import PRODUCT_MASTER
from orders.serializers import OrderSerializer
from users.models import Customer_Detail
from django.http import HttpResponse
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
import xml.etree.ElementTree as ET
import xmltodict
from django.db import connections
from django.views.decorators.csrf import csrf_exempt

@api_view(['GET', 'POST'])
@csrf_exempt
def sales_return(request, order_id):
    if request.method == 'POST':
        customer_id = request.data['customer']['shop_id']
        return_no = RETURN_REQ_MASTER.objects.all().last().RETURN_NO + 1
        return_req_master = RETURN_REQ_MASTER.objects.create(
            RETURN_NO = return_no,
            ORDER_NO = order_id,
            CUSTOMER_ID = customer_id,
            TOTAL_AMOUNT = 10
        )
        total_amount = 0
        for i in request.data['products']:
          total_amount += float(i['RATE']) * float(i['QTY'])
         
          RETURN_REQ_DETAILS.objects.create(
            RETURN_NO = return_req_master.RETURN_NO,
            PROD_CODE = i['PROD_CODE'],
            RATE = i['RATE'],
            QTY = i['QTY'],
            ITEM_PRICE = float(i['RATE']) * float(i['QTY'])
            )
        #print(total_amount, '-------')
        RETURN_REQ_MASTER.objects.filter(RETURN_NO=return_req_master.RETURN_NO).update(TOTAL_AMOUNT = total_amount)
        print(return_req_master.RETURN_NO)
        return Response({'details': 'sales return success'})
    else:
        return Response({'details': 'POST method allowed only'})



@api_view(['GET', 'POST'])
@csrf_exempt
def order_update(request, order_no):
    if request.method == 'POST':
        ORDER_DETAILS.objects.filter(ORDER_NO= order_no).delete()
        json_data = json.loads(request.body)
        for i in json_data['products']:
            ORDER_DETAILS.objects.create(
                ORDER_NO = order_no,
                PROD_CODE = i['PROD_CODE'],
                RATE = i['RATE'],
                QTY = i['QTY'],
                ITEM_PRICE = float(i['RATE']) * float(i['QTY'])
                )
        return Response(json_data)
        #return Response({'details': 'delete success'})

    return Response({'details': 'POST method allowed only'})
    


@api_view(['GET', 'POST'])
@csrf_exempt
def customer_all_order(request, customer_id):
     if request.method == 'GET':
        final_output = []
        sol_data = {}
        sales_orders = ORDER_MASTER.objects.filter(CUSTOMER_ID=customer_id)
        for so in sales_orders:
            sale_order_data = {
                'ORDER_NO': so.ORDER_NO,
                'CUSTOMER_ID': so.CUSTOMER_ID,
                'STATUS': so.STATUS,
                'LATITUDE': so.LATITUDE,
                'LOGITUDE': so.LOGITUDE,
                'USER_ID': so.USER_ID,
                'ORDERDETAILS':120,
                'DOT': so.DOT,
             }
            sale_order_line = ORDER_DETAILS.objects.filter(ORDER_NO = so.ORDER_NO)
            print(sale_order_line)
            soline = []
            for sol in sale_order_line:
                sale_order_line_data = {
                    'ORDER_TRANSAC_SL': sol.ORDER_TRANSAC_SL,
                    'PROD_CODE': sol.PROD_CODE,
                    'RATE': sol.RATE,
                    'QTY': sol.QTY,
                    'ITEM_PRICE': sol.ITEM_PRICE
                    
                }
                soline.append(sale_order_line_data)
            so_id = str(so.ORDER_NO)
            sol_data['sale_order'] = sale_order_data
            sol_data['ORDER_DETAILS'] = soline
            final_output.append({so_id: sol_data})
            sol_data = {}
        return Response(final_output)


@api_view(['GET', 'POST'])
@csrf_exempt
def customer_single_order(request, order_no):
     if request.method == 'GET':
        final_output = []
        sol_data = {}
        sales_orders = ORDER_MASTER.objects.filter(ORDER_NO=order_no)
        for so in sales_orders:
            sale_order_data = {
                'ORDER_NO': so.ORDER_NO,
                'CUSTOMER_ID': so.CUSTOMER_ID,
                'STATUS': so.STATUS,
                'LATITUDE': so.LATITUDE,
                'LOGITUDE': so.LOGITUDE,
                'USER_ID': so.USER_ID,
                'ORDERDETAILS':120,
                'DOT': so.DOT,
             }
            sale_order_line = ORDER_DETAILS.objects.filter(ORDER_NO = so.ORDER_NO)
            print(sale_order_line)
            soline = []
            for sol in sale_order_line:
                sale_order_line_data = {
                    'ORDER_TRANSAC_SL': sol.ORDER_TRANSAC_SL,
                    'PROD_CODE': sol.PROD_CODE,
                    'RATE': sol.RATE,
                    'QTY': sol.QTY,
                    'ITEM_PRICE': sol.ITEM_PRICE
                    
                }
                soline.append(sale_order_line_data)
            so_id = str(so.ORDER_NO)
            sol_data['sale_order'] = sale_order_data
            sol_data['ORDER_DETAILS'] = soline
            final_output.append({so_id: sol_data})
            sol_data = {}
        return Response(final_output)


@api_view(['GET', 'POST'])
@csrf_exempt
def order(request):
    if request.method == 'POST':
      json_data = json.loads(request.body)
      customer_id = json_data['sale_order']['CUSTOMER_ID']
      last_order_no = ORDER_MASTER.objects.last().ORDER_NO +1

      order_master = ORDER_MASTER.objects.create(
          ORDER_NO= last_order_no,
          CUSTOMER_ID=customer_id,
          USER_ID = 1
          )
      total_amount = 0
      for i in json_data['ORDER_DETAILS']:
          total_amount += float(i['RATE']) * float(i['QTY'])
          ORDER_DETAILS.objects.create(
            ORDER_NO = order_master.ORDER_NO,
            PROD_CODE = i['PROD_CODE'],
            RATE = i['RATE'],
            QTY = i['QTY'],
            ITEM_PRICE =total_amount #float(i['RATE']) * float(i['QTY'])
            )
      print(total_amount)
      ORDER_MASTER.objects.filter(ORDER_NO=order_master.ORDER_NO).update(TOTAL_AMOUNT = total_amount)
      return Response({'details': 'success'})

    
       
    if request.method == 'GET':
        final_output = []
        sol_data = {}
        sales_orders = ORDER_MASTER.objects.all()
        details = ORDER_DETAILS.objects.all()
        #print(details)
        for so in sales_orders:
            sale_order_data = {
                'ORDER_NO': so.ORDER_NO,
                'CUSTOMER_ID': so.CUSTOMER_ID,
                'STATUS': so.STATUS,
                'LATITUDE': so.LATITUDE,
                'LOGITUDE': so.LOGITUDE,
                'USER_ID': so.USER_ID,
                'ORDERDETAILS':120,
                'DOT': so.DOT,
             }
            sale_order_line = ORDER_DETAILS.objects.filter(ORDER_NO = so.ORDER_NO)
            print(sale_order_line)
            soline = []
            for sol in sale_order_line:
                sale_order_line_data = {
                    'ORDER_TRANSAC_SL': sol.ORDER_TRANSAC_SL,
                    'PROD_CODE': sol.PROD_CODE,
                    'RATE': sol.RATE,
                    'QTY': sol.QTY,
                    'ITEM_PRICE': sol.ITEM_PRICE
                    
                }
                soline.append(sale_order_line_data)
            so_id = str(so.ORDER_NO)
            sol_data['sale_order'] = sale_order_data
            sol_data['ORDER_DETAILS'] = soline
            final_output.append({so_id: sol_data})
            sol_data = {}
        return Response(final_output)


def cursor_test(request):
    cursor = connections['default'].cursor()
    a = cursor.execute("SELECT * FROM ORDER_MASTER WHERE ORDER_NO = %s", [1])
    for i in a:
        print(i.ORDER_NO)
    return HttpResponse('test cursor')



@api_view(['GET', 'POST'])
def order_master(request):

    # a = ORDER_MASTER(ORDER_NO=18)
    # a.save()
    # print(a)
    if request.method == 'GET':
        print('')
        # CUSTOMER_ID=1,
        #      LATITUDE=1, 
        #      LOGITUDE=1,
        #      USER_ID=1,
        #      ORDERDETAILS='1'
        # cursor = connections['default'].cursor()
        # cursor.execute("INSERT INTO ORDER_MASTER(ORDER_NO) VALUES( 13  )")
        # order_masters = ORDER_MASTER.objects.all()
        # print(order_masters)
        # return Response('success')

       
        # order_master_create = ORDER_MASTER.objects.create(
        #     ORDER_NO= '14',
        #     )
        # print(order_master_create)
        
        # order_masters = ORDER_MASTER.objects.all() #.order_by('-ORDER_NO')
        # serializer = OrderSerializer(data=order_masters, many=True)
        # if serializer.is_valid():
        #     print('aaaaaaaaaaaa')
        # else:
        #     return Response(serializer.errors)
    return Response('a')



    
    # if request.method=='POST':
    #     sales = eval(request.body)
    #     customer = sales['customer']

    #     # status = customer['status']

    #     # print("gggg")

    #     so = SaleOrder.objects.create(
    #         customer_id_id = customer_id,
    #         customer_name = customer_name,
    #         customer_contact=  customer_contact,
    #         shop_name = shop_name,
    #         shop_id = shop_id,
    #         shop_location = shop_location,
    #         invoice_amount = invoice_amount,
    #         sr_id_id = sr_id,
    #         sr_name = sr_name,
    #     )

    #     so_id = so.id

    #     # print(so_id)
    #     for sol in sale_order_line:
    #         # print(sol)
    #         SaleOrderLine.objects.create(
    #             customer_id_id = customer_id,
    #             customer_name = customer_name,
    #             shop_id = shop_id,
    #             shop_name = shop_name,
    #             product_id_id = sol['id'],
    #             product_name = sol['product_name'],
    #             quantity = sol['quantity'],
    #             unit_price = sol['unit_price'],
    #             discount_percent = sol['discount_percent'],
    #             price_with_discount = sol['price_with_discount'],
    #             order_id_id = so_id,
    #         )

    #     return HttpResponse(json.dumps({"success":"done"}))




   # customer = Customer_Detail.objects.get(CUSTOMER_ID=1)
    #order_master = ORDER_MASTER.objects.create( CUSTOMER_ID_id=1, USER_ID=1)
    #product = PRODUCT_MASTER.objects.all()
    #print(product)




    # rate = 5
    # qty = 3

    # order_line = ORDER_DETAILS.objects.create(
    #     ORDER_NO=1,
    #     RATE=rate, QTY=qty,
    #     ITEM_PRICE=rate*qty
    #     )

    return HttpResponse('Apel Mahmud')


@api_view(['GET', 'POST'])
def product(request):
    response = requests.get('https://api.rcl-group.net/api/rcl_api.ashx?method=GETPRODUCTLIST')
    tree = ET.fromstring(response.content)
    xpars = xmltodict.parse(response.text)
    print(response.text)
    json_data = json.dumps(xpars)
    print(json_data)
    return HttpResponse(json_data)
