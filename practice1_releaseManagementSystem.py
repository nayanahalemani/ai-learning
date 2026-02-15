bug_id=input("Enter bug id: ")
severity_level=(input("Enter severity level : ")).strip().lower()


try:

   if severity_level == "critical":
    print(f"Bug {bug_id} is Eligible for immediate hotfix")

   elif severity_level=="high":
    print("Bug {} should be fixed in current sprint", bug_id)

   elif severity_level=="medium":
    print("Bug {} can be fixed in next sprint", bug_id)

   elif severity_level=="low":
    print("Bug {} can be in backlog", bug_id)
     
   else:
      raise ValueError("Please enter severity level.")

except ValueError as ve:
 print("\n Invalid severity level. Use: critical, high, medium, or low.")

except Exception as e:
 print("\n Unexpected Error: ",e)

finally:
 print("\n Execution logging Completed")