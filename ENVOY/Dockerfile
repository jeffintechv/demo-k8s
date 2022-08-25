FROM envoyproxy/envoy:v1.22-latest

RUN apt-get update && apt-get -q install -y \
    curl \
    dnsutils
COPY envoy.json /etc/envoy.json
CMD /usr/local/bin/envoy -c /etc/envoy.json
