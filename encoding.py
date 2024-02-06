def label_encoding(categories):
    label_dict = {}
    for i, category in enumerate(categories):
        label_dict[category] = i
    return label_dict


def one_hot_encoding(categories):
    unique_categories = sorted(set(categories))
    encoding = []
    for category in categories:
        encoding.append([1 if category == c else 0 for c in unique_categories])
    return encoding


if __name__ == "__main__":
    data = ["price", "capacity", "colour", "quantity", "quantity", "colour","price"]
    
    label_encoded = label_encoding(data)
    print("Label Encoded:", label_encoded)
    
    one_hot_encoded = one_hot_encoding(data)
    print("One-Hot Encoded:", one_hot_encoded)
