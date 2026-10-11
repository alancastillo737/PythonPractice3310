# The pattern starts with 7 stars and decreases to 1.
# We set the starting number of stars to 7.
star_count = 7

# Outer loop: Handles the rows (7 rows in total)
for i in range(star_count):
    # Calculate the number of stars for the current row
    # Row 0: 7 stars, Row 1: 6 stars, ..., Row 6: 1 star
    current_row_stars = star_count - i
    
    # Inner loop: Handles the columns (printing stars in a single row)
    for j in range(current_row_stars):
        # Print a star, replace newline with empty space to stay on the same line
        print("*", end="")
    
    # Move to the next new line at the end of each outer-loop iteration
    print()