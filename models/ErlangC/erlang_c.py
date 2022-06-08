import math


# The Erlang C class takes in the number of calls, the period of time, the average handling time, the
# required service level, and the target answer time. It then calculates the number of agents required
# to meet the required service level.

class ErlangC:
    def __init__(self, number_of_calls: int, period_of_time: int, avg_handling_time: int, required_service_level: int,
                 target_answer_time: int):
        self.__number_of_calls = number_of_calls
        self.__period_of_time = period_of_time
        self.__avg_handling_time = avg_handling_time
        self.__required_service_level = required_service_level
        self.__target_answer_time = target_answer_time
        self.__number_of_agents = self.raw_number_of_agents()
        self.calculate_number_of_agents()

    def __str__(self):
        return "Erlang C"

    def traffic_intensity(self) -> int:
        """
        The function takes the number of calls and the average handling time and returns the traffic
        intensity
        :return: The traffic intensity is being returned.
        """
        total_calls = self.__number_of_calls * (self.__avg_handling_time / 60)
        return round(total_calls / 60)

    def raw_number_of_agents(self) -> int:
        """
        > The raw number of agents is the traffic intensity plus one
        :return: The raw number of agents in the system.
        """
        return self.traffic_intensity() + 1

    def calculate_number_of_agents(self) -> int:
        """
        "While the required service level is greater than the current service level, add one to the
        number of agents."
        
        The function starts by setting the number of agents to raw_number_of_agents. Then, it enters a while loop. The
        while loop will continue to run as long as the required service level is greater than the
        current service level
        """
        while self.__required_service_level > self.service_level():
            self.__number_of_agents += 1

    def probability_call_will_wait(self) -> float:
        """
        The probability that a call will wait is the probability that there are N agents busy, divided
        by the probability that there are N agents busy or N agents idle
        :return: The probability that a call will wait.
        """
        A = self.traffic_intensity()
        N = self.__number_of_agents
        x = (A**N / math.factorial(N)) * (N / (N - A))
        y = sum([(A**i) / math.factorial(i) for i in range(N)])
        return x / (y + x)

    def service_level(self) -> float:
        """
        The service level is the probability that a call will be answered within the target answer time
        :return: The service level is being returned.
        """
        A = self.traffic_intensity()
        N = self.__number_of_agents
        x = self.probability_call_will_wait()
        y = math.exp(-((N - A) * (self.__target_answer_time /
                     self.__avg_handling_time)))
        return round((1 - (x * y)) * 100, 2)

    def avg_speed_of_answer(self) -> float:
        """
        The average speed of answer is the probability that a call will wait times the average handling
        time divided by the number of agents minus the traffic intensity.
        :return: The average speed of answer is being returned.
        """
        x = self.probability_call_will_wait() * self.__avg_handling_time
        y = self.__number_of_agents - self.traffic_intensity()
        return x / y

    def percentage_of_calls_answered_immediately(self) -> float:
        """
        The percentage of calls answered immediately is the probability that a call will not wait
        :return: The percentage of calls answered immediately.
        """
        return round((1 - self.probability_call_will_wait()) * 100, 2)

    def maximum_occupancy(self) -> float:
        """
        This function returns the maximum occupancy of the system as a percentage
        :return: The maximum occupancy of the system.
        """
        return round((self.traffic_intensity() / self.__number_of_agents) * 100, 2)

    def number_of_required_agents(self) -> int:
        """
        The number of required agents is the number of agents divided by one minus the shrinkage divided
        by 100.
        :return: The number of agents required to be hired.
        """
        shrinkage = 30  # Took from wikipedia
        return round(self.__number_of_agents / (1 - (shrinkage / 100)))
