import socket
import base64
# import picamera
# import time

#def take_picture():
# 	camera = picamera.PiCamera()
# 	now = time.gmtime()
# 	strNow = str(now[0])+"-"+str(now[1])+"-"+str(now[2])+"-"+str(now[3])+"-"+str(now[4])+"-"+str(now[5])
# 	fileName = strNow+".jpeg"
# 	camera.capture(fileName)
# 	return fileName

server_host = "138.51.58.186"
server_port = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((server_host, server_port))
print ('server bound to ' + server_host + ':' + str(server_port))
server.listen(10)

while(1):
	(clientsocket, address) = server.accept()
	print("client connected from " + str(address))
	# print('Accepted new connection')
	# file_name = take_picture(clientsocket, address)
	file_name = 'test.jpg'
	picture = open(file_name,'rb')
	#print('image data being sent: ' + str(base64.b64encode(picture.read())))
	with picture as image_file:
	    to_send = base64.b64encode(image_file.read())
	    data_size = len(to_send)
	# to_send = picture.read()
	while()
	clientsocket.send(to_send)
	clientsocket.close()
