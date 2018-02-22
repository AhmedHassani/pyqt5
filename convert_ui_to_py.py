from PyQt5 import uic
fin = open('shop_activity.ui','r')
fout = open('shop_activiy.py','w')
uic.compileUi(fin,fout,execute=False)
fin.close()
fout.close()