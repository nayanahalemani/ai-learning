# Simulate a mini test report system in Python that tracks test execution metrics and calculates pass rate.
"""
Test case ID (string)
Execution duration (float)
Timestamp (datetime)
Test result (bool)
Error handling for invalid input
"""
from datetime import datetime


print ("--------QA TEST EXECUTION LOGGER-------")

try:
    #String to get test case id form user
    test_case_id=input("Enter Test Case ID: ")

    execution_time= float(input("Enter execution time in second: "))

    result_input=input("Did the test passs? (yes/no): ").strip().lower()

    if result_input == "yes":
          test_passed=True
    elif result_input=="no":
          test_passed=False
    else:
         raise ValueError("Invalid input for test result. Please enter 'yes' or 'no'.")
    
    # datetime (Current timestamp)
    execution_time_stamp=datetime.now()

    print("TEST SUMMARY")
    print("Test Case Id      :", test_case_id)
    print("Execution Time    :", execution_time)
    print("Execution DateTime:", execution_time_stamp)
    print("Test Passed       :", test_passed)
except ValueError as ve:
    print("\n Input Error:", ve)

except Exception as e:
    print("\n Unexpected Error:", e)

finally:
    print("\n Execution logging completed.")
