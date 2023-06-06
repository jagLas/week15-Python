phones = [
    {
        "brand": "Apple",
        "model": "iPhone 13 Pro",
        "cost": 929,
        "color": "alpine green"
    },
    {
        "brand": "Samsung",
        "model": "Galaxy S22+",
        "cost": 999,
        "color": "black"
    },
    {
        "brand": "Google",
        "model": "Pixel 6",
        "cost": 599,
        "color": "kinda coral"
    },
    {
        "brand": "Apple",
        "model": "iPhone 13 Pro",
        "cost": 929,
        "color": "gold"
    },
    {
        "brand": "Google",
        "model": "Pixel 6",
        "cost": 599,
        "color": "stormy black"
    }
]

# Write your code here.

def get_unique_models(phone_list):
    return set(map(lambda phone: phone['model'], phone_list))

def map_to_names(phone_list):
    return phone_list

unique_models = list(get_unique_models(phones))
print(unique_models)                # iPhone 13 Pro, Galaxy S22+, Pixel 6 (dictionaries)
print(map_to_names(unique_models))  # iPhone 13 Pro, Galaxy S22+, Pixel 6