from socket import *
serverName = '127.0.0.1'
serverPort = 6000
b = 1024

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

question1 = clientSocket.recv(b)
print('Question 1: ')
print(question1.decode())
answer1 = input('Answer: ')
clientSocket.send(answer1.encode())

question2 = clientSocket.recv(b)
print('Question 2: ')
print(question2.decode())
answer2 = input('Answer: ')
clientSocket.send(answer2.encode())

question3 = clientSocket.recv(b)
print('Question 3: ')
print(question3.decode())
answer3 = input('Answer: ')
clientSocket.send(answer3.encode())

question4 = clientSocket.recv(b)
print('Question 4: ')
print(question4.decode())
answer4 = input('Answer: ')
clientSocket.send(answer4.encode())

question5 = clientSocket.recv(b)
print('Question 5: ')
print(question5.decode())
answer5 = input('Answer: ')
clientSocket.send(answer5.encode())

question6 = clientSocket.recv(b)
print('Question 6: ')
print(question6.decode())
answer6 = input('Answer: ')
clientSocket.send(answer6.encode())

question7 = clientSocket.recv(b)
print('Question 7: ')
print(question7.decode())
answer7 = input('Answer: ')
clientSocket.send(answer7.encode())

question8 = clientSocket.recv(b)
print('Question 8: ')
print(question8.decode())
answer8 = input('Answer: ')
clientSocket.send(answer8.encode())

question9 = clientSocket.recv(b)
print('Question 9: ')
print(question9.decode())
answer9 = input('Answer: ')
clientSocket.send(answer9.encode())

question10 = clientSocket.recv(b)
print('Question 10: ')
print(question10.decode())
answer10 = input('Answer: ')
clientSocket.send(answer10.encode())

count = clientSocket.recv(b)
print('\nSCORE: ' + count.decode() + '\n')
clientSocket.close()

# from socket import *
# serverName = '127.0.0.1'
# serverPort = 12000
# clientSocket = socket(AF_INET, SOCK_STREAM)
# clientSocket.connect((serverName,serverPort))
# sentence = input('Input lowercase sentence:')
# clientSocket.send(sentence.encode())
# modifiedSentence = clientSocket.recv(1024)
# print ('From Server:', modifiedSentence.decode())
# clientSocket.close()