docker build --platform linux/amd64 -t armswdev/learn-dev-container:amd64 .
docker build --platform linux/arm64 -t armswdev/learn-dev-container:arm64 .

docker push armswdev/learn-dev-container:amd64
docker push armswdev/learn-dev-container:arm64

docker manifest create armswdev/learn-dev-container:latest \
--amend armswdev/learn-dev-container:arm64 \
--amend armswdev/learn-dev-container:amd64

docker manifest push --purge armswdev/learn-dev-container:latest

