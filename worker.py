# DO: import threshhold, cachedCleanTime from globalVariables files

# Assumptions : workers and worker is just worker_id or worker_name not worker object

class Worker:
    def __init__(self, worker_id, threshhold):
        self.worker_id = worker_id
        self.threshhold = threshhold
        self.currentLoad = 0
        self.cachedPackages = []
        # Dict which shows last executed time for a package on this worker node
        self.lastExcecutedTime = {}
        # DO :self.threshhold = threshhold
        # DO : self.cacheCleanTime = cacheCleanTime
