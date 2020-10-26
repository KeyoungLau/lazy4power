# 腾讯优图云的OCR识别
# https://open.youtu.qq.com/#/open
# 腾讯优图云的sdk要去github上下载，需要Requests库
# https://github.com/TencentYouTu/python_sdk
# 安装教程：https://www.cnblogs.com/aliceboy/p/9895613.html
import TencentYoutuyun
from pprint import pprint

appid = '10244796'
secret_id = 'AKID3ylUB1zNtGSZnxtlPvNk4KgME1hBFfBb'
secret_key = 'Tp5DAzhIi07A3oNqEVedYKyRjtRs9JH5'
userid = '810366639'  # userid填个QQ号就可以了

# 这里主要演示身份证的识别
# 其他识别可以慢慢去探索
end_point = TencentYoutuyun.conf.API_YOUTU_END_POINT  # 优图开放平台
youtu = TencentYoutuyun.YouTu(appid, secret_id, secret_key, userid, end_point)
file_path = r"C:\Users\Keyou\Desktop\idcard.jpg"
result = youtu.idcardocr(file_path, card_type=2)
for k, v in result.items():
    if isinstance(v, str):
        print(k.encode('iso8859-1').decode('utf-8') + ":" + v.encode('iso8859-1').decode('utf-8'))  # 注意编码和解码
    else:
        pass
        #print(v)
