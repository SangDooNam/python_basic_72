from worker import DeliveryMan, Packager



# Complete the method create_object
class WorkerFactory:
    @staticmethod
    def create_object(worker_type):
        if worker_type == 'delivery':
            return DeliveryMan()
        elif worker_type == 'packager':
            return Packager()
        raise TypeError('Unknown type')


