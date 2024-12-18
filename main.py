def max_panels(roof_height, roof_width, panel_height, panel_width):
    max_count = 0

    orientations = [(panel_height, panel_width), (panel_width, panel_height)]
    for orientation in orientations:
        a, b = orientation

        for i in range((roof_height // a) + 1):
            horizontal_count = i * (roof_width // b)
            actual_length = roof_height - i * a
            vertical_count = (actual_length // b) * (roof_width // a)
            max_count = max(max_count, horizontal_count + vertical_count)

    return max_count

# print("Ejemplos:")
# print(max_panels(2, 4, 1, 2))  # 4
# print(max_panels(3, 5, 1, 2))  # 7
# print(max_panels(1, 10, 2, 2))  # 0

# print("\nEjemplos Propios:")
# print(max_panels(1, 10, 1, 2))  # 5
# print(max_panels(1, 10, 2, 1))  # 5
# print(max_panels(7, 3, 2, 2))  # 3
# print(max_panels(7, 3, 2, 1))  # 10
# print(max_panels(6, 4, 1, 3))  # 8