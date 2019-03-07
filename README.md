# pinocchio

(in three separate terminal)
docker-compose -f docker-compose-kafka.yml up (the kafka+zookeeper) <br />
docker-compose -f docker-compose-pinocchio.yml up --build (the producer) <br />
docker-compose -f docker-compose-consumer-only.yml up --build (the consumer) <br />
