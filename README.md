# pinocchio

(in three separate terminal)
docker-compose -f docker-compose-kafka.yml up (the kafka+zookeeper)
docker-compose -f docker-compose-pinocchio.yml up --build (the producer)
docker-compose -f docker-compose-consumer-only.yml up --build (the consumer)
