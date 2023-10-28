def remove_matching_letter(list1, list2):
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                list1.remove(list1[i])
                list2.remove(list2[j])
                return [list1 + ['*'] + list2, True]
    return [list1 + ['*'] + list2, False]


def main():
    name1 = input("Enter the name of the first person: ").lower().replace(" ", "")
    name2 = input("Enter the name of the second person: ").lower().replace(" ", "")

    list1 = list(name1)
    list2 = list(name2)

    proceed = True
    while proceed:
        result, proceed = remove_matching_letter(list1, list2)

    count = len(list1) + len(list2)
    result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

    split_index = (count % len(result)) - 1

    if split_index >= 0:
        right_half = result[split_index + 1:]
        left_half = result[:split_index]
        new_result = right_half + left_half
    else:
        new_result = result[:split_index]  # Ignore the last element

    while len(new_result) > 1:
        count = len(new_result)
        split_index = (count % len(new_result)) - 1

        if split_index >= 0:
            right_half = new_result[split_index + 1:]
            left_half = new_result[:split_index]
            new_result = right_half + left_half
        else:
            new_result = new_result[:split_index]  # Ignore the last element

    final_result = new_result[0]
    print(f"The relationship between {name1} and {name2} is: {final_result}")


if __name__ == "__main":
    main()