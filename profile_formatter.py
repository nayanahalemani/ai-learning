# Demonstrates Python string operations using formatter

name="nayana halemani"
role="SDET"
Skills="Manual testing, Automation, Selenium, C#, Javascript, Python"



# Clean and format strings
clean_name=name.strip().title()
clean_role=role.title().upper()


# Create formatted profile summary
profile_summary=(
    f"Name   :{clean_name}\n"
    f"Role   :{clean_role}\n"
    f"Skills :{Skills}"
)

# Decorative header
header= "professional profile".upper()
line="-" *len(header)

# Output
print(line)
print(header)
print(line)
print(profile_summary)

# Extra string operations
print("\nProfile Summary Length: ",len(profile_summary))