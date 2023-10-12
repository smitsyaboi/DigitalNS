import datetime
import re
import matplotlib.pyplot as plt

"""
Log Analysis Program

This program reads log entries and analyzes them to track the occurrences of different components through the day, 
categorized into total counts and counts during working hours (9:00 to 17:00) and after working hours.

The program processes log entries in the following manner:
- It extracts the timestamp and component information from each log entry.
- It maintains a dictionary to store the total count of each component throughout the day.
- It determines whether each log entry falls within working hours or after working hours.
- It maintains separate dictionaries for counts during working hours and after working hours for plotting.


Usage:
- pip install matplotlib
- Ensure the log entries are provided in the log_file_path var.
- The program will output component counts for the full day, and plot during working hours, and after working hours.

Author: Joshua Smith
Date: 2023-09-21
"""

# Define regular expression pattern to parse log entries
logEntryPattern = r'(\w{3} \d{2} \d{2}:\d{2}:\d{2}) (\w+) (\S+)\[(\d+)\]: (.+)'
logFilePath = r'part2.log' 


# Create dictionaries to store component counts for working hours and after hours
workingHoursComponents = {}
afterHoursComponents = {}
totalComponents = {}

# Open the log file
with open(logFilePath, 'r') as log_file:
    for line in log_file:
        # Parse the log entry
        match = re.match(logEntryPattern, line)
        if match:
            timestamp_str, _, component, _, _ = match.groups()

            # Component counts for the full day
            totalComponents[component] = totalComponents.get(component, 0) + 1
            
            # Convert the timestamp to a datetime object
            timestamp = datetime.datetime.strptime(timestamp_str, '%b %d %H:%M:%S')
            
            # Check if the entry is during working hours (9:00 to 17:00)
            is_working_hours = 9 <= timestamp.hour <= 17
            
            # Update component counts for the appropriate time period
            if is_working_hours:
                workingHoursComponents[component] = workingHoursComponents.get(component, 0) + 1
            else:
                afterHoursComponents[component] = afterHoursComponents.get(component, 0) + 1

# Find and print the three most commonly used components
commonComponents = sorted(totalComponents.items(), key=lambda x: x[1], reverse=True)[:3]
print("Three most common components for the day:")
for component, count in commonComponents:
    print(f"{component}: {count} times")

# Create a plot to show component usage during working hours and after hours
workingHoursLabels = list(workingHoursComponents.keys())
workingHoursCounts = list(workingHoursComponents.values())
afterHoursLabels = list(afterHoursComponents.keys())
afterHoursCounts = list(afterHoursComponents.values())

plt.figure(figsize=(12, 6))
plt.bar(workingHoursLabels, workingHoursCounts, label='Working Hours', alpha=0.7)
plt.bar(afterHoursLabels, afterHoursCounts, label='After Hours', alpha=0.7)
plt.xlabel('Components')
plt.ylabel('Entry Count')
plt.title('Component Usage During Working Hours and After Hours')
plt.xticks(rotation=45, ha='right')
plt.legend()
plt.tight_layout()
plt.show()
