import zlib, base64

data = open('py_compression\demo_compressed.txt','r').read()
bytes_data = bytes(data,'utf-8')
decompressed_data = zlib.decompress(base64.b64decode(bytes_data))
decoded_data = decompressed_data.decode('utf-8')
decompressed_file = open('py_compression\demo_decompressed.txt','w')
decompressed_file.write(decoded_data)