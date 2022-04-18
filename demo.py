#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hbh112233abc@163.com'

import os
from ofd_parser import OfdParser

ofd_file = os.path.join(os.path.dirname(__file__),'tests','files','00101.ofd')

ofd = OfdParser(ofd_file)
print('Versions: {}\nDocType: {}'.format(ofd.OFD.get_Version(), ofd.OFD.get_DocType()))

print(' '*10 + '---Parsing Document.xml---')
print(('MaxUnitID: {}').format(ofd.Document.get_CommonData().get_MaxUnitId()))
print('Length of Pages: {}'.format(ofd.Document.get_Pages().__len__()))


#Pages
print('-' * 46)
print(' '*10 + '---Parsing Pages---')
for n,page in enumerate(ofd.Pages,1):
    page_N = page.get_PageN()
    page_res = None if page_N.get_select_PageRes() == '' else page_N.get_select_PageRes()
    print(f"Pages {n} {' '*4} PageID: {page.get_PageID()} {' '*4} PageRes: {page_res}")
    texts = page_N.get_select_Content().get_Layer().get_PageBlock().get_TextObject()
    for text in texts:
        print(text.get_TextCode().get_TextValue())

#Res
print('-' * 46)
print(' '*10 + '---Parsing PublicRes---')
try:
    for i in range(len(ofd.PublicRes.get_Fonts())):
        print(('ID: {}' + ' '*4 + 'FontName: {}' + ' '*4 +'FamilyName: {}' + ' '*4 + 'FontFile: {}').format(\
            ofd.PublicRes.get_Fonts()[i].get_ID(), ofd.PublicRes.get_Fonts()[i].get_FontName(),\
                ofd.PublicRes.get_Fonts()[i].get_select_FamilyName(), ofd.PublicRes.get_Fonts()[i].get_select_FontFile()))
except:
    print('No PublicRes')
print('-' * 46)
print(' '*10 + '---Parsing DocumentRes---')
try:
    for i in range(len(ofd.DocumentRes.get_MultiMedias())):
        print(('ID: {}' + ' '*4 + 'Type: {}' +' '*4 + 'MediaFile: {}' + ' '*4 + 'Format: {}').format(\
            ofd.DocumentRes.get_MultiMedias()[i].get_ID(), ofd.DocumentRes.get_MultiMedias()[i].get_Type(),\
                ofd.DocumentRes.get_MultiMedias()[i].get_MediaFile(), ofd.DocumentRes.get_MultiMedias()[i].get_select_Format()))
except:
    print('No DocumentRes')
