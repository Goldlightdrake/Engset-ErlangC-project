

# The Engset class is a class that calculates the expected number of customers in the queue, the
# expected number of customers in the system, the expected waiting time in the queue, and the expected
# time in the system.

class Engset:
    def __init__(self, number_of_customers: float, arrival_rate: float, service_rate: float):
        self.__number_of_customers = number_of_customers
        self.__arrival_rate = arrival_rate
        self.__service_rate = service_rate

    def __str__(self):
        return "Engset"

    def __system_utlization(self):
        """
        The system utilization is the ratio of the arrival rate to the service rate
        :return: The system utilization is being returned.
        """
        return self.__arrival_rate / self.__service_rate

    def expected_number_of_customers_in_queue(self) -> float:
        """
        The expected number of customers in the queue is the number of phrasers plus one divided by two
        times the number of phrasers times the arrival rate squared divided by the service rate minus the
        arrival rate.
        :return: The expected number of customers in the queue.
        """
        a = (self.__number_of_customers + 1) / 2 * self.__number_of_customers
        b = self.__arrival_rate**2 / self.__service_rate * \
            (self.__service_rate - self.__arrival_rate)
        return round(a * b, 2)

    def expected_number_of_customers_in_system(self) -> float:
        """
        The expected number of customers in the system is the expected number of customers in the queue
        times the system utilization.
        :return: The expected number of customers in the system.
        """
        return round(self.expected_number_of_customers_in_queue() * self.__system_utlization(), 2)

    def expected_waiting_time_in_queue(self) -> float:
        """
        The expected waiting time in queue is the number of phrasers plus one divided by two times the
        number of phrasers times the arrival rate divided by the service rate minus the arrival rate.
        :return: The expected waiting time in queue.
        """
        a = (self.__number_of_customers + 1) / 2 * self.__number_of_customers
        b = self.__arrival_rate / self.__service_rate * \
            (self.__service_rate - self.__arrival_rate)
        return round(a * b, 2)

    def expected_time_in_system(self) -> float:
        """
        > The expected time in system is the expected waiting time in queue plus the expected service time
        :return: The expected time in the system is the expected waiting time in the queue plus the
        expected service time.
        """
        return round(self.expected_waiting_time_in_queue() + 1 / self.__service_rate, 2)
