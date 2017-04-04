class Endpoint:
    def __init__(self, id_, datacenter_latency, amount_of_caches):
        self.id_ = id_
        self.datacenter_latency = datacenter_latency
        self.amount_of_caches = amount_of_caches
        self.cache_server_latencies = dict()

    def __repr__(self):
        return "Endpoint#{0}:\n" \
               "latency to datacenter: {1}, amount of cache servers: {2}\n" \
               "cache server latencies: {3}"\
            .format(self.id_, self.datacenter_latency,
                    self.amount_of_caches, self.cache_server_latencies)
