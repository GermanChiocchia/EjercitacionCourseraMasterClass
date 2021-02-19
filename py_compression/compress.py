import zlib, base64

data = open('py_compression\demo.txt','r').read()
bytes_data = bytes(data,'utf-8')
compressed_data = base64.b64encode(zlib.compress(bytes_data,9))
decoded_data = compressed_data.decode('utf-8')
compressed_file = open('py_compression\demo_compressed.txt','w')
compressed_file.write(decoded_data)