Kafka

```
docker exec -it <kafka-image> bash

kafka-topics --bootstrap-server localhost:9092 --create --topic ndov_xml --partitions 1 --replication-factor 1
```

Hadoop winutils for Spark Kafka Stream:

https://github.com/steveloughran/winutils

Commited & Available Offset Reset

- Delete checkpoints folder
- Set CURRENT-OFFSET to LOG-END-OFFSET on Kafka shell

```
kafka-consumer-groups --bootstrap-server localhost:9092 --group --all-groups --topic ndov_xml --reset-offsets <offset> --execute
```

```
kafka-topics --bootstrap-server localhost:9092 --delete --topic ndov_xml

kafka-topics --bootstrap-server localhost:9092 --create --topic ndov_xml --partitions 1 --replication-factor 1

kafka-consumer-groups --bootstrap-server localhost:9092 --list
```
