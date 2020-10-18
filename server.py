from concurrent import futures
import logging

import grpc

import api_pb2
import api_pb2_grpc

import RPi.GPIO as GPIO
import time
pins = [36, 38, 40]
# Remove warning message
GPIO.setwarnings(False)
# Remove warning message
GPIO.setmode(GPIO.BOARD)

for i in pins:
    GPIO.setup(i, GPIO.OUT)

# Remove warning message
pwmR = GPIO.PWM(pins[0], 70)
pwmG = GPIO.PWM(pins[1], 70)
pwmB = GPIO.PWM(pins[2], 70)

# Enable PWM
pwmR.start(0)
pwmG.start(0)
pwmB.start(0)

class Tester(api_pb2_grpc.TesterServicer):

    def Test(self, request, context):
        pwmR.ChangeDutyCycle(100)
        pwmG.ChangeDutyCycle(0)
        pwmB.ChangeDutyCycle(0)

        time.sleep(3)
        

        pwmR.ChangeDutyCycle(0)
        pwmG.ChangeDutyCycle(0)
        pwmB.ChangeDutyCycle(0)
        return api_pb2.TestReply(message='Value: %s!' % request.value)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    api_pb2_grpc.add_TesterServicer_to_server(Tester(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()