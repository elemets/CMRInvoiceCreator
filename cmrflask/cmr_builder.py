from reportlab.pdfgen import canvas
from flask import url_for
from reportlab.platypus import Paragraph, Frame, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch, cm
from cmrflask.reportlabfunc import fill_page_with_image
from pdfrw.toreportlab import makerl
import sys
import os
from reportlab.pdfgen.canvas import Canvas
from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from datetime import datetime
import time
from pdfrw.toreportlab import makerl


def read_and_double(inpfn):
    pages = PdfReader(inpfn).pages
    pages = [pagexobj(x) for x in pages]
    if len(pages) & 1:
        pages.append(pages[0])  # Sentinel -- get same size for back as front

    xobjs = []
    while len(pages) > 2:
        xobjs.append((pages.pop(), pages.pop(0)))
        xobjs.append((pages.pop(0), pages.pop()))
    xobjs += [(x,) for x in pages]
    return xobjs


def make_pdf(outfn, xobjpairs):
    c = canvas.Canvas(outfn)
    for xobjlist in xobjpairs:
        x = y = 0
        for xobj in xobjlist:
            x += xobj.BBox[2]
            y = max(y, xobj.BBox[3])

        c.setPageSize((x, y))

        # Handle blank back page
        if len(xobjlist) > 1 and xobjlist[0] == xobjlist[-1]:
            xobjlist = xobjlist[:1]
            x = xobjlist[0].BBox[2]
        else:
            x = 0
        y = 0

        for xobj in xobjlist:
            c.saveState() 
            c.translate(x, y)
            c.doForm(makerl(c, xobj))
            c.restoreState()
            x += xobj.BBox[2]
    return c

def draw_text_in_boxes(positionX, positionY, max_num_lines, texttowrite, canvas):
    
    textobject = canvas.beginText(positionX *cm, positionY *cm)
    textobject.setFont('Times-Roman', 8)
    
    textsplit = texttowrite.splitlines(False)
    
    if len(textsplit) > max_num_lines:
        for line in range(0, len(textsplit), 2):
                textobject.textLine((textsplit[line] + "      " + textsplit[line + 1]).rstrip() )
    else:
        for line in texttowrite.splitlines(False):
            textobject.textLine(line.rstrip())
            
            
    canvas.drawText(textobject)



def drawCMR(data):
    try:
        
        pdf = "cmr-form.pdf"
        
        c = make_pdf(pdf, read_and_double("./cmrflask/static/cmrpdf-min.pdf"))
        
        sender = data['sender']
        
        c.setFont('Times-Roman', 8)
        
        draw_text_in_boxes(1, 27.5, 7, sender, c)
        
        draw_text_in_boxes(1, 24, 7, data['consignee'], c)
        
        print(data)
        
        draw_text_in_boxes(1, 20.5, 7, data['place_of_delivery'], c)

        date_of_goods = data['date_of_goods_take_over'].strftime("%d/%m/%Y")


        draw_text_in_boxes(1, 17, 7, data['place_of_goods_take_over'], c)
        draw_text_in_boxes(1, 16.5, 7, date_of_goods, c)
        
        draw_text_in_boxes(1, 14.8, 7, data['annexed_documents'], c)
        
        
        draw_text_in_boxes(10.6, 24, 7, data['carrier'], c)
        
        draw_text_in_boxes(10.6, 20.5, 7, data['successive_carriers'], c)
        
        #c.drawString(300, 480, str(data['carriers_reservation']))
        
        draw_text_in_boxes(10.6, 17.5, 7, str(data['carriers_reservation']))
        
        # c.drawString(8, 10, "YOOOO")
        gross_table_list = []

        print("list of items")
        for item in data.items():
            if 'gross_weight' in item[0] or 'volume_goods' in item[0] or 'statistical_number' in item[0] or 'marks_numbers' in item[0] or 'number_packages' in item[0] or 'method_packing' in item[0] or 'nature_goods' in item[0] or 'total_gross_volume' in item[0]:
                gross_table_list.append(item[1])

        print(gross_table_list)
        
        ### drawing the box table marks and numbers
        for items in range(0, len(gross_table_list)):
            if items < 8:
                c.drawString(22, 350 - (items * 10), gross_table_list[items])
            elif 7 < items < 16:
                c.drawString(72, 350 - ((items - 8) * 10), str(gross_table_list[items]))
            elif 15 < items < 24:
                c.drawString(117, 350 - ((items - 16) * 10), str(gross_table_list[items]))
            elif 23 < items < 32:
                c.drawString(165, 350 - ((items - 24) * 10), str(gross_table_list[items]))
            elif 31 < items < 40:
                c.drawString(355, 350 - ((items - 32) * 10), str(gross_table_list[items]))
            elif 39 < items < 49:
                c.drawString(430, 350 - ((items - 40) * 10), str(gross_table_list[items]))
            else:
                c.drawString(500, 350 - ((items - 49) * 10), str(gross_table_list[items]))

        # drawing the letter number etc
        c.drawString(60, 268, data['classe'])
        c.drawString(160, 268, data['number'])
        c.drawString(250, 268, data['letter'])
        c.drawString(300, 268, data['ADR'])

        draw_text_in_boxes(1, 8.2, 7, data['sender_instructions'], c)
        draw_text_in_boxes(10.6, 8.2, 3, data['special_agreements'], c)
        
        draw_text_in_boxes(1, 8.2, 7, data['sender_instructions'], c)

        c.save()
        
    except:
        return "Data needs to be passed"


