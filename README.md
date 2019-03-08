# pinocchio
you need to have docker and have created a docker network. <br />
just do: docker network create kafka-demo-network <br />

and then (in three separate terminal) <br />
docker-compose -f docker-compose-kafka.yml up (the kafka+zookeeper) <br />
docker-compose -f docker-compose-pinocchio.yml up --build (the producer) <br />
docker-compose -f docker-compose-consumer-only.yml up --build (the consumer) <br />
