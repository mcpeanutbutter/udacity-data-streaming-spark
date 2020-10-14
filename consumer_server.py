  
import asyncio
from confluent_kafka import Consumer

async def consume(topic_name):
    consumer = Consumer({
        'bootstrap.servers': 'localhost:9092',
        'group.id' : 0
    })
    
    consumer.subscribe([topic_name])
    
    while True:
        messages = consumer.consume()
        
        for message in messages:
            if message is None:
                pass
            elif message.error() is not None:
                print(f'Error: {message.error()}')
            else:
                print(f'{message.value()}\n')
                
        await asyncio.sleep(0.5)
                
            
def run_kafka_consumer():
    asyncio.run(consume('com.udacity.police.calls'))    

        
if __name__ == '__main__':
    run_kafka_consumer()



# def consume(topic_name):
#     consumer = KafkaConsumer(
#         bootstrap_servers = ["localhost:9092"]
#         )
    
#     consumer.subscribe(topic_name)
    
#     while True:
#         messages = consumer.poll()
        
#         for message in messages:
            
#             print(type(message))
#             print(message.value)
# #             if message is None:
# #                 pass
# #             elif message.error() is not None:
# #                 print(f'Error: {message.error()}')
# #             else:
# #                 print(f'{message.value()}\n')

#         time.sleep(0.5)

# if __name__ == '__main__':
#     consume('com.udacity.police.calls')