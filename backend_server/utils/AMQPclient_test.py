from AMQPclient import CloudAMQPClient

CLOUDAMQP_URL = "amqp://wirxetlw:FMdNgb83vuRko1L-PIS9pMrkClqHCmnt@llama.rmq.cloudamqp.com/wirxetlw"
QUEUE_NAME = 'test'

def test():
    client = CloudAMQPClient(CLOUDAMQP_URL, QUEUE_NAME)

    demoMsg = {'test':'test msg'}
    client.sendMessage(demoMsg)
    client.sleep(10)
    recvMsg = client.getMessage()
    assert demoMsg == recvMsg
    print('test success')


if __name__ == '__main__':
    test()
