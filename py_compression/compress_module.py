import zlib, base64

def compress(input_file,output_file):
    data = open(input_file,'r').read()
    bytes_data = bytes(data,'utf-8')
    compressed_data = base64.b64encode(zlib.compress(bytes_data,9))
    decoded_data = compressed_data.decode('utf-8')
    compressed_file = open(output_file,'w')
    compressed_file.write(decoded_data)

def decompress(input_file,output_file):
    data = open(input_file,'r').read()
    bytes_data = bytes(data,'utf-8')
    decompressed_data = zlib.decompress(base64.b64decode(bytes_data))
    decoded_data = decompressed_data.decode('utf-8')
    decompressed_file = open(output_file,'w')
    decompressed_file.write(decoded_data)