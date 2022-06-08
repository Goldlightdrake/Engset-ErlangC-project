import os

from models.Engset import Engset
from models.ErlangC import ErlangC

SEPERATOR = "\n################################\n"


class Controller:
    def __init__(self):
        self.initial_dialog()
        self.data = ""
        self.chosen_model = input("Choose one of the models (a or b): ")
        if self.chosen_model == "a":
            self.input_for_engset()
            self.functions_for_enkset()
        else:
            self.input_for_erlang_c()
            self.functions_for_erlang_c()
        print(self.data)
        self.exit_dialog()

    @staticmethod
    def initial_dialog():
        print(SEPERATOR)
        print("Presentation of models: ")
        print("a) Engset")
        print("b) ErlangC")
        print(SEPERATOR)

    def input_for_engset(self):
        print(SEPERATOR)
        print("Chosen model - Engset\n")
        print("Input fields:")
        print(" - number_of_customers(float)")
        print(" - arrival_rate(float)")
        print(" - service_rate(float)")
        print(SEPERATOR)
        number_of_customers = float(input("number_of_customers: "))
        arrival_rate = float(input("arrival_rate: "))
        service_rate = float(input("service_rate: "))
        self.chosen_model = Engset(
            number_of_customers=number_of_customers,
            arrival_rate=arrival_rate,
            service_rate=service_rate,
        )

    def input_for_erlang_c(self):
        print(SEPERATOR)
        print("Chosen model - Erlang C\n")
        print("Input fields:")
        print(" - number_of_calls(int)")
        print(" - period_of_time(int)")
        print(" - avg_handling_time(int)")
        print(" - required_service_level(int)")
        print(" - target_answer_time(int)")
        print(SEPERATOR)
        number_of_calls = int(input("number_of_calls: "))
        period_of_time = int(input("period_of_time: "))
        avg_handling_time = int(input("avg_handling_time: "))
        required_service_level = int(input("required_service_level: "))
        target_answer_time = int(input("target_answer_time: "))
        self.chosen_model = ErlangC(
            number_of_calls=number_of_calls,
            period_of_time=period_of_time,
            avg_handling_time=avg_handling_time,
            required_service_level=required_service_level,
            target_answer_time=target_answer_time
        )

    def functions_for_enkset(self):
        print(SEPERATOR)
        print("Chosen model - Engset\n")
        print("Available functions:")
        print(" 1) expected_number_of_customers_in_queue(float)")
        print(" 2) expected_number_of_customers_in_system(float)")
        print(" 3) expected_waiting_time_in_queue(float)")
        print(" 4) expected_time_in_system(float)")
        print(SEPERATOR)
        user_input = -1
        while user_input != 0:
            user_input = int(input("Choose function to display (press 0 to exit): "))
            if user_input == 1:
                print("Expected number of customers in queue: ")
                output = self.chosen_model.expected_number_of_customers_in_queue()
                print(output)
                self.write_to_data("Expected number of customers in queue: ")
                self.write_to_data(output)
            elif user_input == 2:
                print("Expected number of customers in system: ")
                output = self.chosen_model.expected_number_of_customers_in_system()
                print(output)
                self.write_to_data("Expected number of customers in system: ")
                self.write_to_data(output)
            elif user_input == 3:
                print("Expected waiting time in queue: ")
                output = self.chosen_model.expected_waiting_time_in_queue()
                print(output)
                self.write_to_data("Expected waiting time in queue: ")
                self.write_to_data(output)
            elif user_input == 4:
                print("Expected time in system: ")
                output = self.chosen_model.expected_time_in_system()
                print(output)
                self.write_to_data("Expected time in system: ")
                self.write_to_data(output)
            else:
                print("Wrong input try again!")

    def functions_for_erlang_c(self):
        print(SEPERATOR)
        print("Chosen model - Erland C\n")
        print("Available functions:")
        print(" 1) number_of_required_agents(int)")
        print(" 2) service_level(float)")
        print(" 3) probability_call_will_wait(float)")
        print(" 4) avg_speed_of_answer(float)")
        print(" 5) percentage_of_calls_answered_immediately(float)")
        print(SEPERATOR)
        user_input = -1
        while user_input != 0:
            user_input = int(input("Choose function to display (press 0 to exit): "))
            if user_input == 1:
                print("Total number of Agents Required: ")
                output = self.chosen_model.number_of_required_agents()
                print(output)
                self.write_to_data("Total number of Agents Required: ")
                self.write_to_data(output)
            elif user_input == 2:
                print("Service Level: ")
                output = self.chosen_model.service_level() + "%"
                print(output)
                self.write_to_data("Service Level: ")
                self.write_to_data(output)
            elif user_input == 3:
                print("Probability a call has to wait: ")
                output = str(round(self.chosen_model.probability_call_will_wait() * 100, 2)) + "%"
                print(output)
                self.write_to_data("Probability a call has to wait: ")
                self.write_to_data(output)
            elif user_input == 4:
                print("Average Speed of Answer: ")
                output = str(self.chosen_model.avg_speed_of_answer()) + " seconds"
                print(output)
                self.write_to_data("Average Speed of Answer: ")
                self.write_to_data(output)
            elif user_input == 5:
                print("% of calls Answered Immediately: ")
                output = str(self.chosen_model.percentage_of_calls_answered_immediately()) + "%"
                print(output)
                self.write_to_data("% of calls Answered Immediately: ")
                self.write_to_data(output)
            else:
                print("Wrong input try again!")

    def write_to_data(self, output: str):
        self.data += (str(output) + "\n")

    def write_to_file(self):
        with open("./data/" + f"{self.chosen_model}.txt", "x") as output_file:
            output_file.write(self.data)

    def exit_dialog(self):
        print(SEPERATOR)
        save = input("Would you like to save your data to file? (y/n): ").lower()
        if save == "y" or save == "yes":
            self.write_to_file()
            print(f"Your file has been saved in data folder check under {self.chosen_model} name.")
        print("Thanks for using our small project!")
        print("@Authors Zofia Żukowicz and Piotr Graczyk")
