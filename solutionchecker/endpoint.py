class Endpoint:
    def __init__(self, endpoint_id, datacenter_latency, amount_of_caches):
        self.endpoint_id = endpoint_id
        self.datacenter_latency = datacenter_latency
        self.amount_of_caches = amount_of_caches
        self.cache_server_latencies = dict()

    def __repr__(self):
        return self.pretty_string_representation()

    def pretty_string_representation(self):
        return "Endpoint#{0}:\n" \
               "latency to datacenter: {1}, amount of cache servers: {2}\n" \
               "cache server latencies: {3}" \
            .format(self.endpoint_id, self.datacenter_latency,
                    self.amount_of_caches, self.cache_server_latencies)
