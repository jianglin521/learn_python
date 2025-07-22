# -*- coding: utf-8 -*-
from flask import Flask, Response, render_template, send_file, send_from_directory,json, jsonify, make_response
app = Flask(__name__)  #实例化flask app

#file_name是客户端传来的需要下载的文件名
@app.route('/get_file/<file_name>', methods=['get'])
def get_file(file_name):
    directory = './'
    print(file_name, '00000000000')
    try:
        def send_chunk():  # 流式读取
            store_path = './day09/专题数据1-44.xlsx'
            with open(store_path, 'rb') as target_file:
                while True:
                    chunk = target_file.read(20 * 1024 * 1024)  # 每次读取20M
                    if not chunk:
                        break
                    yield chunk
        return Response(send_chunk(), content_type='application/rar')
        # response = make_response(
        #     send_from_directory(directory, '02.rar', as_attachment=False))
        # return response
    except Exception as e:
        return jsonify({"code": "异常", "message": "{}".format(e)})
 
if __name__ == '__main__':
    app.run(host='172.18.1.198', port=5000,debug=True)