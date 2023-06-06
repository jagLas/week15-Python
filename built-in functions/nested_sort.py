teachers = [
    {
        "name": "Emily Richardson",
        "subjects": ["Geometry", "Geometry Honors"],
        "years_active": 5,
        "classroom": {
            "building_id": "A",
            "room_number": 12,
            "capacity": 45
        }
    },
    {
        "name": "Richard Emilyson",
        "subjects": ["English 11", "AP English Language"],
        "years_active": 12,
        "classroom": {
            "building_id": "J",
            "room_number": 42,
            "capacity": 60
        }
    },
    {
        "name": "Richly Emiardson",
        "subjects": ["Chemistry", "Chemistry Honors", "AP Chemistry"],
        "years_active": 8,
        "classroom": {
            "building_id": "C",
            "room_number": 5,
            "capacity": 32
        }
    },
]

# Write your code here.

def sort_teachers_by_classroom_capacity(card_list):
    card_list = sorted(card_list, key=lambda card: card['classroom']['capacity'])
    return list(map(lambda card: card['name'], card_list))


print(sort_teachers_by_classroom_capacity(teachers)) 
# Richly Emiardson, Emily Richardson, Richard Emilyson
