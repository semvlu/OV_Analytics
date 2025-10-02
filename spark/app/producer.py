# https://htmwiki.nl/#!hackathon/realtime.md
from gzip import GzipFile
from io import BytesIO
import zmq
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

topic = "ndov_xml"

# save_dir = os.path.join(os.path.dirname(__file__), "../data")
# os.makedirs(save_dir, exist_ok=True)

# cnt = 0

context = zmq.Context()

subscriber = context.socket(zmq.SUB)
subscriber.connect("tcp://pubsub.besteffort.ndovloket.nl:7658")
subscriber.setsockopt_string(zmq.SUBSCRIBE, "/GVB/KV6posinfo")
subscriber.setsockopt_string(zmq.SUBSCRIBE, "/GVB/KV17cvlinfo")

while True:
    multipart = subscriber.recv_multipart()
    address = multipart[0]
    contents = b''.join(multipart[1:])
    try:
        with GzipFile(fileobj=BytesIO(contents)) as gz:
            decompressed = gz.read()
        print('GZIP', address, contents, decompressed)

        '''
        # Save file for debugging
        filename = os.path.join(save_dir, f"kv6_{int(time.time())}_{cnt}.xml")
        with open(filename, "wb") as f:
            f.write(decompressed)

        print(f"Saved XML: {filename}")
        cnt += 1
        '''
        
        producer.send(topic, decompressed)
        producer.flush()
        
    except Exception as e:
        print('NOT GZIP', address, contents, e)

subscriber.close()
context.term()