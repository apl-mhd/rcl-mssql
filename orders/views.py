import django
from django.shortcuts import render
from . models import ORDER_DETAILS, ORDER_MASTER
from products.models import PRODUCT_MASTER
from users.models import Customer_Detail
from django.http import HttpResponse
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def create_order(request):

    # if request.method == 'GET':
    #     sale_orders = ORDER_MASTER.objects.all()
       
    if request.method == 'GET':
        final_output = []
        sol_data = {}
        sales_orders = ORDER_MASTER.objects.all()
        for so in sales_orders:
            sale_order_data = {
                'ORDER_NO': so.ORDER_NO,
                'CUSTOMER_ID': so.CUSTOMER_ID_id,
                'STATUS': so.STATUS,
                'LATITUDE': so.LATITUDE,
                'LOGITUDE': so.LOGITUDE,
                'USER_ID': so.USER_ID,
                'ORDERDETAILS':120,
                'DOT': so.DOT,
            }
            sale_order_line = ORDER_DETAILS.objects.filter(ORDER_NO = so.ORDER_NO)
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




