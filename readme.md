

# Readme

This repository contains my solution for the second project of the Udacity Data Streaming nanodegree. The solution was developed with the integrated Jupyterlab environment. 


## Running the code

First, the requirements need to be installed:
```
./start.sh
```
Zookeeper is then started with:
```
zookeeper-server-start config/zookeeper.properties
```
Next, we launch the Kafka server via:
```
kafka-server-start config/server.properties
```
The producer is then started using:
```
python kafka_server.py
```
We may test the producer in two different ways. First, via the kafka-console-producer:
```
kafka-console-consumer --bootstrap-server localhost:9092 --topic com.udacity.police.calls --from-beginning
```
and second, via a small Python script:
```
python consumer_server.py
```
Lastly, the proper Spark streaming app is run via:
```
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.3.4 --master local[*] --conf spark.ui.port=3000 data_stream.py 
```

## Screenshots

### Output of kafka-console-consumer

![Screenshot of kafka-console-consumer](/screenshots/consumer.png)

### Progress reporter

![Screenshot progress tracker for data_stream.py](/screenshots/progresstracker.png)

### Crime aggregation table

![Screenshot of crime aggregation table produced by data_stream.py](/screenshots/crime_aggregation.png)

### Spark Streaming UI

![Screenshot Spark UI for data_stream.py](/screenshots/spark_ui.png)

## Additional questions

### Question 1

> How did changing values on the SparkSession property parameters affect the throughput and latency of the data?

The value of `maxOffsetsPerTrigger` seems to have a strong effect. If it is too small, throughput can be limited and the streaming overhead per batch becomes quite significant. If it is too large, the processing time per batch is increased (which might need to be compensated for by increasing `processingTime`).

Common ways of managing Spark data flow, like setting the number of partitions, still apply in the streaming case and can affect throughput and latency. 


### Question 2
> What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?

- The aforementioned `maxOffsetsPerTrigger` has a significant effect
- The same holds true for `maxRatePerPartition` (maximum messages per time per partition).
- Due to the small scale of the project, the properties related to memory and cpu load (e.g. `spark.driver.memory`, `spark.executor.memory`, `spark.executor.cores`, ...)  play a rather small role and do not need to be heavily optimized. 


## Attributions
The following solution was used as guidance for the additional questions:
* **[enricomarchesin](https://github.com/enricomarchesin/spark-streaming-example)**




