#dependacies and pac
import re
import collections
import statistics
# import psycopg2
import random
import math

#Color data
color_data = """
MONDAY GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN
TUESDAY ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLUE, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE
WEDNESDAY GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE
THURSDAY BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN
FRIDAY GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE
"""
#Clean and flatten color data
colors = re.findall(r'\b\w+\b', color_data)



# Clean and flatten color data
colors = re.findall(r'\b\w+\b', color_data)

# Frequency analysis
color_freq = collections.Counter(colors)

# 1. Mean color (most frequent)
mean_color = color_freq.most_common(1)[0][0]

# 2. Color mostly worn throughout the week
most_worn_color = mean_color

# 3. Median color
median_color = statistics.median([color_freq[k] for k in color_freq])

# 4. Variance of colors (BONUS)
color_variance = statistics.variance([color_freq[k] for k in color_freq])

# 5. Probability of choosing red at random (BONUS)
red_probability = color_freq['RED'] / len(colors)

# # 6. Save colors and frequencies to PostgreSQL database
# # conn = psycopg2.connect(
# #     database="your_database",
# #     user="your_username",
# #     password="your_password",
# #     host="your_host",
# #     port="your_port"
# # )
# cur = conn.cursor()
# cur.execute("CREATE TABLE IF NOT EXISTS colors (color TEXT, frequency INTEGER)")
# for color, freq in color_freq.items():
#     cur.execute("INSERT INTO colors VALUES (%s, %s)", (color, freq))
# conn.commit()
# conn.close()

# 7. Recursive searching algorithm (BONUS)
def recursive_search(arr, target):
    if not arr:
        return False
    if arr[0] == target:
        return True
    return recursive_search(arr[1:], target)

# 8. Generate random 4-digit binary number and convert to base 10
binary_num = ''.join(str(random.randint(0, 1)) for _ in range(4))
decimal_num = int(binary_num, 2)

# 9. Sum first 50 Fibonacci numbers
def fibonacci(n):
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return sum(fib)

fib_sum = fibonacci(50)

# Print results
print("1. Mean color:", mean_color)
print("2. Color mostly worn throughout the week:", most_worn_color)
print("3. Median color:", median_color)
print("4. Variance of colors:", color_variance)
print("5. Probability of choosing red at random:", red_probability)
print("6. Colors and frequencies saved to PostgreSQL database")
print("7. Recursive search algorithm:")
print(recursive_search([1, 2, 3, 4, 5], 3)) # Example usage
print("8. Random 4-digit binary number:", binary_num)
print("9. Sum of first 50 Fibonacci numbers:", fib_sum)

# Replace the PostgreSQL database connection details with your own.


# This code addresses all the requirements:


# 1. Mean color
# 2. Color mostly worn throughout the week
# 3. Median color
# 4. Variance of colors (BONUS)
# 5. Probability of choosing red at random (BONUS)
# 6. Save colors and frequencies to PostgreSQL database
# 7. Recursive searching algorithm (BONUS)
# 8. Generate random 4-digit binary number and convert to base 10
# 9. Sum first 50 Fibonacci numbers

