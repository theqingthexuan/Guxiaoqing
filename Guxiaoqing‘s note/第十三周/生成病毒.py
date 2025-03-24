# -*- coding:UTF-8 -*-
import pyclamd
cd = pyclamd.ClamdNetworkSocket('127.0.0.1', 3310)
#通过EICAR()方法生成一个带有病毒特征的文件/tmp/EICAR，编译测试
void = open('D:/test/EICAR', 'wb').write(cd.EICAR())