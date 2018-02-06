import pika
import json #python self-provided

class CloudAMQPClient:
    def __init__(self, cloud_amqp_url, queue_name):
        self.cloud_amqp_url = cloud_amqp_url
        self.queue_name = queue_name

        self.param = pika.URLParameters(cloud_amqp_url)  #The more queue, the more amqp instance needed
        self.param.socket_timeout = 3   #CloudAMQP need to be mannually closed
        self.connection = pika.BlockingConnection(self.param)

        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=queue_name) #Only init when it does not exist

    def sendMessage(self, message):
        self.channel.basic_publish(exchange='', routing_key=self.queue_name, body=json.dumps(message))#dumps: serialization
        print ("[Test] send to %s: %s" % (self.queue_name, message))
        return

    def getMessage(self):
        method_frame, header_frame, body = self.channel.basic_get(self.queue_name)
        if method_frame:
            print ("[Test] receive from %s: %s" % (self.queue_name, body))
            self.channel.basic_ack(method_frame.delivery_tag) #Send acknowledge to server to allow server delete correconding msg  *Important to avoid duplicate
            return json.loads(body)
        else:
            print ('No message returned')
            return None

    #define a sleep method to avoid keep scraping too fast.
    #Don't use threading(python provided) - connection to CloudAMQP will be disconnect (heart beat test fail)
    def sleep(self, seconds):
        self.connection.sleep(seconds)
